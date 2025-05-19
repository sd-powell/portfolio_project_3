/**
 * Dynamically adds new track formsets to the record form.
 * 
 * - Clones a hidden empty form template
 * - Replaces __prefix__ with the current form count
 * - Appends the new form to the container
 * - Updates TOTAL_FORMS to track the new count
 */
document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('formset-container');
    const totalForms = document.getElementById('id_form-TOTAL_FORMS');
    const addBtn = document.getElementById('add-track-btn');
    const emptyForm = document.getElementById('empty-form-template').innerHTML;

    if (addBtn && container && totalForms && emptyForm) {
        addBtn.addEventListener('click', function () {
            const formCount = parseInt(totalForms.value);
            const newFormHtml = emptyForm.replace(/__prefix__/g, formCount);
            container.insertAdjacentHTML('beforeend', newFormHtml);
            totalForms.value = formCount + 1;
        });
    }
});