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



