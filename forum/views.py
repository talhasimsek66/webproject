from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()
    return render(request, "forum_html/home.html", {'posts':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id = id)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user.username
            new_comment.email = request.user.email
            new_comment.save()
            return redirect('forum:post_detail', id=post.id)
        return None
    else:
        form = CommentForm()
        return render(request, 'forum_html/post_detail.html', {'post': post, "comments": comments, "comment_form": form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("forum:home")

    else:
        form = PostForm()
    return render(request, "forum_html/post_edit.html", {"form": form})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("forum:home")

@login_required
def add_comment(request):
    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(user=request.user, content=content)
        return redirect('forum:forum_page')
    return render(request, 'account/add_comment.html')

from django.shortcuts import render
from .models import Comment

def forum_page(request):
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'account_html/home.html', {'comments': comments})