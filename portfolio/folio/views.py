from django.shortcuts import render
from .forms import StateForm
from .models import States
from django.http import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
	if request.is_ajax():
		if request.method == "POST":
			form = StateForm(request.POST)
			if form.is_valid():
				state = form.save_state()
			return JsonResponse({"state_name":state.state_name})
		states_array=[]
		if request.method == "GET":
			states = States.objects.all()
			for state in states:
				states_array.append(state.state_name)
			return JsonResponse({"data":states_array})
	return render(request,'folio/index.html')
