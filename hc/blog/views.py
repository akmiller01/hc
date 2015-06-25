from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.models import Tag
    

def index(request):
    #get the blog posts that are published
    posts = Post.objects.filter(published=True)
    for post in posts:
        post.tags = Tag.objects.filter(post__slug=post.slug)
    #now return the rendered template
    return render(request,'blog/index.html',{'posts':posts})

def post(request,slug):
    #get the Post object
    post = get_object_or_404(Post,slug=slug)
    tags = Tag.objects.filter(post__slug=post.slug)
    #now return the rendered template
    return render(request,'blog/post.html',{'post':post,'tags':tags})

def tag(request,slug):
    #get the Tag object
    tag = get_object_or_404(Tag,slug=slug)
    posts = Post.objects.filter(tag__name=tag.name)
    #now return the rendered template
    return render(request,'blog/tag.html',{'tag':tag,'posts':posts})
