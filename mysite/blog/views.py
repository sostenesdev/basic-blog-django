from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from blog.models import Post


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)

    return render(request, 
        'blog/post/list.html',
        {'page':page,'posts':posts})
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, 
                    status='published', 
                    publish__year=year,
                    publish__month=month,
                    publish__day=day,
                    )
    print(post)
    return render(request,'blog/post/detail.html',{'post':post})