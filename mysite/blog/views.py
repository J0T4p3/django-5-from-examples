from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    post_list = Post.published.all()
    # Paginator with 3 items pe page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        # If not found, returns the last page
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # If page is another value type than an integer
        posts = paginator.page(1)

    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post,
                             publish__day=day, publish__month=month, publish__year=year)
    return render(request, 'blog/post/detail.html', {'post': post})
