from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime
from trips.models import Post
# Create your views here.
#def Hello_world(request):
def hello_world(request):
    return render(request,
                  'hello_world.html',
                  {'current_time': datetime.now()},dirs=('templates',))
def home(request):
    # get all the posts
    post_list = Post.objects.all()
    return render(request,
                  'home.html',
                  {'post_list': post_list},dirs=('templates',))
    