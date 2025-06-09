# Vinyl Crate - Testing

--

> [!NOTE]  
> Return back to the [README.md](README.md) file.

This document outlines the testing processes and results for the **Vinyl Crate** application. It ensures that all key features function correctly, provide a responsive and accessible user experience, and meet the expectations defined by the project requirements. Both manual and automated testing methods were used throughout the development process.

---

<a id=contents></a>

## CONTENTS

- [AUTOMATED TESTING](#automated-testing)
  - [W3C Validator](#w3c-validation)
  - [W3C CSS Validator](#css-validation)
  - [JavaScript Validator](#js-validation)
  - [Lighthouse](#lighthouse)
- [MANUAL TESTING](#manual-testing)
  - [Full Testing](#full-testing)
  - [Browser Compatibility](#browser)
  - [Responsiveness](#responsiveness)
  - [Accessibility](#accessibility)
  - [Testing User Stories](#testing-user)
  - [Features Testing](#features-test)
  - [Existing Features](#existing-features)
  - [Manual Features Testing](#manual-features-test)

<br>
<hr>

Testing was an **integral part of the development process**, ensuring that the Vinyl Crate application remained both **functional and user-friendly** at every stage. Through **continuous testing**, issues were identified and resolved early, contributing to a smoother development workflow and a more reliable final product.

**Chrome Developer Tools** were used extensively to monitor page responsiveness, diagnose styling and layout issues, and debug JavaScript and form interactions. This allowed for efficient troubleshooting and performance tuning during both frontend and backend development.

**ChatGPT** was a key support resource throughout the project. It helped refine user flows, debug Django logic, structure testing strategies, and optimize content and interface decisions. The guidance received led to more maintainable code, better practices, and improved overall project quality.

To ensure the site was **responsive and accessible across devices**, all views and forms were manually tested on a range of screen sizes using Chrome’s responsive design mode, alongside physical testing on **desktops, laptops, tablets, and smartphones**. Special attention was given to form interactions, navigation flow, and data display across breakpoints to guarantee a **consistent user experience**.

---

<a id=w3c-validation></a>

### W3C Validator

[W3C Validator](https://validator.w3.org/) was used to check the HTML and CSS across all pages of the site. Since Django’s templating language is embedded within the HTML files, I viewed the rendered page source in the browser and submitted that output to the validator to ensure accuracy.

| Page tested | Result | Evidence |
| --------- | ------ | ---------- |
| Home | Pass | [Home Page Validation](documentation/testing/validation/w3c-home.webp) |
| Dashboard | Pass | [Dashboard Page Validation](documentation/testing/validation/w3c-dashboard.webp) |
| My Crate  | Pass | [My Crate Page Validation](documentation/testing/validation/w3c-my-crate.webp) |

---

<a id=css-validation></a>

### CSS Validator

[CSS W3C Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS file.

| File tested | Result | Evidence |
| ----------- | ------ | -------- |
| base/style.css    | [base/style.css validation](documentation/testing/validation/w3c-style-css.webp) |

<a id=automated-testing></a>

## Automated Testing

Automated testing was a critical part of the development process for **Vinyl Crate**, ensuring that key components of the application worked reliably across various user scenarios. The testing suite was designed to cover **models, forms, views, and admin methods** using Django’s built-in [TestCase](https://docs.djangoproject.com/en/4.1/topics/testing/overview/) framework, supported by [coverage](https://pypi.org/project/coverage/) for reporting.

### Scope of Automated Testing

The automated test suite was planned and executed to cover the following key areas:

#### Models
- **Record** and **Track** models
- Field definitions, validation constraints, default values, and foreign key relationships
- Basic model creation with valid and invalid data

#### Forms
- **RecordForm**, **TrackForm**, and **CustomSignupForm**
- Required field validation, custom error messages, widget rendering
- Optional vs required fields behaviour (e.g. blank BPM or musical key)
- Edge cases, such as rating and BPM outside allowed range, or invalid year input

#### Views
- Coverage of all major views:
  - `index`, `record_list`, `record_detail`
  - `record_create`, `record_update`, `record_delete`
  - `record_collection`, and `custom_404_view`
- GET and POST requests tested using `client.get()` and `client.post()`
- Authentication requirements enforced and verified
- Context data verified (e.g. record queryset, staff picks, filter options)
- Template rendering assertions using `assertTemplateUsed`

#### Admin
- `cover_thumb()` logic tested explicitly
- Ensures graceful fallback for records with missing or broken images
- Admin display robustness validated separately from frontend logic

#### User Flow
- Simulated signup flow using `CustomSignupForm`
- Verifies correct storage of first and last name fields
- Checks that optional fields do not block signup
- Error handling for missing username or password mismatches

#### Tools Used

| Tool | Purpose |
| ---- | ------- |
| Django TestCase | Core unit and integration test framework |
| Client() | Simulates authenticated and anonymous users |
| coverage.py | Measures line and branch coverage |
| htmlcov/ | Visual review of missed lines and test quality |

#### Test Files

| File Name | Contents | 
| ---- | ------- |
| tests_forms.py | RecordForm validation and required field logic |
| tests_forms_track.py | TrackForm validation, optional fields, and data types |
| tests_forms_signup.py | Signup logic and first/last name persistence |
| tests_views.py | All key views covered including CRUD and 404 |
| tests_admin.py | Admin thumbnail image rendering logic |

#### Coverage

Testing was monitored using `coverage.py`, and line-by-line analysis was conducted to identify and address gaps. Areas typically hard to reach (like admin methods or error branches) were tested explicitly. Coverage reached a high level, with all business-critical logic tested and documented.

#### Edge Cases Covered
- Submitting forms with missing, invalid, or out-of-range data
- Submitting a record with no title (invalid)
- Filtering/searching records with multiple query params
- Authenticated vs unauthenticated access (e.g. attempting to view a record without login)
- Trying to update/delete records not owned by the user
- Rendering views with no records (empty states and onboarding)
- Handling missing or corrupted image files in the admin interface
- Custom 404 handling with missing templates and bad URLs

### Summary

This comprehensive automated test suite ensures that Vinyl Crate is robust, secure, and scalable. It gave confidence to iterate rapidly, knowing that regressions would be caught early in development.