from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    """
        Form tickets
    """
    class Meta(object):
        """
            Meta tickets
        """
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    """
        Form Review
    """
    class Meta(object):
        """
            Meta Review
        """
        model = Review
        fields = ['title_review', 'description_review', 'note']
