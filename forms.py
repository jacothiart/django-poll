from django import forms

from .models import Poll


class PollForm(forms.ModelForm):

    class Meta:
        model = Poll
        exclude = ('user',)


class PollVoteForm(forms.Form):
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

    def construct(self, instance):
        if not instance.multiple_choice:
            self.fields['choice'] = forms.ChoiceField(widget=forms.RadioSelect)

        self.fields['choice'].choices = ((choice.pk, choice.choice_text)
                                         for choice in instance.choice_set.all())
