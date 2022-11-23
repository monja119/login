import requests
import openvpn_api
from django.shortcuts import render, redirect
from django.http import request, response, HttpResponse
from app.forms import Authentificaton


def home(request):
    # form validation ?
    form = Authentificaton(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        return HttpResponse('Authentification success')
    else:
        # setting proxy
        proxies = {
            'http': 'http://127.0.0.1:80',
            'https': 'https://127.0.0.1:8080'
        }

        # target validator url
        url = 'http://localhost:8000'

        # authorisation
        response_auth = requests.get(url, proxies=proxies, auth=('email', 'password'))

        if response_auth.status_code == 200:
            form = Authentificaton()
            return render(request, 'pages/login.html', locals())
        else:
            return HttpResponse(f'Error : {response_auth.status_code}')


def vpn_test(request):
    vpn = openvpn_api.VPN('localhost', 800)
    try:
        if vpn.connect():
            return HttpResponse('connected')
        else:
            return HttpResponse('Not connected')
    except Exception as e:
        return HttpResponse('Error : {}'.format(e))