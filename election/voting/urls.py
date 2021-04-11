from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import (
    VoterCreateView,
    VoterDetailView,
    VoterListView,
    CandidateCreateView,
    CandidateDetailView,
    CandidateListView,
    LoginTemplateView,
   )
from django.conf.urls.static import static
from django.conf import settings
from voting.views import overall, Voter_detail_view,results

app_name = 'voting'


urlpatterns =[

	path('voter/', VoterListView.as_view(), name='voter-list'),	
	path('voter/vot-create/', VoterCreateView.as_view(), name='voter-create'),
	path('voter/<int:id>/', VoterDetailView.as_view(), name='voter-detail'),
	path('candidate/', CandidateListView.as_view(), name='candi-list'),	
	path('candidate/candi-create/', CandidateCreateView.as_view(), name='candi-create'),
	path('candidate/<int:id>/', CandidateDetailView.as_view(), name='candi-detail'),
	path('overall/', overall, name='overall-list'),
	path('voter-login/', LoginTemplateView.as_view(), name='ovelist'),
	path('voter-login/<int:id>/vote/', Voter_detail_view, name='vote'),
	path('results/', results, name='results'),
	

] 