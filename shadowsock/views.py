from django.shortcuts import render
from django.db import connection
from shadowsock.models import user,account
from django.http.response import HttpResponse
import base64
import json
# Create your views here.
def yanzheng(request,imei):
    for us in user.objects.all():
        convert = base64.b64encode(us.imei)
        if convert== imei: 
            #return HttpResponse("ke yi shang wang")
            return getconfig()
    return HttpResponse("bu ke yi shang wang")            
def getconfig():
    config=account.objects.all()[0];
    response_data={}
    response_data['server'] = config.proxy
    response_data['server_port'] = config.remotePort
    response_data['password'] = config.sitekey
    response_data['method'] = config.encMethod
    return HttpResponse(json.dumps(response_data), content_type="application/json")