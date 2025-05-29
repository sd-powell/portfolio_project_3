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

<a id=automated-testing></a>

## Automated Testing

Automated testing was a critical part of the development process for **Vinyl Crate**, ensuring that key components of the application worked reliably across various user scenarios. The testing suite was designed to cover **models, forms, views, and admin methods** using Django’s built-in [TestCase](https://docs.djangoproject.com/en/4.1/topics/testing/overview/) framework, supported by [coverage](https://pypi.org/project/coverage/) for reporting.

### Scope of Automated Testing

The automated test suite was planned and executed to cover the following key areas:

#### Models
- Record and Track models
- Field definitions, validation constraints, and foreign key relationships
- Custom admin-related methods like cover_thumb

#### Forms
- RecordForm, TrackForm, and CustomSignupForm
- Required field validation, widget rendering, and error messages
- Edge cases, such as invalid field types and min/max values

#### Views
- Coverage of all views including:
    - index, record_list, record_detail
    - record_create, record_update, record_delete
    - record_collection and custom_404_view
- GET and POST requests tested
- Authentication requirements and redirect behaviour
- Context data and template rendering

#### Admin
- cover_thumb() logic tested directly via a unit test
- Ensures admin displays are handled gracefully even when image files are missing

#### User Flow
- Simulated signup flow using CustomSignupForm
- Verifying that first and last names are saved correctly
- Testing form validity with and without optional fields

#### Tools Used

| Tool | Purpose |
| ---- | ------- |
| Django TestCase | Core unit and integration test framework |
| Client() | Simulates authenticated and anonymous users |
| coverage.py | Measures line and branch coverage |
| htmlcov/ | Visual review of uncovered lines |

#### Test Files

| File Name | Contents | 
| ---- | ------- |
| tests_forms.py | RecordForm validation and field behaviour |
| tests_forms_track.py | TrackForm edge cases and optional field logic |
| tests_forms_signup.py | CustomSignupForm behaviour and save logic |
| tests_views.py | Comprehensive coverage of all views (GET, POST, context) |
| tests_admin.py | Admin-specific logic for image thumbnail display |

#### Coverage

Testing was monitored using coverage.py and all critical logic was covered. Where certain Django admin display methods were difficult to hit through normal use, explicit tests were written to trigger them directly and close coverage gaps.

#### Edge Cases Covered
- Submitting forms with missing or invalid data
- Submitting rating or BPM values outside allowed ranges
- Viewing pages as unauthenticated users (and being redirected)
- Filtering and searching combinations in record_collection
- Attempting to update or delete non-existent or unauthorized records
- Handling missing cover images in admin display

This automated test suite ensures that Vinyl Crate is robust, secure, and ready for real-world use. It also gave confidence to iterate quickly during development without breaking existing features.