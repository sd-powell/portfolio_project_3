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
    Display the logged-in user's dashboard.

    Retrieves all records belonging to the current user
    and calculates the total count.
    If the user has records, the latest 8 are shown
    in a "Recently Added" section.
    If the user has no records, a curated selection of
    staff picks is displayed instead.

    Context passed to the template includes:
    - records: All user-owned records
    - total_records: Count of all user-owned records
    - recently_added: Latest 8 records (if any)
    - staff_picks: Optional featured records for new users

    Returns:
        HttpResponse: Rendered 'record_list.html' dashboard template.
    """
    records = Record.objects.filter(user=request.user)
    total_records = records.count()
    recently_added = records.order_by('-created_on')[:8]

    context = {
        'records': records,
        'total_records': total_records,
        'recently_added': recently_added,
    }

    if total_records == 0:
        context['staff_picks'] = get_staff_picks()

    return render(request, 'records/record_list.html', context)


def record_detail(request, slug):
    """
    Display the details of a single public record.

    This view retrieves a record by its slug and displays its details,
    including cover image, title, artist, and associated metadata.
    It is accessible to both authenticated and unauthenticated users.

    If a `from` parameter is included in the query string, it is preserved
    to allow the user to return to their previous filtered collection view.

    Parameters:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the record to retrieve.

    Returns:
        HttpResponse: Rendered template with the record's details,
                    or 404 if the record is not found.
    """
    record = get_object_or_404(Record, slug=slug, user=request.user)

    previous_url = request.GET.get('from') or request.META.get('HTTP_REFERER')

    # Optional: Only allow back to known pages
    if previous_url and not previous_url.startswith(
        request.build_absolute_uri(reverse('record_collection'))
    ):
        previous_url = reverse('record_collection')

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
            - Redirects to the record detail on successful creation.
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
            return redirect('record_detail', slug=record.slug)
    else:
        form = RecordForm()
        formset = TrackFormSet(prefix='tracks')
    return render_record_form(request, form, formset)


@login_required
def record_update(request, slug):
    """
    Handle the update of an existing record and its associated tracks
    for the logged-in user.

    Retrieves the specified record by slug and ensures it belongs to the
    current user. Displays a pre-filled form and an inline formset to
    allow editing of both the record and its related tracks.

    On GET requests:
        - Displays the existing record and tracks.
        - Includes one extra blank track form to
        support JavaScript duplication.

    On POST requests:
        - Processes the submitted data without extra blank forms.
        - Saves updates only if both the record form and formset are valid.

    Parameters:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the record to be updated.

    Returns:
        HttpResponse:
            - Redirects to the record detail page on successful update.
            - Re-renders the form with validation errors otherwise.
    """
    record = get_object_or_404(Record, slug=slug, user=request.user)

    if request.method == 'POST':
        TrackFormSet = get_track_formset(extra=0)
        form = RecordForm(request.POST, request.FILES, instance=record)
        formset = TrackFormSet(request.POST, instance=record, prefix='tracks')
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(
                request, f"Record '{record.title}' updated successfully!"
                )
            return redirect('record_detail', slug=record.slug)
    else:
        TrackFormSet = get_track_formset(extra=1)
        form = RecordForm(instance=record)
        formset = TrackFormSet(instance=record, prefix='tracks')
    return render_record_form(request, form, formset)


@login_required
def record_delete(request, slug):
    """
    Delete an existing record owned by the logged-in user.

    Parameters:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the record to be updated.

    Returns:
        HttpResponse: Redirects to the record list after deletion,
                      or renders a confirmation page before deleting.
    """
    record = get_object_or_404(Record, slug=slug, user=request.user)
    if request.method == 'POST':
        title = record.title
        record.delete()
        messages.success(
            request, f"Record '{title}' was deleted successfully."
            )
        return redirect('record_collection')
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
    all_user_records = Record.objects.filter(user=request.user)
    total_records = all_user_records.count()

    records = all_user_records

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
        'total_records': total_records,
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


def custom_400_view(request, exception):
    """
    Custom handler for 400 errors.
    """
    return render(request, '400.html', status=400)
