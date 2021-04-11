from django import forms

from .models import Voter, Candidate


class VotingModelForm(forms.ModelForm):
    class Meta:
        model = Voter
        
        fields =[
            'name',
			'rolno',
			'Username',
			'Password',
        ]

class CandidateModelForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields =[
            'name',
			'rolno',
			'symbol',
			
        ]

class LoginModelForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields =[
			'Username',
			'Password',
        ]

