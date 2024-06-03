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

- Listings Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|listing card|||Pass|Tested on home page|
|Footer|Click on all of the social links in the footer. Ensure each one opens the correct page in a new tab |All links open the correct page in a new tab |Pass| |

- Single Listing Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
| Back button|Open the single listing page. Click on the back button. Ensure it sends you back to the previous page|When clicked the button brings you back to the previous page.|Pass||
|Listing details|Ensure all the dogs details are accurate with the details used when creating the listing. Ensure all icons display as they should|All icons display as they should, and the information is accurate.|Pass||
|Description|Scroll to the description section. Ensure the accurate description is displayed |The accurate description is displayed|Pass||

- Create listing Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
||Click on each drop down field to ensure correct options are displayed|Correct options are displayed|Pass||

- Edit listing Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Form|||Pass|Tested at create listing|
||Open edit listing page. Ensure the form is populated with the correct listing's details|The form is populated with the correct listing's details|Pass||

- My Profile Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|My Profile|Open my profile page. Ensure the image is displaying correctly.|The image is displaying correctly.|Pass||
|Edit profile button|Click on the edit profile button. Ensure it redirects to the edit profile page.|The edit profile button redirects to the edit profile page.|Pass||
|Delete profile button|Click on the delete profile button. Ensure it redirects to the delete profile page.|The delete profile button redirects to the delete profile page.|Pass||
||Click on my listings link on the sidebar nav. Ensure it redirects to my listings page| Redirects to my listings page|Pass||

- My Listings Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|My Listings|When on the my listings page ensure the listings displayed were created by the authenticated user.|The listings displayed were created by the authenticated user. |Pass||
||Click on the edit button. Ensure it redirects to the edit listing page.|The button redirects to the edit listing page. |Pass||
||Click on the delete button. Ensure it redirects to the delete listing page.|The button redirects to the delete listing page. |Pass||
||Click on the view button. Ensure it redirects to the single listing page.|The button redirects to the single listing page. |Pass||

- Delete Listing Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Go back button|Click on the go back button. Ensure it sends back to previous page |When clicked the button brings back to previous page.|Pass||
|Delete Listing|Click on the delete listing button. Ensure it deletes the listing and the user is redirected to the my listings page. |The user is redirected to the my listings page. By checking in the admin pannel can be confirmed the was deleted|Pass||

- Log In page

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Form|Fill all fields with correct data in the expected format. Click Log In. Ensure Flash message appears and the user is redirected to the home page. To ensure the user is logged in: Open developer tools and navigate to application. On the side select cookies and check for sessionid being added. |When submitted success flash message is presented, the user is redirected to the home page. |Pass||
| | Fill in the form with incorrect details. Ensure the user is not logged in and flash message appears| Flash message appears in warning letting the user know they have entered incorrect details. The user is not signed in| Pass| |
| | Click on the forgot password link. ensure it redirects to the reset password page.| The user is redirected to the reset password page| Pass| |
| | Click on the register here link. ensure it redirects to sign up page.| The user is redirected to the sign up page| Pass| |

- Sign Up Page

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Form|Fill all fields with correct data in the expected format. Click Sign Up. Ensure Flash message appears and the user is redirected to the my profile page.|When submitted success flash message is presented, the user is redirected to the my profile page.|Pass||
||Fill all fields with correct data but one. Click Sign Up. Ensure the form does not submit and appropriate message is displayed. Repeat for all fields. |Form did not submit, appropriate message was displayed|Pass||
| | Click on the Already have an account? Log In link. ensure it redirects to the login page.| The user is redirected to the login page| Pass| |


- Sign Out confirmation

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Go back button|Click on the go back button. Ensure it sends back to previous page |When clicked the button brings back to previous page.|Pass||
|Log out button|Click on the Log out button.To ensure the user is logged out: Open developer tools and navigate to application. On the side select cookies and check for sessionid being removed.The user should be redirected to the the home page. Ensure flash message is displayed |The user is redirected to the home page. Flash message is displayed. Sessionid is removed from cookies.|Pass||

## User Story Testing

|User Story|Screenshot|Result|
| --- | --- | --- |
| As a developer I can set up a new Django project so that I can create the project's structure | The project was set up successfully| <mark>PASS<mark>  |
| As a developer I can connect database and media storage so that the user's stored data is stored successfully | Database and media storage were connected successfully| <mark>PASS<mark> |
| As a developer I can deploy the application early so that I can confirm that the initial setup is working and can continue testing the application during development | The application was deployed after the initial set up to confirm everything is working as expected| <mark>PASS<mark> |
| As a developer I can create wireframes so that the layout of the website is clear for desktop and mobile | wireframes were created and are included in the relevant section of the [README](./README.md)| <mark>PASS<mark> |
| As a user I want to be able to register an account so that I can have access to all functionality of Petlover. | ![Sign up](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717259980/sign-up_eqiofx.png)| <mark>PASS<mark> |
| As a registered user I want to be able to log in to my account so I can view my profile page and my listings. | ![Log In](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717259980/log-in_ydtyfo.png)| <mark>PASS<mark> |
| As a registered user I want to be able to see my profile page so that I can update my information | ![My Profile](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717230458/my-profile_ic18io.png)| <mark>PASS<mark> |
| As a registered user I want to be able to delete my profile and all my listings if I do not wish to use the services of Petlover. | ![Delete Profile](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717260510/delete-profile_lmz8tj.png)| <mark>PASS<mark> |
| As a user, I want to be able to see the most recent listings on the landing page so that I can quickly and easily discover the latest items available for sale | ![Recent Listings](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717225317/recent-listings_povy8e.png)| <mark>PASS<mark> |
| As a user I want to be able to see details about the listing such as a description, image, and seller’s details so that I can find suitable dogs and make informed decisions before I contact the seller | ![Single Listing](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717259554/single-listing_pctxzi.png)| <mark>PASS<mark> |
| As a registered user I want to be able to create a listing so that I can advertise dogs for sale. | ![Create Listing](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717230200/create-listings_rxklqv.png)| <mark>PASS<mark> |
| As a registered user I want to be able to edit a listing so that I can correct any mistakes or adjust the listed price | ![Edit Listing](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717258435/edit-listing_sv9zmh.png)| <mark>PASS<mark> |
| As a registered user I want to be able to delete a listing so that it is not available for other users to view. | ![Delete Listing](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717258733/delete-listing_ovd9rr.png)| <mark>PASS<mark> |
| As a registered user I want to be able to see all of the listings I have created so that I can manage and keep track of the dogs I have listed for sale. | ![My Listings](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717230674/my-listings_eb1l2q.png)| <mark>PASS<mark> |
| As a site owner I want to ensure that the user is prompted with a notification message when performing CRUD operations or login/logout, and signup so that the user is informed about the outcome of the action taken | ![Flash messages](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717419062/flash-messages_z5sc1y.png)| <mark>PASS<mark> |
