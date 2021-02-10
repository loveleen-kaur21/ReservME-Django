from django.shortcuts import render
from django.views.generic import TemplateView
from ReservME.models import GuestandPaymentInfo

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class InformationView(DetailView):
    model = GuestandPaymentInfo
    template_name = 'information.html'
    fields = ['room_type', 'room_id', 'availability', 'full_name', 'address', 'email', 'zipcode', 'state', 'phone', 'company', 'card_number', 'csv', 'expiration', 'card_holder']
    