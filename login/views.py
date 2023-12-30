from django.shortcuts import render, redirect
from django.http import HttpResponse


def logout(request):
    try:
        del request.session['member_id']
        del request.session['member_type']
        del request.session['name']
    except KeyError:
        pass
    return redirect('function')
