from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from app.models import *

# Create your views here.
def index(request):

    ## Login request ##
    if request.method == "POST":

        ## Post Get's ##
        username = request.POST.get("username")
        password = request.POST.get("password")

        ## Login ##
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect(home)

    return render(request, 'index.html')

def signupPage(request):

    ## Signup request ##
    if request.method == "POST":

        ## Post Get's ##
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        birthdate = request.POST.get("birthdate")

        ## SignUp ##
        CNUser.createNewUser(username, birthdate, email, password)

        ## Returning to LoginPage(index) ##
        return redirect(index)

    return render(request, 'signupPage.html')

@login_required(login_url=index)
def home(request):

    if request.method == "POST":

        ## Collecting post data ##
        title = request.POST.get("title")
        content = request.POST.get("content")
        attachment = request.FILES.get("attachment")
        userOwner = request.user

        ## Creating post ##
        Post.newPost(title, content, attachment, userOwner)

        return redirect(home)

    return render(request, 'home.html')

@login_required(login_url=index)
def profilePage(request):

    userPosts = Post.objects.filter(userOwner = request.user)
    likes = PostLike.objects.filter(userOwner = request.user)

    if request.method == "POST":

        ## Collecting new data ##
        username = request.POST.get("username")
        bio = request.POST.get("bio")
        picutre = request.FILES.get("picture")

        ## Updating profile ##
        CNUser.updateInfos(request.user.id, username, bio, picutre)

        ## Redirecting to home ##
        return redirect(home)

    return render(request, 'profilePage.html', {'userPosts':userPosts, 'likes':likes})

@login_required(login_url=index)
def likeOptions(request, id):

    ## Storing the post target ##
    post = Post.objects.get(id=id)

    ## Checking for like or deslike
    try:
        like = PostLike.objects.get(post=post)

        PostLike.unLike(post, request.user)
        post.likes -= 1
        post.save()

        return redirect(profilePage)
    
    except:

        PostLike.giveLike(post, request.user)
        post.likes += 1
        post.save()

        return redirect(profilePage)