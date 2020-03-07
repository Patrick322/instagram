from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
@login_required(login_url='/accounts/login')
def timeline(request):
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


@login_required(login_url='/account/login')
def search_results(request)
if 'search' in request.GET and request.GET["search"]:
    search_term = request.GET.get("search")
    searched_users = user.search_user(search_term)
    messages = f"{search}"


    return render(request,)

else:
    messages="You have not searche for any term."
    return render(request, )


@login_required(login_url='/accounts/login')
def explore(request):
    posts = Posts.objects.all()
    profiles = Profile.objects.all[:5]


    return render(request)


@login_required(login_url='/accounts/login/')
def profile(request,id)
user_object = request.user
current_user = Profile.objects.get(username__id=request.user.id)
user = profile.objects.get(username__id=id)
posts = Post.objects.filter(upload_by = user)
follows = Folow.objects.all()

if request.method == 'POST' and 'follower' in request.POST:
    print("follow saved")
    followed_user_id = request.POST.get("follower")
    followform = FollowForm(request.POST)
    if followform.is_valid():
        followed_user_id = int(request.POST.get("follower"))
        current_user = Profile.objects.get(username__id=request.user.id)
        follow.username = request.user
        followed_user = user.objects.get(pk=followed_user_id)
        print(followed_user)
        follow.followed = followed_user
        follow.follow_id = str(follow.username.id)+"-"+str(follow.followed.id)
        follow.save()
        print("follow saved")

        return redirect("profile",username.id)
    else:
        followform = FollowForm()    

    if request.method =='POST' and 'unfollower' in request.POST:
        followed_user_id = request.POST.get("unfollower")
        followed_user = user.objects.get(pk=followed_user_id)
        follow_delete = Follow.objects.get(follow_id=follow_id)
        follow_delete.delete()


    follows = Follow.objects.all()
    followzz = Follow.objects.values_list('follow_id',flat=True)
    followzz = list(followzz)
    follower = 0
    following = 0
    for follow in followzz:
        follow = follow.split("-")
        if follow[0] == str(user.username.id):
            following+=1
        if follow[-1] == str(user.username_id)
            follower+=1

    return render(request, "profile.html")


    def following(request):
        if request.method == 'POST' and 'follower' in request.POST:
            print("follow saved")

@login_required(login_url='accounts/login')
def new_post(request):
    current_user = Profile.objects.get(username__id=request.user.id)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.upload_by = current_user
            post.save()
        return redirect('timeline')

    else:
        form = NewPostForm()
        return render(request, 'new_post.html', {"form":"form"})      

@login_required(login_url='accounts/login')
def edit_profile(request)     



