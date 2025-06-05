/**
 * Handles dynamic add/remove of track formsets in the record form.
 * 
 * Features:
 * - Clones a hidden empty form template when "Add Another Track" is clicked
 * - Replaces __prefix__ in field names/IDs with the current form index
 * - Appends the new form to the formset container
 * - Adds a remove button to each formset
 * - Allows removing any formset and reindexes remaining forms
 * - Updates TOTAL_FORMS to match the current number of formsets
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
            trackForm.remove();
            // Update TOTAL_FORMS count
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

    if (container && totalForms && addBtn && templateElement) {
        addBtn.addEventListener('click', function () {
            const formCount = parseInt(totalForms.value);
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
        console.warn('Required elements not found or template missing');
    }
});