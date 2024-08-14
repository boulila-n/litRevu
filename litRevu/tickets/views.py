from itertools import chain

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import CharField, Value
from multi_form_view import MultiModelFormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .decorator import is_owner
from .forms import TicketForm, ReviewForm
from .models import Ticket, Review


class PostsListView(LoginRequiredMixin, ListView):
    """
        Liste de mes posts
    """
    model = Review
    template_name = 'tickets/liste.html'

    def get_context_data(self, **kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        # envoi requette à la base table:Ticket
        tickets = (Ticket.objects.filter(user=self.request.user.id)
                   .annotate(content_type=Value('TICKET', CharField())))
        reviews = (Review.objects.filter(user=self.request.user.id)
                   .annotate(content_type=Value('REVIEW', CharField())))
        posts = sorted(
            chain(tickets, reviews),
            key=lambda post: post.created_at,
            reverse=True
        )
        context.update({
            'post_list': posts
        })
        return context


class TicketCreateView(LoginRequiredMixin, CreateView):
    """
        Ticket create view
    """
    model = Ticket
    fields = ['title', 'description', 'image']

    # permission_required = 'ticketing.add_ticket'

    # session
    def get_success_url(self):
        return reverse_lazy('liste')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    """
        Ticket update view + securisation
    """
    model = Ticket
    fields = ['title', 'description', 'image']

    def get_success_url(self):
        return reverse_lazy('liste')

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # session
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    """
        Ticket delete view + securisation
    """
    model = Ticket

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('liste')


class ReviewWithTicket(MultiModelFormView):
    """
        Review form + ticket form + securisation
    """
    form_classes = {
        'ticket_form': TicketForm,
        'review_form': ReviewForm,
    }
    template_name = 'tickets/review_with_ticket.html'
    review_id = 0

    @method_decorator(is_owner)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # Update
    def get_objects(self):
        self.review_id = self.kwargs.get('pk', None)
        try:
            review = Review.objects.get(id=self.review_id)
        except Review.DoesNotExist:
            review = None
        return {
            'review_form': review,
            'ticket_form': review.ticket if review else None
        }

    def get_success_url(self):
        return reverse_lazy('liste')

    def forms_valid(self, forms):

        ticket = forms['ticket_form'].save(commit=False)
        print(ticket)
        ticket.user = self.request.user
        ticket.save()

        review = forms['review_form'].save(commit=False)
        review.ticket = ticket
        review.user = self.request.user
        review.save()
        return super(ReviewWithTicket, self).forms_valid(forms)


class ReviewWithoutTicket(LoginRequiredMixin, UpdateView):
    """
        Review update + securisation
    """
    model = Review
    fields = ['title_review', 'description_review', 'note']

    @method_decorator(is_owner)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('liste')


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    """
        Review delete + securisation
    """
    model = Review

    @method_decorator(is_owner)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('liste')
