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
    const totalForms = document.getElementById('id_tracks-TOTAL_FORMS');
    const addBtn = document.getElementById('add-track-btn');
    const templateElement = document.getElementById('empty-form-template');

    if (container && totalForms && addBtn && templateElement) {
        addBtn.addEventListener('click', function () {
            const formCount = parseInt(totalForms.value);
            const newFormHtml = templateElement.textContent.trim().replace(/__prefix__/g, formCount);

            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = newFormHtml;

            container.appendChild(tempDiv);
            totalForms.value = formCount + 1;

            console.log('New form added, total now:', totalForms.value);
        });
    } else {
        console.warn('Required elements not found or template missing');
        console.log({ container, totalForms, addBtn, templateElement });
    }
});