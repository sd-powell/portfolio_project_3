from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Record
from .forms import RecordForm  # Form to be created


@login_required
def record_list(request):
    """
    Display a list of records owned by the logged-in user.

    Returns:
    HttpResponse: Rendered template showing a list of the user's records.
    """
    records = Record.objects.filter(user=request.user)
    return render(request, 'records/record_list.html', {'records': records})


@login_required
def record_detail(request, pk):
    """
    Display the details of a single record owned by the logged-in user.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): Primary key of the record to retrieve.

    Returns:
        HttpResponse: Rendered template with the record's details,
                      or 404 if not found or not owned by user.
    """
    record = get_object_or_404(Record, pk=pk, user=request.user)
    return render(request, 'records/record_detail.html', {'record': record})


@login_required
def record_create(request):
    """
    Create a new record and save it to the database.

    Returns:
        HttpResponse: Redirects to the record list if successful,
                      or renders the form with errors if not.
    """
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


@login_required
def record_update(request, pk):
    """
    Update an existing record owned by the logged-in user.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): Primary key of the record to update.

    Returns:
        HttpResponse: Redirects to the record list if successful,
                      or renders the form with errors if not.
    """
    record = get_object_or_404(Record, pk=pk, user=request.user)
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = RecordForm(instance=record)
    return render(request, 'records/record_form.html', {'form': form})


@login_required
def record_delete(request, pk):
    """
    Delete an existing record owned by the logged-in user.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): Primary key of the record to delete.

    Returns:
        HttpResponse: Redirects to the record list after deletion,
                      or renders a confirmation page before deleting.
    """
    record = get_object_or_404(Record, pk=pk, user=request.user)
    if request.method == 'POST':
        record.delete()
        return redirect('record_list')
    return render(
        request,
        'records/record_confirm_delete.html',
        {'record': record}
    )
