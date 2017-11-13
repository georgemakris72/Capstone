from django.shortcuts import redirect

from capstone import urls

from allauth.account.adapter import DefaultAccountAdapter

class AccountAdapter(DefaultAccountAdapter):

  def get_login_redirect_url(self, request):
      return '/'

  def get_logout_redirect_url(self,request):
      return '/'
