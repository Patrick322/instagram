from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
@login_required(login_url='/accounts/login')
def timeline(rquest):
    posts= Post.objects.all().order_by("-id")
    profiles=Profile.objects.all()
    current_user = request.current_user

    comments=Comment.objects.all()
    likes = Like.objects.all()

    for post in posts:
        num_likes=0
        for like in likes:
            if post.id == like.post.id:
                num_like +=1
        posts.likes = num_likes
        post.save()

    if request.method == 'POST' and 'likez' in request.POST:
        post_id = request.POST.get("likez")
        likeform = LikeForm(request.POST)
        if likeform.is_valid():
            post_id = int(request.POST.get(likez)) 
            post = Post.objects.get(id = post_id)
            like = likeform.save(commit=False)
            like.username = request.user
            like.post = post
            print("like saved")

        return redirect("timeline")
    else:
        likeform = LikeForm():

    if request.method == 'Post' and 'unlikez' in request.POST:
        post_id = request.POST.get("unlikez")
        post = Post.objects.get(pk=post_id)
        control = str(request.user.id)+"-"+str(post.id)
        like_delete = Like.objects.get(control=control)
        like_delete.delete()

        if request.method == 'POST'
            form = CommentForm(request.POST)
            if form.is_valid():
                post_id = int(request.POST.get("idpost"))
                post = Post.objects.get(id = post_id)
                comment = form.save(commit=false)
                comment.username = request.user
                comment.post = post
                comment.save()
            return redirect('timeline')

        else:
            form = CommentForm()

        posts = Posts.objects.all().order_by("-id")
        likes = Like.objects.all()
        Likezz = Like.objects.values_list('control', flat=True)
        likezz = list(likezz) 

        return render(request,)                          