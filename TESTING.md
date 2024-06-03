# Petlover  - Testing

![Mock-up](https://res.cloudinary.com/dmhdrvehj/image/upload/v1711016918/mock-up_rfmhf4.png)

[Click here to view the live web application](https://petlover-6900a2845617.herokuapp.com/)

Back to [README.MD](README.md)

# Testing

- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)

- [Responsiveness](#responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Manual Testing](#manual-testing)
- [User Story Testing](#user-story-testing)

## Code Validation

### HTML

I ran the code for all the pages through the [W3C HTML Validator](https://validator.w3.org/nu/) using the textarea input by generating the source code from the deployed site (right click and select 'View Page Source' in Chrome) and pasting it in to allow me to check all pages whether requiring log in or not. All code passed the validation tests. Results below.

<details><summary>HTML Validation Results Table</summary>

| **Feature** | **Expected Outcome** | **Test Performed** | **Result** | **Pass / Fail** |
|---|---|---|---|---|
| **HOME** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | closing tag error in footer (/ul)- resolved | PASS |
| **LISTINGS** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | Page passes validation with no errors | PASS |
| **SINGLE LISTING** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ |Closing tag error in seller details (/a)| PASS |
| **CREATE AND EDIT LISTINGS** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ |  No errors | PASS |
| **MY PROFILE** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ |  Page passes validation no errors | PASS |
| **MY LISTINGS** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **EDIT PROFILE** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | Page passes validation no errors | PASS |
| **DELETE PROFILE** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **LOGIN** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **SIGN UP** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **SIGN OUT** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |

</details>

---

### CSS Validation

I ran the CSS code through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input). All code passed the validation tests. Results below.


<details><summary>CSS Validation Results Table</summary>

| **Feature**    | **Expected Outcome**                  | **Test Performed**                                   | **Result**                                                                                                              | **Pass / Fail** |
|----------------|---------------------------------------|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------|
| CSS Validation | Page passes validation with no errors | Ran CSS through https://jigsaw.w3.org/css-validator/ | no errors | PASS            |

</details>

<details><summary>Validation Final Results Screenshot</summary>

<img src="https://res.cloudinary.com/dmhdrvehj/image/upload/v1717279231/deblhc6uynu71mcxtv6z.png">

</details>

---

### JavaScript

I ran the JavaScript code through [JSHint](https://jshint.com/). For full results see the dropdowns below.

<details><summary>JavaScript Results Table</summary>

| **Feature** | **Expected Outcome** | **Test Performed** | **Result** | **Pass / Fail** |
|---|---|---|---|---|
| **script.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | No Errors | PASS |

</details>

---

### Python

I ran the app.py code through [https://pep8ci.herokuapp.com/](https://pep8ci.herokuapp.com/) to check the Syntax. GitPod also has a built in Python Linter which was used throughout the development process (see below). All code passed the validation tests. For full results see the dropdowns below.

<details><summary>Python Results Table</summary>

| **App** | **File** | **Expected Outcome** | **Test Performed** | **Result** | **Pass / Fail** |
|---|---|---|---|---|---|
| Petlover | settings | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | whitespace errors | PASS |
| Petlover | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| home | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| home | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Line too long | PASS |
| home | choice | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | whitespace errors | PASS |
| home | forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | whitespace errors | PASS |
| home | models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | whitespace errors | PASS |
| home | signals | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | whitespace errors | PASS |

</details>

---

## Responsiveness

The manual testing was done on the following devices

- Dell laptop 14 inch
- Apple iPhone 13 pro max
- Oneplus 10

## Browser Compatibility

|Browser|Result|Pass/Fail|Notes|
| --- | --- | --- | ---|
| Google Chrome | All pages, load as expected. All features work as expected | PASS | --- |
| Firefox | All pages, load as expected. All features work as expected | PASS | --- |
| Edge | All pages, load as expected. All features work as expected | PASS | ---|