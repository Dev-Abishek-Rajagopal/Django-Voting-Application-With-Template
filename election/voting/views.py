from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django import forms
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
    TemplateView,
)
from .forms import VotingModelForm, CandidateModelForm,LoginModelForm
from .models import Voter, Candidate




class VoterCreateView(CreateView):
    template_name = 'voting/voter_create.html'
    form_class = VotingModelForm
    queryset = Voter.objects.all() # <blog>/<modelname>_list.html
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class VoterListView(ListView):
    template_name = 'voting/voter_list.html'
    queryset = Voter.objects.all()

class VoterDetailView(DetailView):
    template_name = 'voting/voter_detail.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Voter, id=id_)

class CandidateCreateView(CreateView):
    template_name = 'voting/candi_create.html'
    form_class = CandidateModelForm
    queryset = Candidate.objects.all() # <blog>/<modelname>_list.html
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CandidateListView(ListView):
    template_name = 'voting/candi_list.html'
    queryset = Candidate.objects.all()

class CandidateDetailView(DetailView):
    template_name = 'voting/candi_detail.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Candidate, id=id_)

def overall(request):
	queryset1 = Voter.objects.all()
	queryset2 = Candidate.objects.all()
	context = {
       "objectlist1":queryset1,
       "objectlist2":queryset2,
	}
	return render(request, "voting/overalllist.html", context)
	
class LoginTemplateView(TemplateView):
    template_name = 'voting/vot-login.html'
    form_class = LoginModelForm
    queryset = Voter.objects.all()

    def post(self,request):
    	form = LoginModelForm(request.POST)
    	queryset = Voter.objects.all()
    	if form.is_valid():
    		user = form.cleaned_data['Username']
    		passwd = form.cleaned_data['Password']
    		print(user)
    		
    		inbase = 'no'
    		for i in queryset:
    			if user == i.Username:
    				inbase = 'yes'
    				if i.cashing != 0 or i.cashing != None :
    					if passwd == i.Password:
    						print(i.cashing)
    						print(i.candidate)
    						vali = "Validation successful"
    						context = {
    						"form":form,
    						"vali":vali,
    						"id":i.id,
    						}
    					else:
    						vali ='Password Wrong!!!!!!!!!'
    						context = {
    						"form":form,
    						"vali":vali,
    						}
    					#raise forms.ValidationError("Password wrong")

    					
    					
    					return render(request,self.template_name,context)
    					
    				else:
    					vali = "You have already voted.. Get Lost!!!!...."
    					print(i.cashing)
    					print(i.candidate)
    					context = {
    					"form":form,
    					"vali":vali,
    					}
    					return render(request,self.template_name,context)

					
    					
			
    		if inbase == 'no':
    			vali = "User doesn't exit!!!!"
    			context = {
    					"form":form,
    					"vali":vali,
    					}
    			return render(request,self.template_name,context)
				

    	context = {
	        "form":form,
		}
    	return render(request,self.template_name,context)

    def get(self,request):
    	form = LoginModelForm()
    	context = {
	        "form":form,
		}
    	return render(request,self.template_name,context)


    
def Voter_detail_view(request,id):


	obj = Voter.objects.get(id=id)
	
	confirm = 0

	if obj.cashing == 0 and confirm == 0:
		queryset = Candidate.objects.all()
		queryset1 = Voter.objects.all()
		h_type = request.POST.get('vote')
		form = VotingModelForm()
		print(obj.cashing)

		if h_type is not None and confirm == 0:
			print(h_type)
			form = VotingModelForm(request.POST)
			obj.cashing = 1
			obj.candidate = int(h_type) 
			obj.save()
			obj1=Candidate.objects.get(id=queryset[obj.candidate-1].id)
			obj1.votes = obj1.votes + 1
			obj1.save()
			print(obj.cashing)
			print(obj.candidate)
			confirm = 1
			context ={
			"object":obj,
			"h_type":h_type,
			"obj":queryset[int(h_type)-1],

			}
			return render(request, "voting/vote.html",context)

		context ={
      	"object":obj,
      	"object_list":queryset,

		}
		return render(request, "voting/vote.html",context)

	return render(request, "voting/vote.html",{})
    
def election(request):
	
	return render(request, "voting/election.html", {})	


def results(request):
	queryset = Candidate.objects.all()
	queryset1 = Voter.objects.all()
	
	print("Then")

	context ={
		"queryset1":queryset1,
		"queryset":queryset,
		

		
		}
	
	return render(request, "voting/results.html", context)	

    	
    		

    	


    	


        

	    

