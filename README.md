# PetLover

# Introduction

Petlover aims to facilitate connections between individuals interested in buying or selling dogs. The platform enables users to register accounts and effortlessly create advertisements for dogs available for purchase.

Welcome to the [PetLover](https://petlover-6900a2845617.herokuapp.com/). The project is built using Django framework for the backend and HTML, CSS, Bootstrap and JavaScript on the frontend. Petlover allows the users to create an account and perform CRUD functionality on their profile and listings. This project was created as part of Code Institute full-stack developer course.

[You can see the live project here](https://petlover-6900a2845617.herokuapp.com/)

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1711016918/mock-up_rfmhf4.png)

## [Table of Contents](#table-of-contents)

- [User Experience](#user-experience)
  - [Website goal](#website-goal)
  - [Scope](#scope)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Color Scheme](#color-scheme)
  - [Database Schema](#database-schema)
  - [Fonts](#fonts)
  - [Wireframes](#wireframes)
  - [Agile Methodology](#agile-methodology)
    - [Overview](#overview)
    - [EPICS(Milestones)](#epics(milestones))
    - [User Stories issues](#user-stories-issues)
    - [MoSCoW prioritization](#moscow-prioritization)
    - [GitHub Projects](#github-projects)

- [Features](#features)
    - [Navbar](#navbar)
    - [Footer](#footer)
    - [Home](#home)
        - [Hero Section](#hero-section)
        - [Recent Listings](#recent-listings)
        - [Listing Card](#listing-card)
    - [Listings Page](#listings-page)
    - [Create Listing](#create-listing)
    - [Profile Page](#profile-page)
    - [My Listings](#my-listings)
    - [Edit Listing](#edit-listing)
    - [Delete Listing](#delete-listing)
    - [View Listing](#view-listing)
    - [Log In Page](#log-in-page)
    - [Sign Up Page](#sign-up-page)
    - [Sign Out Confirmation](#sign-out-confirmation)
    - [Edit Profile](#edit-profile)
    - [Delete Profile Confirmation](#delete-profile-confirmation)

- [Future Features](#future-features)
- [Testing](#testing)
- [Technologies And Languages](#technologies-and-languages)
    - [Languages Used](#languages-used)
    - [Python Modules](#python-modules)
    - [Technologies and programs](#technologies-and-programs)
- [Credits](#credits)
  - [Code](#code)
  - [content](#content) 
  - [Mockup](#mockup)
  - [Images](#images-1)

## User Experience

### Website goal

- To provide the users with a place to advertise their dogs.
- To provide a range of available dogs for sale to potential buyers.
- To provide a place for the users to browse dogs and find out the dogs's price range and othe details.
- To make the website available and functional on every device.

### Scope

The project aims to develop an online dog listing platform called "Petlover" that facilitates users in listing, viewing, and managing dogs listings. The platform will be responsive and user-friendly, providing features for user registration, listing creation, profile management.

Key Features:

1. Initial Project Setup:

- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval.
- An early deployment of the application will be carried out to confirm the initial setup's functionality.

2. Responsive Design: -The website will be responsive, allowing users to access it on both desktop and mobile devices.

3. User Authentication:

- Users can register an account, providing access to all functionality of Petlover.
- Registered users can log in to view their profile, listings.

4. Profile Management:

- Registered users can view and edit their profiles, including personal details and profile pictures.
- Users can delete their profiles and associated listings.

5. Listing Management:
- Users can perform CRUD on their listings with dogs for sale.
- The most recent listings will be displayed on the landing page.
- Listings will include details, descriptions, images, and seller's information.

6. Notification Messages:

- Users will receive notification messages when performing CRUD operations, login/logout, and signup actions.

### User Stories

1. As a developer I can set up a new Django project so that I can create the project's structure
2. As a developer I can connect database and media storage so that the user's stored data is stored successfully
3. As a developer I can deploy the application early so that I can confirm that the initial setup is working and can continue testing the application during development
4. As a developer I can create wireframes so that the layout of the website is clear for desktop and mobile
5. As a user I want the website to be responsive so I can view it on my mobile
6. As a user I want to be able to register an account so that I can have access to all functionality of Petlover.
7. As a registered user I want to be able to log in to my account so I can view my profile page, my listings.
8. As a registered user I want to be able to see my profile page so that I can update my information
9. As a user I want to be able to view other user’s profiles so that I can get more information about the seller/buyer like location and phone number
10. As a registered user I want to be able to delete my profile and all my listings if I do not wish to use the services of Petlover.
11. As a user I want to be able to see details about the listing such as a description, image, and seller’s details so that I can find suitable dogs options and make informed decisions before I contact the seller
12. As a registered user I want to be able to create a listing so that I can advertise my dogs for sale.
13. As a registered user I want to be able to edit a listing so that I can correct any mistakes or adjust the listed price
14. As a registered user I want to be able to delete a listing so that it is not available for other users to view.
15. As a registered user I want to be able to see all of the listings I have created so that I can manage and keep track of the dogs I have listed for sale.
16. As a site owner I want to ensure that the user is prompted with a notification message when performing CRUD operations or login/logout, and signup so that the user is informed about the outcome of the action taken
17. As a User I can navigate through the website so that I can access different sections efficiently
18. As a non-authenticated user, I want to access the user profile pages of listing owners, so that I can view their contact details and listings.

[Back to Table of contents](#table-of-contents)

## Design

### Colour Scheme
In this website mainly used grey back ground. For login,sign up forms and buttons used light blue colors. For  container used white color, inside this container added picture.

The below colours are the main colours.
-  body background-color - rgb(154, 179, 209)
-  nav-bar hover - yellow
-  nav bar, button, card header - #007bff
-  button hover -  #0056b3
-  footer -  #f8f9fa
-  button back ground -   #4CAF50
-  button color- white

### Database Schema

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717021191/dbdaigram_oqfvlj.png)

1. User:  The User model is connected to the UserProfile model with one to one relationship.

2. UserProfile: The UserProfile model is a created model to handle the user profile details. 

3. Dog: This model was created to store all of the dog details in the database

4. Listing: The listing model is connected to the Profile with the ForeignKey field - owner and dog. 

### Fonts

In addition to Bootstrap 4 built in font family the below two fonts were used throughout the application

- Poppins
- Indie Flower

### Wireframes

- Home
<details>
  <summary>Home</summary> 
    <img src="https://res.cloudinary.com/dmhdrvehj/image/upload/v1717107163/wireframe-home_axuuoi.png">   
</details>

- Listings
<details>
  <summary>Listings</summary> 
  <img src ="https://res.cloudinary.com/dmhdrvehj/image/upload/v1717107163/wireframe-listings_il26gc.png">
</details>

- Single Listing
<details>
  <summary>Single Listing</summary> 
  <img src ="https://res.cloudinary.com/dmhdrvehj/image/upload/v1717107163/wireframe-Single-listings_j3c5ph.png">
</details>

- My Listings
<details>
  <summary>My Listing</summary> 
  <img src ="https://res.cloudinary.com/dmhdrvehj/image/upload/v1717107163/wireframe-my-listings_watjbl.png">
</details>

- My Profile
<details>
  <summary>My Profile</summary> 
  <img src ="https://res.cloudinary.com/dmhdrvehj/image/upload/v1717107163/wireframe-my-profile_fxudsa.png">
</details>

### Agile Methodology

#### Overview

This project was created using agile principles. As this is my first full-stack project, using agile, it was easier to identify the relevant milestones. Using the agile approach allowed me to plan all the features of the website through user stories. Each user story has acceptance criteria and tasks to clearly outline the requirements for each feature to be completed.

#### Epics(Milestones)

The user stories are grouped into six EPICS or Milestones. 

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717108208/Epics_wctcpx.png)

#### User Stories Issues

The structure of the user story issue consists of the user story, acceptance criteria, and tasks that outline the steps that are required for this issue to be completed. During development where possible, the commit messages are connected to their corresponding issues.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717108208/user-stories_zy1gej.png)

#### MoSCoW prioritization

This prioritization technique was used to effectively prioritize the features and requirements of the project based on their importance. The acronym "MoSCoW" stands for "Must have, Should have, Could have, and Won't have." Each category helps categorize and prioritize features to guide the development process and ensure that the most critical elements are addressed first.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717108208/moscow_wv1qfb.png)

#### GitHub Projects

The project was created using a basic Kanban Board structure, divided into columns such as Todo, In Progress, Done, and Backlog. This setup provides a clear and organized way to track the status of tasks and visualize and manage the workflow.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717108600/kamban-board_zprqvc.png)

## Features

### Navbar

The navbar was built using bootstrap 5 and it is fully responsive. When the user clicks login/signup the log in form will come and if user has no account they sign up using register here form. If the user is authenticated additional menu options are displayed like my profile and create listing.  The my profile links shows registered user profile and thier listings also

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717224504/navbar2_pkzvrp.png)

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717224503/navbar_xn4nwe.png)

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717224504/navbar1_kzndea.png)

### Footer

The footer consist of links to social media links and address.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717225012/footer_n7r2e8.png)

### Home

#### Hero Section

The hero section is the beginning of the whole customer's journey. That is why I made it a priority to create appealing hero section. 

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717225012/Hero-section_phnzjq.png)

#### Recent Listings

The products displayed on the home page are the most recently added 6 Listings.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717225317/recent-listings_povy8e.png)

#### Listing Card

The listing card is designed to present to the user the most important information about the listing. The card consists of a breed, location, time ago posted, DOB, temperament, price and a button for view details. The card and the button are links to the single listing page.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717228332/listing-card_xyuwkn.png)

[Back to Table of contents](#table-of-contents)

### Listings Page

The listings page consists all the listings starting from the most recent ones.  

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717228046/listings_gkggn4.png)

### Create Listing

This page can be accessed only by authenticated users. It provides the user with a listing creation form.  The model field is then populated with the appropriate options based on the dog breed, sex and temperament selection. Price selection is from 100 to 1000 for range of 50. This helps to prevent users from creating listings with wrong details. All fields are required. 

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717230200/create-listings_rxklqv.png)

### Profile Page

This page can be accessed only by authenticated users. It consists of a sidebar menu with links for Profile and My Listings. The profile page is essentially a large card that includes the user's profile image and details like name, user name, email, and phone. Underneath, there are two buttons one for edit profile and one for delete profile.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717230458/my-profile_ic18io.png)

### My listings

This page shows all of the listings that were created by this user. The cards have additional buttons for viewing,editing and deleting listings which allows each user to easily manage their listings. And there is a back  button to go back to my profile. 

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717230674/my-listings_eb1l2q.png)

### Edit Listing

This page displays the same form as create a listing, with already populated fields with the current details of the listing. The user can amend all of the details on the page and upload new images or just save the form as it is. Once submitted the user is redirected to my listings page.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717258435/edit-listing_sv9zmh.png)

### Delete Listing

When the user visits my listings page they can delete listings using the delete button on each card, which redirects the user to confirmation page. The page consists of a warning message and two buttons - one to go back and one to delete listing, which is in red colour to clearly indicate danger. Once the user confirms, the listing is deleted. The user is then redirected to my listings page.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717258733/delete-listing_ovd9rr.png)

### View Listing

This button leads to the single listing page. On the top left, there is a button to go back. In this page left side displays the picture, middle displays dogs details and right side displays contact details of this listing.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717259554/single-listing_pctxzi.png)

### Log In page

Consist of a form with username and password.A log in button which submits the form. The register link is position below that.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717259980/log-in_ydtyfo.png)

### Sign Up page

Consists of a form with name, email, username, password, and password confirmation. Below it has a link to log in if the user already has an account. Below that is the signup button. 

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717259980/sign-up_eqiofx.png)

### Sign out confirmation

When the user clicks on the log out link in the nav, they are redirected to the confirmation page. This page consist of warning message and two buttons- one to go back to home and one to log out.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717260187/Signout-confirmation_etwkq8.png)

### Edit Profile

The edit profie page renders a form with prefilled fields with the existing information for this user. It consists of profie image, name, username, email, phone. Below their is save button and back button. which will update the profile details once submitted.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717260510/edit-profile_odbbpz.png)

### Delete Profile Confirmation

This page consists of warning message with two buttons - one to go back and one to delete the profile. Delete profile is in red to indicate danger. Once clicked the profile is deleted and is redirected to home page

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1717260510/delete-profile_lmz8tj.png)

[Back to Table of contents](#table-of-contents)

## Future Features

1. I want to add pagination to the listings and my listing page.

2. Add favourites if some one likes the listings.

3. Password reset

## Testing

Testing documentation can be found [here](TESTING.md).

## Technologies And Languages

### Languages Used

  - HTML
  - CSS
  - JavaScript
  - Bootstrap
  - Python
  - Django

### Python Modules

  - dj-database-url - This library is used to parse the database URL specified in the DATABASE_URL environment variable, which is commonly used for configuring database connections in Django projects.

  - django-storages - Django Storages is a collection of custom storage backends for Django, including support for storing files on remote services like Cloudinary.

  - gunicorn - Gunicorn is a popular WSGI (Web Server Gateway Interface) HTTP server for running Python web applications, including Django applications, in a production environment.

  - Pillow - Pillow is a Python Imaging Library (PIL) fork that provides tools for working with images in various formats.

  - psycopg2 - Psycopg2 is a PostgreSQL adapter for Python. It allows Django to connect to PostgreSQL databases.

### Technologies and programs

  - Favicon Generator was used to generate Favicon
  - GitHub is the hosting site used to store the code for the website.
  - Git was used as a version control software to commit and push the code to the GitHub repository.
  - Heroku - used for deploying the project
  - Font Awesome - for creating atractive UX with icons
  - Bootstrap5 - for adding predifined styled elements and creating responsiveness
  - LightHouse - for testing performance
  - Photoshop was used for creating the mockup images of the website during planning stage.
  - Google Fonts was used to import fonts.
  - Google Chrome Lighthouse was used during the testing of the website.
  - Google Chrome Developer Tools was used during testing, debugging and making the website responsive.
  - Cloudinary was used to store media files.  
  - W3C HTML Validator was used to check for errors in the HTML code.
  - W3C CSS Validator was used to check for errors in the CSS code
  - Js Hint was used to validate the JavaScript code.
  - CI Python Linter was used to validate the Python code.

## Credits

To complete this project I used Code institue student template: [Gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template)
 
- Ideas and knowledge library:
  
-  [AutoMarket](https://github.com/Dayana-N/AutoMarket-PP4)

- [stackoverflow.com](https://stackoverflow.com/)

### Code

- [Template Inheritance in Django](https://www.youtube.com/watch?v=gw-hKVt71A8)
- [Image Upload to Cloudinary From Django](https://www.youtube.com/watch?v=i0ar7W98Osc)
- [Host uploaded images from Django with Cloudinary](https://www.youtube.com/watch?v=fQo9ivqX4xs)

### content

- [AutoMarket](https://github.com/Dayana-N/AutoMarket-PP4)

### Mockup

- [Mockup screenshot generator](https://ui.dev/amiresponsive)

### Images

- www.freepik.com



