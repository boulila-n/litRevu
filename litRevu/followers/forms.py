from django import forms
from django.contrib.auth import get_user_model

PersonalUser = get_user_model()


class SubscribeForm(forms.Form):
    """
        Subscribe Form
    """
    def __init__(self, *args, **kwargs):
        """
            Exclude l'utilisateur connecté + ses abonnés
        """
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        user = PersonalUser.objects.filter(id=self.user.id).first()
        self.fields['subscribe'].queryset = (PersonalUser.objects
                                             .exclude(followers=user.id)
                                             .exclude(id=self.user.id))

    subscribe = forms.ModelChoiceField(queryset=None)
