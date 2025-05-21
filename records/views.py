from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Record, GENRE_CHOICES, RATING_CHOICES
from .forms import RecordForm, TrackFormSet


def index(request):
    """
    Display the homepage with a selection of staff-picked records.

    Returns:
        HttpResponse: Rendered homepage with staff picks if any exist (max 6).
    """
    staff_picks = Record.objects.filter(is_staff_pick=True)[:6]
    return render(request, 'records/index.html', {'staff_picks': staff_picks})


@login_required
def record_list(request):
    """
    Display a list of records owned by the logged-in user.

    Returns:
    HttpResponse: Rendered template showing a list of the user's records.
    """
    records = Record.objects.filter(user=request.user)
    recently_added = (
        Record.objects
        .filter(user=request.user)
        .order_by('-created_on')
    )[:6]
    return render(request, 'records/record_list.html', {
        'records': records,
        'recently_added': recently_added,
    })


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
    Create a new record and associated tracks, save it to the database.

    Returns:
        HttpResponse: Redirects to the record list if successful,
                      or renders the form with errors if not.
    """
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        formset = TrackFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            formset.instance = record
            formset.save()

            messages.success(
                request, f"Record '{record.title}' created successfully!"
                )
            return redirect('record_list')
    else:
        form = RecordForm()
        formset = TrackFormSet(prefix='tracks')
    return render(request, 'records/record_form.html', {
        'form': form,
        'formset': formset,
    })


@login_required
def record_update(request, pk):
    """
    Update an existing record owned by the
    logged-in user and it's associated tracks.

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
        formset = TrackFormSet(request.POST, instance=record)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('record_list')
    else:
        form = RecordForm(instance=record)
        formset = TrackFormSet(instance=record)
    return render(request, 'records/record_form.html', {
        'form': form,
        'formset': formset,
    })


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


@login_required
def record_collection(request):
    """
    Display a searchable and filterable collection of the user's records.
    """
    records = Record.objects.filter(user=request.user)

    # Handle filters
    search_query = request.GET.get('search', '')
    genre_filter = request.GET.get('genre', '')
    artist_filter = request.GET.get('artist', '')
    rating_filter = request.GET.get('rating', '')

    if search_query:
        records = records.filter(
            Q(title__icontains=search_query) | Q(artist__icontains=search_query)
        )

    if genre_filter:
        records = records.filter(genre=genre_filter)

    if artist_filter:
        records = records.filter(artist=artist_filter)

    if rating_filter:
        records = records.filter(rating=rating_filter)

    # Get distinct values for dropdowns
    genres = GENRE_CHOICES
    ratings = RATING_CHOICES
    artists = Record.objects.filter(user=request.user).values_list('artist', flat=True).distinct().order_by('artist')

    return render(request, 'records/record_collection.html', {
        'records': records,
        'genres': genres,
        'ratings': ratings,
        'artists': artists,
        'search_query': search_query,
        'selected_genre': genre_filter,
        'selected_artist': artist_filter,
        'selected_rating': rating_filter,
    })


def custom_404_view(request, exception):
    """
    Custom handler for 404 errors.
    """
    return render(request, '404.html', status=404)
