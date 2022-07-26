from django.shortcuts import render, get_object_or_404
from .models import Myblog

# Create your views here.
def all_blogs(request):
    posts = Myblog.objects.all()
    return render(request, 'blog/all_blogs.html', {'posts':posts})

def detail(request, blog_id):
    blog = get_object_or_404(Myblog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})