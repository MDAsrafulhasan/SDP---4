from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_author(request):
    if request.method == 'POST':      # user post request korse 
        author_form = forms.AuthorForm(request.POST)      #  user er post request er data ekhane rakhsi
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
    else:
        author_form = forms.AuthorForm()
    return render(request , 'add_author.html',{'form':author_form})