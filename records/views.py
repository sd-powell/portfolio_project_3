from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.forms import inlineformset_factory

from .models import Record, Track, GENRE_CHOICES, RATING_CHOICES
from .forms import RecordForm


def get_staff_picks(limit=6):
    """
    Retrieve a queryset of staff-picked records, limited to a specified number.

    Args:
        limit (int): Maximum number of records to return.

    Returns:
        QuerySet: Staff-picked records.
    """
    return Record.objects.filter(is_staff_pick=True)[:limit]


def get_track_formset(extra):
    """
    Create an inline formset for Track instances linked to a Record.

    Args:
        extra (int): Number of extra blank forms to display.

    Returns:
        InlineFormSet: The Track formset class.
    """
    return inlineformset_factory(
        Record,
        Track,
        fields=('title', 'position', 'duration', 'bpm', 'key'),
        extra=extra,
        can_delete=True
    )


def render_record_form(request, form, formset):
    """
    Render the shared form template for record creation and update.

    Args:
        request (HttpRequest): The current request.
        form (RecordForm): The main record form.
        formset (BaseInlineFormSet): The formset for associated tracks.

    Returns:
        HttpResponse: Rendered form template.
    """
    return render(request, 'records/record_form.html', {
        'form': form,
        'formset': formset,
    })


def index(request):
    """
    Display the public homepage featuring selected records.

    Retrieves up to six records marked as staff picks to showcase
    on the homepage. These are intended to highlight notable entries
    from the full database, regardless of the logged-in user.

    Returns:
        HttpResponse: Rendered homepage template with a
        list of staff-picked records.
    """
    staff_picks = Record.objects.filter(is_staff_pick=True)[:6]
    return render(request, 'records/index.html', {'staff_picks': staff_picks})


@login_required
def record_list(request):
    """
    Display the main dashboard view for the logged-in user's record collection.

    - If the user has records, show all their records and
    the six most recently added.
    - If the user has no records, also pass a 'staff_picks'
    queryset for onboarding content.

    Staff picks are selected records marked by admins or
    curators to help new users discover and add to their crate.

    Returns:
        HttpResponse: Rendered dashboard template with:
            - records: All user-owned records
            - recently_added: Latest eight records added by the user
            - staff_picks (optional): Highlighted records for new users
    """
    records = Record.objects.filter(user=request.user)
    recently_added = records.order_by('-created_on')[:8]

    context = {
        'records': records,
        'recently_added': recently_added,
    }

    if not records.exists():
        context['staff_picks'] = get_staff_picks()

    return render(request, 'records/record_list.html', context)


def record_detail(request, slug):
    """
    Display the details of a single public record.

    This view retrieves a record by its slug and displays its details,
    including cover image, title, artist, and any associated metadata.
    It is accessible to both authenticated and unauthenticated users.

    Parameters:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the record to retrieve.

    Returns:
        HttpResponse: Rendered template with the record's details,
                      or 404 if the record is not found.
    """
    record = get_object_or_404(Record, slug=slug)
    previous_url = request.META.get('HTTP_REFERER', reverse('record_list'))
    return render(request, 'records/record_detail.html', {
        'record': record,
        'previous_url': previous_url,
    })


@login_required
def record_create(request):
    """
    Handle the creation of a new record and its associated tracks.

    This view displays a form for the user to input a new record's details
    and any number of associated tracks. If the request method is POST and
    both the record and track forms are valid,
    the data is saved to the database.

    The record is automatically linked to the currently logged-in user.

    Returns:
        HttpResponse:
            - Redirects to the record list on successful creation.
            - Renders the form again with validation errors otherwise.
    """
    TrackFormSet = get_track_formset(extra=1)

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
    return render_record_form(request, form, formset)


@login_required
def record_update(request, pk):
    """
    Handle the update of an existing record and its associated tracks
    for the logged-in user.

    This view retrieves a record by its primary key (pk) and ensures it
    belongs to the current user. It displays a form pre-filled with the
    record’s existing data, along with an inline formset for editing
    associated tracks.

    If the request method is POST and both the record form and formset
    are valid, the updated data is saved to the database.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the record to be updated.

    Returns:
        HttpResponse:
            - Redirects to the record list on successful update.
            - Renders the edit form with validation errors otherwise.
    """
    record = get_object_or_404(Record, pk=pk, user=request.user)
    TrackFormSet = get_track_formset(extra=0)

    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES, instance=record)
        formset = TrackFormSet(request.POST, instance=record)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(
                request, f"Record '{record.title}' updated successfully!"
                )
            return redirect('record_list')
    else:
        form = RecordForm(instance=record)
        formset = TrackFormSet(instance=record)
    return render_record_form(request, form, formset)


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
        title = record.title
        record.delete()
        messages.success(
            request, f"Record '{title}' was deleted successfully."
            )
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
            (
                Q(title__icontains=search_query) |
                Q(artist__icontains=search_query)
            )
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
    artists = (
        Record.objects
        .filter(user=request.user)
        .values_list('artist', flat=True)
        .distinct()
        .order_by('artist')
    )

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


def custom_403_view(request, exception=None):
    """
    Custom handler for 403 errors.
    """
    return render(request, "403.html", status=403)
