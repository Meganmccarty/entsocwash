// The code below was taken and modified from Brian at Engineer to Developer following his formset tutorial
// https://engineertodeveloper.com/dynamic-formsets-with-django/

// Variables used for all functions
const mainForm = document.querySelector("#main_form");

// Phone
const phoneForm = document.getElementsByClassName("phone-form");
const addPhoneFormBtn = document.querySelector("#add-phone-form");
const totalPhoneForms = document.querySelector("#id_has_phones-TOTAL_FORMS");

let formPhoneCount = phoneForm.length - 1;

function updateForms() {
    let count = 0;
    for (let form of phoneForm) {
        const formRegex = RegExp(`has_phones-(\\d){1}-`, 'g');
        form.innerHTML = form.innerHTML.replace(formRegex, `has_phones-${count++}-`)
    }
}

addPhoneFormBtn.addEventListener("click", function (event) {
    event.preventDefault();

    const newPhoneForm = phoneForm[0].cloneNode(true);
    const newPhoneDelBtn = document.createElement("button")
    newPhoneDelBtn.className = "button btn-danger delete-phone-form"
    newPhoneDelBtn.innerText = "Delete"
    const formRegex = RegExp(`has_phones-(\\d){1}-`, 'g');

    formPhoneCount++;

    newPhoneForm.innerHTML = newPhoneForm.innerHTML.replace(formRegex, `has_phones-${formPhoneCount}-`);
    mainForm.insertBefore(newPhoneForm, addPhoneFormBtn);
    newPhoneForm.appendChild(newPhoneDelBtn);
    totalPhoneForms.setAttribute('value', `${formPhoneCount + 1}`);
});

mainForm.addEventListener("click", function (event) {
    if (event.target.classList.contains("delete-phone-form")) {
        event.preventDefault();
        event.target.parentElement.remove();
        formPhoneCount--;
        updateForms();
        totalPhoneForms.setAttribute('value', `${formPhoneCount + 1}`);
    }
});

// Geography
const geographyForm = document.getElementsByClassName("geography-form");
const addGeographyFormBtn = document.querySelector("#add-geography-form");
const totalGeographyForms = document.querySelector("#id_has_geographies-TOTAL_FORMS");

let formGeographyCount = geographyForm.length - 1;

function updateForms() {
    let count = 0;
    for (let form of geographyForm) {
        const formRegex = RegExp(`has_geographies-(\\d){1}-`, 'g');
        form.innerHTML = form.innerHTML.replace(formRegex, `has_geographies-${count++}-`)
    }
}

addGeographyFormBtn.addEventListener("click", function (event) {
    event.preventDefault();

    const newGeographyForm = geographyForm[0].cloneNode(true);
    const newGeographyDelBtn = document.createElement("button")
    newGeographyDelBtn.className = "button btn-danger delete-geography-form"
    newGeographyDelBtn.innerText = "Delete"
    const formRegex = RegExp(`has_geographies-(\\d){1}-`, 'g');

    formGeographyCount++;

    newGeographyForm.innerHTML = newGeographyForm.innerHTML.replace(formRegex, `has_geographies-${formGeographyCount}-`);
    mainForm.insertBefore(newGeographyForm, addGeographyFormBtn);
    newGeographyForm.appendChild(newGeographyDelBtn);
    totalGeographyForms.setAttribute('value', `${formGeographyCount + 1}`);
});

mainForm.addEventListener("click", function (event) {
    if (event.target.classList.contains("delete-geography-form")) {
        event.preventDefault();
        event.target.parentElement.remove();
        formGeographyCount--;
        updateForms();
        totalGeographyForms.setAttribute('value', `${formGeographyCount + 1}`);
    }
});

// Subject
const subjectForm = document.getElementsByClassName("subject-form");
const addSubjectFormBtn = document.querySelector("#add-subject-form");
const totalSubjectForms = document.querySelector("#id_has_subjects-TOTAL_FORMS");

let formSubjectCount = subjectForm.length - 1;

function updateForms() {
    let count = 0;
    for (let form of subjectForm) {
        const formRegex = RegExp(`has_subjects-(\\d){1}-`, 'g');
        form.innerHTML = form.innerHTML.replace(formRegex, `has_subjects-${count++}-`)
    }
}

addSubjectFormBtn.addEventListener("click", function (event) {
    event.preventDefault();

    const newSubjectForm = subjectForm[0].cloneNode(true);
    const newSubjectDelBtn = document.createElement("button")
    newSubjectDelBtn.className = "button btn-danger delete-subject-form"
    newSubjectDelBtn.innerText = "Delete"
    const formRegex = RegExp(`has_subjects-(\\d){1}-`, 'g');

    formSubjectCount++;

    newSubjectForm.innerHTML = newSubjectForm.innerHTML.replace(formRegex, `has_subjects-${formSubjectCount}-`);
    mainForm.insertBefore(newSubjectForm, addSubjectFormBtn);
    newSubjectForm.appendChild(newSubjectDelBtn);
    totalSubjectForms.setAttribute('value', `${formSubjectCount + 1}`);
});

mainForm.addEventListener("click", function (event) {
    if (event.target.classList.contains("delete-subject-form")) {
        event.preventDefault();
        event.target.parentElement.remove();
        formSubjectCount--;
        updateForms();
        totalSubjectForms.setAttribute('value', `${formSubjectCount + 1}`);
    }
});

// Taxonomy
const taxonomyForm = document.getElementsByClassName("taxonomy-form");
const addTaxonomyFormBtn = document.querySelector("#add-taxonomy-form");
const totalTaxonomyForms = document.querySelector("#id_has_taxons-TOTAL_FORMS");

let formTaxonomyCount = taxonomyForm.length - 1;

function updateForms() {
    let count = 0;
    for (let form of taxonomyForm) {
        const formRegex = RegExp(`has_taxons-(\\d){1}-`, 'g');
        form.innerHTML = form.innerHTML.replace(formRegex, `has_taxons-${count++}-`)
    }
}

addTaxonomyFormBtn.addEventListener("click", function (event) {
    event.preventDefault();

    const newTaxonomyForm = taxonomyForm[0].cloneNode(true);
    const newTaxonomyDelBtn = document.createElement("button")
    newTaxonomyDelBtn.className = "button btn-danger delete-taxonomy-form"
    newTaxonomyDelBtn.innerText = "Delete"
    const formRegex = RegExp(`has_taxons-(\\d){1}-`, 'g');

    formTaxonomyCount++;

    newTaxonomyForm.innerHTML = newTaxonomyForm.innerHTML.replace(formRegex, `has_taxons-${formTaxonomyCount}-`);
    mainForm.insertBefore(newTaxonomyForm, addTaxonomyFormBtn);
    newTaxonomyForm.appendChild(newTaxonomyDelBtn);
    totalTaxonomyForms.setAttribute('value', `${formTaxonomyCount + 1}`);
});

mainForm.addEventListener("click", function (event) {
    if (event.target.classList.contains("delete-taxonomy-form")) {
        event.preventDefault();
        event.target.parentElement.remove();
        formTaxonomyCount--;
        updateForms();
        totalTaxonomyForms.setAttribute('value', `${formTaxonomyCount + 1}`);
    }
});