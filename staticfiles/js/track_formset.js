/**
 * Handles dynamic add/remove functionality for track formsets in the record form.
 *
 * Features:
 * - Clones a hidden template form when "Add Another Track" is clicked
 * - Replaces __prefix__ placeholders with correct form indices
 * - Appends new track forms to the formset container
 * - Allows removal of track forms:
 *    - For newly added (unsaved) forms: removes from the DOM
 *    - For existing forms: checks the DELETE checkbox and hides the form
 * - Reindexes form fields and updates the management TOTAL_FORMS count
 *
 * Ensures compatibility with Django’s inline formset mechanism.
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

    if (container && totalForms && addBtn && templateElement) {
        addBtn.addEventListener('click', function () {
            const formCount = parseInt(totalForms.value);
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
});