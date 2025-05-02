from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Record
from .forms import RecordForm # Form to be created


# Create your views here.

