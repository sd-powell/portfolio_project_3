/**
 * Handles dynamic add/remove functionality for Django inline track formsets.
 *
 * Features:
 * - Adds new track forms by cloning a hidden template when "Add Another Track" is clicked
 * - Replaces Django's `__prefix__` placeholder with an updated index for new form elements
 * - Reindexes form field names, IDs, and labels after removal to maintain consistency
 * - Removes track forms:
 *    - Unsaved forms: completely removed from the DOM
 *    - Saved forms: marked for deletion via the DELETE checkbox and hidden
 * - Updates the `TOTAL_FORMS` input to reflect the current number of visible forms
 * - Initializes and refreshes Bootstrap tooltips for enhanced accessibility
 *
 * Ensures full compatibility with Django’s inline formset mechanism and Bootstrap UI behaviors.
 */
document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('formset-container');
    const totalForms = document.getElementById('id_tracks-TOTAL_FORMS');
    const addBtn = document.getElementById('add-track-btn');
    const templateElement = document.getElementById('empty-form-template');

    function updateRemoveButtons() {
        const removeButtons = container.querySelectorAll('.remove-track-btn');
        removeButtons.forEach(button => {
            button.removeEventListener('click', handleRemove); // prevent duplicates
            button.addEventListener('click', handleRemove);
        });
    }

    function handleRemove(e) {
        const trackForm = e.target.closest('.track-form');
        if (trackForm) {
            const deleteCheckbox = trackForm.querySelector('input[type="checkbox"][name*="DELETE"]');
            if (deleteCheckbox) {
                // For existing saved forms, mark for deletion and hide from view
                deleteCheckbox.checked = true;
                trackForm.style.display = 'none';
            } else {
                // For newly added forms, just remove from the DOM
                trackForm.remove();
                const forms = container.querySelectorAll('.track-form');
                totalForms.value = forms.length;

                // Update all form indexes
                forms.forEach((form, index) => {
                    form.querySelectorAll('input, select, textarea, label').forEach(el => {
                        if (el.name) {
                            el.name = el.name.replace(/tracks-\d+-/, `tracks-${index}-`);
                        }
                        if (el.id) {
                            el.id = el.id.replace(/tracks-\d+-/, `tracks-${index}-`);
                        }
                        if (el.htmlFor) {
                            el.htmlFor = el.htmlFor.replace(/tracks-\d+-/, `tracks-${index}-`);
                        }
                    });
                });
            }
        }
    }

    function refreshTooltips() {
        const tooltips = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltips.forEach(el => {
            new bootstrap.Tooltip(el);
        });
    }

    if (container && totalForms && addBtn && templateElement) {
        addBtn.addEventListener('click', function () {
            const formCount = parseInt(totalForms.value, 10);
            // Replace Django's __prefix__ placeholder with the current form index
            const newFormHtml = templateElement.innerHTML.replace(/__prefix__/g, formCount);

            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = newFormHtml;
            const newForm = tempDiv.firstElementChild;

            container.appendChild(newForm);
            totalForms.value = formCount + 1;

            updateRemoveButtons(); // reattach listeners for all
        });
        updateRemoveButtons(); // attach to initial forms
    } else {
        // Formset not present on this page; skipping dynamic form logic
    }

    // Initialize Bootstrap tooltips on page load
    refreshTooltips();

    // Enable Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
        new bootstrap.Tooltip(tooltipTriggerEl);
    });
});