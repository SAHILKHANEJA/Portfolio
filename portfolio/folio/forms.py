from django import forms
from folio.models import States

class StateForm(forms.Form):
	state_name = forms.CharField(max_length=50)

	def save_state(self):
		state_name = self.cleaned_data['state_name']
		state = States(state_name=state_name)
		state.save()
		return state