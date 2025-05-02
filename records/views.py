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

# Detail View - Shows one record in full
@login_required
def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk, user=request.user)
    return render(request, 'records/record_detail.html', {'record': record})


# Create View - Allows the user to create a new record
@login_required
def record_create(request):
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('record_list')
    else:
        form = RecordForm()
    return render(request, 'records/record_form.html', {'form': form})