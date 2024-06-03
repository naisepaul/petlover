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
- [Lighthouse](#lighthouse)
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

## Lighthouse

<details><summary>Lighthouse</summary>

|Page|Validator|Result|
| --- | --- | --- |
| Home Desktop |![home](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717413761/lighthouse-home-desktop_izh5mh.png) | <mark>PASS<mark> |
| Home Mobile |![home](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717413761/lighthouse-home-mobile_nqrp24.png) | <mark>PASS<mark> |
| Listings Desktop|![listings](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717413761/lighthouse-listing-desktop_vsahxl.png) | <mark>PASS<mark> |
| Listings Mobile|![listings](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717413761/lighthouse-listing-mobile_wbjppy.png) | <mark>PASS<mark> |
| Single Listing Desktop|![Single Listing](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717413761/lighthouse-Single-listing-desktop_nzspdq.png) | <mark>PASS<mark> |
| Single Listing Mobile|![Single Listing](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717413761/lighthouse-Single-listing-mobile_urzfqe.png) | <mark>PASS<mark> |
| Log In Desktop|![Log In](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717414499/lighthouse-login-desktop_kmgzda.png) | <mark>PASS<mark> |
| Log In Mobile|![Log In](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717414499/lighthouse-login-mobile_zeppvm.png) | <mark>PASS<mark> |
| Sign Up Desktop|![Sign Up](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717414472/lighthouse-signup-desktop_cosics.png) | <mark>PASS<mark> |
| Sign Up Mobile|![Sign Up](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717414472/lighthouse-signup-mobile_jwmzl4.png) | <mark>PASS<mark> |
| Log Out Conf Desktop|![home](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717414135/lighthouse-logout-desktop_pi0wq2.png) | <mark>PASS<mark> |
| Log Out Conf Mobile|![home](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717414135/lighthouse-logout-mobile_mmkk68.png) | <mark>PASS<mark> |
| Create Listing Desktop|![Create Listing](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717415459/lighthouse-createlisting-desktop_xqsvgh.png) | <mark>PASS<mark> |
| Create Listing Mobile|![Create Listing](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717415460/lighthouse-createlisting-mobile_ozp13w.png) | <mark>PASS<mark> |
| My Profile Desktop|![My Profile](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717415460/lighthouse-myprofile-desktop_ymxqg0.png) | <mark>PASS<mark> |
| My Profile Mobile|![My Profile](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717415462/lighthouse-myprofile-mobile_nmuzun.png) | <mark>PASS<mark> |
| My Listings Desktop|![My Listings](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717415460/lighthouse-mylisting-desktop_pjqbs4.png) | <mark>PASS<mark> |
| My Listings Mobile|![My Listings](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717415460/lighthouse-mylisting-mobile_jphfab.png) | <mark>PASS<mark> |

</details>

## Manual Testing

- Home Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Navbar|Click on logo in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on Home link in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on Listings link in Navbar|Redirect to Listings Page |Pass|Navbar present on all pages |
||Click on Create Listing link in Navbar|Redirect to Create Listing Page |Pass|Navbar present on all pages |
||Click on Profile link in Navbar|Redirect to My Profile Page |Pass|Navbar present on all pages |
||Click on Log Out link in Navbar|Redirect to Create Listing Page |Pass|Navbar present on all pages |
||Click on Login/Sign Up in Navbar|Redirect to Login Page |Pass|Navbar present on all pages |
|Hero section|Open Home page. Ensure the hero section loads as it should|Hero section loads as it should |Pass| |
|Recent Listings|Open the Home page. Scroll down to recent listings. Ensure the most recent listings are showing by comparing the time added stamp|The most recent 6 listings are displayed |Pass| |
||Open the Create Listing page and create a listing. Ensure it shows as first in the most recent listings section |The added listing is displayed as most recent |Pass| |
|Listing Card| Click on the listing card photo. Ensure it redirects to the correct single listing page |When clicked each card redirects to the correct single listing page |Pass| |
|| Click on the view details button. Ensure it redirects to the correct single listing page |When clicked each card button redirects to the correct single listing page |Pass| |
|| Go to the Create Listings page and create a new listing. Ensure the details displayed on the card are accurate |The information displayed on the card is accurate |Pass| |
|Footer|Click on all of the social links in the footer. Ensure each one opens the correct page in a new tab |All links open the correct page in a new tab |Pass| |
