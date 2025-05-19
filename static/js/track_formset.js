document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('formset-container');
    const totalForms = document.getElementById('id_form-TOTAL_FORMS');
    const addBtn = document.getElementById('add-track-btn');
    const emptyForm = document.getElementById('empty-form-template').innerHTML;

    if (addBtn) {
        addBtn.addEventListener('click', function () {
            const formCount = parseInt(totalForms.value);
            const newForm = emptyForm.replace(/__prefix__/g, formCount);
            container.insertAdjacentHTML('beforeend', newForm);
            totalForms.value = formCount + 1;
        });
    }
});