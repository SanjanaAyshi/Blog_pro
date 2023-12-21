from django.shortcuts import render, redirect
from . import forms
# Create your views here.


def addProfile(request):
    if request.method == 'POST':
        profileForm = forms.ProfileFrom(request.POST)
        if profileForm.is_valid():
            profileForm.save()
            return redirect('add_Profile')

    else:
        profileForm = forms.ProfileFrom()
    return render(request, 'addProfile.html', {'form': profileForm})
