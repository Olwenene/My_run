from django import forms
from .models import Question

class Choiceform(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'candidate_biography_1', 'candidate_biography_2', 'candidate_biography_3']