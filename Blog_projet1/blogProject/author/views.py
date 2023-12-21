from django.shortcuts import render, redirect
# from .forms import AuthorForm
from . import forms


def addAuthor(request):
    if request.method == 'POST':
        authorForm = forms.AuthorFrom(request.POST)
        if authorForm.is_valid():
            authorForm.save()
            return redirect('add_Author')

    else:
        authorForm = forms.AuthorFrom()
    return render(request, 'addAuthor.html', {'form': authorForm})
