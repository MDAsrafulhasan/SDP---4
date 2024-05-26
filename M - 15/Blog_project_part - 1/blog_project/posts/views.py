from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def add_post(request):
    if request.method == 'POST':      # user post request korse 
        post_form = forms.PostForm(request.POST)      #  user er post request er data ekhane rakhsi
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.PostForm()
    return render(request , 'add_post.html',{'form':post_form})


def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)

    print(post.title)
    if request.method == 'POST':      # user post request korse 
        post_form = forms.PostForm(request.POST, instance=post)      #  user er post request er data ekhane rakhsi
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    # else:
    #     post_form = forms.PostForm()
    return render(request , 'add_post.html',{'form':post_form})

def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')