from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Record
from .forms import RecordForm # Form to be created


# Create your views here.

# List View – Shows all records belonging to the logged-in user
@login_required
def record_list(request):
    records = Record.objects.filter(user=request.user)
    return render(request, 'records/record_list.html', {'records': records})
