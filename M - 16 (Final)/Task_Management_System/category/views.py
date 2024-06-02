from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def CategoryViews(request):
    # categoryform = forms.CategoryForms()
    # return render(request, 'category.html' , {'categoryform': categoryform })
    if request.method == 'POST':
        categoryform = forms.CategoryForms(request.POST)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('add_category_page')
        
    else:
        categoryform = forms.CategoryForms()
        return render(request, 'category.html' , {'categoryform': categoryform })