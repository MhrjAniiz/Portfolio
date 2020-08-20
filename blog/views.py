from django.shortcuts import render,get_object_or_404
from . models import Blog

def all_blogs(request):
    blog = Blog.objects.order_by('-date')
    return render(request,'blog.html',{'blog':blog})


def detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blogdetail.html',{'blog':blog})