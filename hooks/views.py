from django.shortcuts import render
from accounts.models import api_keys
from django.views.generic import TemplateView
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

class Main(TemplateView):

   model = api_keys

   def get_context_data(self, **kwargs):
       #print(user.id)
       context = super(Main, self).get_context_data(**kwargs)
       result=api_keys.objects.filter(user_id=4).order_by("-id")[:1:1]
       context['api_key_lists'] = result
       context['user_info']=self.request.user.id
       context['client_api_key']=result[0].api_key
       context['client_api_secret_key']=result[0].api_secret_key

       client = Client(context['client_api_key'], context['client_api_secret_key'])
       return context
