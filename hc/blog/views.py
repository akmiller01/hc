from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post
from blog.models import Tag
    

def index(request):
    #get the blog posts that are published
    post_list = Post.objects.filter(published=True)
    paginator = Paginator(post_list,4) # Show 4 posts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        #If page is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)
    for post in posts:
        post.tags = Tag.objects.filter(post__slug=post.slug)
    #now return the rendered template
    return render(request,'blog/index.html',{'posts':posts})

def post(request,slug):
    #get the Post object
    post = get_object_or_404(Post,slug=slug)
    post.tags = Tag.objects.filter(post__slug=post.slug)
    #now return the rendered template
    return render(request,'blog/post.html',{'post':post})

def tag(request,slug):
    #get the Tag object
    tag = get_object_or_404(Tag,slug=slug)
    posts = Post.objects.filter(tag__name=tag.name)
    #now return the rendered template
    return render(request,'blog/tag.html',{'tag':tag,'posts':posts})
