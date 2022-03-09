# accounts/views.py

from .forms import UserRegisterForm
from django import forms

from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import api_keys

from django.views import generic
from django.views.generic import TemplateView

import pandas as pd
import json
import asyncio
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager,AsyncClient



#from django.core.mail import send_mail



class SignUpView(generic.CreateView):
    #form_class = UserCreationForm
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ApiKeysInfoView(TemplateView):
    #api key listesini ve başka bilgileri içerebilir home.html ye data atarken kullanıyorum
   model = api_keys
   #template_name = "blog/post_list.html"
   #queryset = api_keys.objects.all()

   #şablondan ulaşmak istenilen değişken adı
   #context_object_name = "test"

   #def get_context_data(self, **kwargs):
   def get_context_data(self, **kwargs):
       #print(user.id)
       context = super(ApiKeysInfoView, self).get_context_data(**kwargs)
       result=api_keys.objects.filter(user_id=self.request.user.id).order_by("-id")[:1:1]
       context['api_key_lists'] = result
       context['user_info']=self.request.user.id

       context['client_api_key']=result[0].api_key
       context['client_api_secret_key']=result[0].api_secret_key

       client = Client(context['client_api_key'], context['client_api_secret_key'])
       #info = client.get_all_tickers()
       info = client.get_account()
       #df = pd.DataFrame(info["balances"])
       #df["free"] = df["free"].astype(float).round(4)
       #df = df[df["free"] > 0]



       wallet_info=info["balances"]
       wallet =[]

       for val in wallet_info:
           if float(val['free']) > 0 :
               #print(val['free'])
              wallet.append(val)


       context['wallet_coin_lists']=wallet
       print(context['wallet_coin_lists'])
       #print(df)
       #print(info)


       #client = await AsyncClient.create()
       # fetch exchange info
        #res = client.get_exchange_info()
        #print(json.dumps(res, indent=2))


       #context={'api_key_lists': api_keys.objects.all(), 'soyadi': 2}
       return context



def ApiKeyAddView(request):
    if request.method == 'POST':
       q = api_keys(
            user_id=request.user.id,
            api_key=request.POST.get("api_key"),
            api_secret_key=request.POST.get("api_secret_key")
       )
       q.save()
       #return redirect(index)

       #send_mail(
        #'Mail başlığı',
        #'Mail içeriği',
        #'onerkerim1@yandex.com',
        #['onerkerim@me.com'],
        #fail_silently=False,
        #)



    return render(request,'api/api-key-add.html',locals())
