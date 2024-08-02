from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from app.models import Post


def echo_page(request):
    return render(request, "app/echo_page.html")


def liveblog_index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all()
    return render(request, "app/liveblog_index.html", {"post_list": post_list})


def post_partial(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)
    return render(request, "app/partial/post.html", {"post": post})
