from django import forms
from .game_facts import classes, ancestries, backgrounds
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ClassChoiceForm(forms.Form):
    ancestry_choice_field = [
        (k, cl) for k, cl in zip(range(len(ancestries)), ancestries)
    ]
    ancestry = forms.ChoiceField(choices=ancestry_choice_field, required=True)
    background_choice_field = [
        (k, ": ".join(background))
        for k, background in zip(range(len(backgrounds)), backgrounds)
    ]
    background = forms.ChoiceField(choices=background_choice_field, required=True)
    class_choice_field = [(k, cl) for k, cl in zip(range(len(classes)), classes)]
    class_ = forms.ChoiceField(choices=class_choice_field, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "create_pc"
        self.helper.add_input(Submit("submit", "Create PC"))
