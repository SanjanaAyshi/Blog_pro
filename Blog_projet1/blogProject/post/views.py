from django.shortcuts import render, redirect
# from .forms import AuthorForm
from . import forms
from . import models


def addPost(request):
    if request.method == 'POST':
        postForm = forms.PostFrom(request.POST)
        if postForm.is_valid():
            postForm.save()
            return redirect('add_post')

    else:
        postForm = forms.PostFrom()
    return render(request, 'addPost.html', {'form': postForm})


def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    postForm = forms.PostFrom(instance=post)
    if request.method == 'POST':  # user post request koreche
        # user er post request data ekhane capture korlam
        postForm = forms.PostFrom(request.POST, instance=post)
        if postForm .is_valid():  # post kora data gula amra valid kina check kortechi
            postForm .save()  # jodi data valid hoy taile database e save korbo
            # sob thik thakle take add author ei url e pathiye dibo
            return redirect('homepage')

    return render(request, 'addPost.html', {'form': postForm})


def deletePost(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
