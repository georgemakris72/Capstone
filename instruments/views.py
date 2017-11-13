from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Instrument

# Testing Signin imports

from allauth.account.views import SignupView
from allauth.account.forms import LoginForm

class CustomSignupView(SignupView):
    # here we add some context to the already existing context
    def get_context_data(self, **kwargs):
        # we get context data from original view
        context = super(CustomSignupView,
                        self).get_context_data(**kwargs)
        context['login_form'] = LoginForm() # add form to context
        return context

class InstrumentList(ListView):
    model = Instrument
    template_name= "instrument_list.html"

    #def productList(request):
        # product=Product.object.all()
        # template_name="product_list.html"
        # return render(request.template_name,{"object_list":product})


class InstrumentDetail(DetailView):
    model= Instrument


    def get_context_data(self, **kwargs):
        print(kwargs)
        template_name="instrument_detail.html"
        context = super(InstrumentDetail, self).get_context_data(**kwargs)
        print(context)
        return context

    def get_slug_field(self, **kwargs):
        print(kwargs)
        context= super(InstrumentDetail, self).get_slug_field(**kwargs)
        return context
