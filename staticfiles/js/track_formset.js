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
        container.querySelectorAll('.remove-track-btn').forEach(button => {
            button.removeEventListener('click', handleRemove); // prevent duplicates
            button.addEventListener('click', handleRemove);
        });
    }

    function reindexForms() {
        const forms = container.querySelectorAll('.track-form');
        forms.forEach((form, index) => {
            form.querySelectorAll('input, select, textarea, label').forEach(el => {
                if (el.name) el.name = el.name.replace(/tracks-\d+-/, `tracks-${index}-`);
                if (el.id) el.id = el.id.replace(/tracks-\d+-/, `tracks-${index}-`);
                if (el.htmlFor) el.htmlFor = el.htmlFor.replace(/tracks-\d+-/, `tracks-${index}-`);
            });
        });
        totalForms.value = forms.length;
    }

    function handleRemove(e) {
        const trackForm = e.target.closest('.track-form');
        if (!trackForm) return;

        const deleteCheckbox = trackForm.querySelector('input[type="checkbox"][name*="DELETE"]');
        if (deleteCheckbox) {
            deleteCheckbox.checked = true;
            trackForm.style.display = 'none';
        } else {
            trackForm.remove();
            reindexForms();
        }
    }

    function initTooltip(el) {
        return new bootstrap.Tooltip(el);
    }

    function refreshTooltips(scope = document) {
        const tooltips = scope.querySelectorAll('[data-bs-toggle="tooltip"]');
        tooltips.forEach(el => {
            /* global bootstrap */
            initTooltip(el);
        });
    }

    if (container && totalForms && addBtn && templateElement) {
        addBtn.addEventListener('click', function () {
            const formCount = parseInt(totalForms.value, 10);
            const newFormHtml = templateElement.innerHTML.replace(/__prefix__/g, formCount);

            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = newFormHtml;
            const newForm = tempDiv.firstElementChild;

            container.appendChild(newForm);
            totalForms.value = formCount + 1;

            updateRemoveButtons();
            refreshTooltips(newForm);
        });

        updateRemoveButtons();
        refreshTooltips(container);
    }
});