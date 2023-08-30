# PB MAJESTIC CLODING - PP5

## Overview

Welcome to the official repository of PB Majestic Clothing, your ultimate destination for high-quality Christian custom t-shirts that blend faith and fashion. We're thrilled to have you here and share our passion for spreading the message of Christ through stylish apparel. This is a B2C e-commerce site to sell christian brands.

### About PB Majestic Clothing

At PB Majestic Clothing, we believe that clothing is not just about fashion; it's also a powerful way to express your faith and devotion. Our brand is dedicated to creating unique and meaningful custom t-shirts that allow you to wear your beliefs proudly. Whether you're looking for eye-catching designs, inspirational quotes, or subtle symbols, our collection has something special for everyone.

## Project Goal

This is my fifth portfolio project for Code Institute, and I hope to demonstrate the abilities I've acquired by doing so. Due to my dream of establishing such an online business, I then decided to use this opportunity to build this for the future.

![Mock up](docs\images\mock.jpg)

### Click [Here](https://pb-majestic-cloding-30c8cd3db475.herokuapp.com/) to visit the deployed Site

## UX

As a graphic designer myI intended to make the website quite simple while I was developing it. When trying to convince a user to become a customer, overcomplicating the aesthetic of an online business runs the danger of creating a poor user experience.
It is a business-to-consumer e-commerce site that tends to supply customers with the best quality customised T-shirts with a lot of messages in the christian faith and also be a piece to guide a man in life because of the words in some of the designs.
On visiting the site, user's are greeted with a large image that gives a cleatr introduction of all what the site is about.
All users will be able to browse/sort Products, add to a cart, and checkout. Registered users will be able to add products to their Wishlist, view their Order history, and update/save their delivery information for quicker checkouts. Registered users will also be able to review products and like/comment on Blog posts. Staff will be able to add/edit/delete Products and add/edit/delete Blog Posts without entering admin. Any user reviews can be edited/deleted by Staff if required. When dealing with Products Staff will be able to make a Product a featured Product to be displayed on the Homepage or put a Product on sale. The graphical elements and overall design of the site provide the user with an enjoyable experience with an aesthetically pleasing display.

"Crafting Seamless Shopping Experiences: Our online shop prioritizes user-centric design, seamlessly integrating intuitive 'Add to Cart' and 'Remove' interactions that enhance product exploration. We elevate convenience by streamlining the 'Place Order' process, ensuring a frictionless journey from selection to purchase. Your personalized 'User Profile' area empowers you, putting control at your fingertips, and making every visit a delightful and efficient engagement." The User Profile gives easily access and update your profile information, keep track of your orders, and curate your wishlist for a personalized and convenient shopping journey

"Seamlessly shop a curated collection of products and explore enriching Christian blogs, all in one platform. Experience the convenience of user reviews for informed decisions, while engaging in meaningful discussions through interactive comment sections. Elevate your online journey with us, where shopping meets spirituality."

## Agile planning

This project was developed using agile methodologies by delivering small features across the duration of the project. All User Stories were assigned to Epics, prioritized under the labels, Must Have, Should Have, and Could Have. They were assigned story points according to complexity. The Fibonacci sequence is employed for the Story points. "Must Have" stories were completed first, "Should Have's" and then finally "Could Have's". It was done this way to ensure that all core requirements were completed first to give the project a complete feel. In some scenarios, certain "Should Have's" were implemented before schedule due to the nature of the implementation i.e. some Product related "Should Have's" were done during Product development with some "Must Have's" - Error templates developed later on. The Kanban board was created using Github projects user/developer stories and also a list of Acceptance criterias and Task

![Kanban Board](docs\images\kanban-board.jpg)
![Kanban Board](docs\images\user-stories-eg.jpg)

## User Stories

### EPIC 1: Initial Django Setup

- As a Developer I can set up Django and install the supporting libraries predicted to be needed so that I am ready to start development
- As a Developer I need to create the env.py and add to .gitignore so that I can securely deploy the site without exposing developer keys/information

### Epic 2: UX/UI Design

- As a Developer I can build a base template so that it can be extended to any templates that may require it.
- As a Developer I can design an aesthetically pleasing Homepage so that users have a positive experience when visiting the site.
- As a Developer I can implement message toasts so that the user/customer is alerted when they carry out and action or encounter and error.

### EPIC 3: Authorization and Authentication

- As a site user I want to be able to create an account on the site so that I can save my billing and shipping details and see a history of my purchases on my account.
- As a registered site user I want to be able to add products to a wish list so that I can keep a collection of items I am interested in buying in the future.
- As a registered user I want to be able to edit the details saved to my account so that I can keep my details up to date.

### Epic 4: Homepage/Site Navigation

- As a first-time site visitor I want to be able to clearly see what the site's purpose is so that I can decide whether or not to continue browsing it.
- As a user I want to be able to easily navigate the website so that I can find the content I'm looking for.
- As a site user I want to be able to search the website so that I can find specific products and see if the site has them in stock.
- As a site user I want to be able to contact the site owners so that I can request further information about the site or lodge a complaint.

### EPIC 5: Products Setup (CRUD)

- As a Developer I can create functional code to apply Products to my site so that the customer has Products to purchase
- As a User I would like the ability to search for a product so that to see if the site sells it
- As a User I would like to view a page containing the search results from my Product search so that so that I can find my prefered Product or see similar Products
- As a User I would like a page that displays All Products the site offers so that I can browse and find products that I may want to purchase
- As a User I would like the ability to sort products so that I can identity the best priced Products the site offers #31
- As a Developer I can allow the functionality to edit Products by staff members so that they can reduce/increase prices, change product descriptions/images etc
- As a Developer I can add functionality for staff members to delete Products so that if they do not sell or there is problems with the Product it can be removed from the storefront
- As a User I would like to view the details of any Product so that I can see if the Product has the required specifications that I need/want

### EPIC 6: Purchase / Checkout

- As a site user I want to be able to add products to my shopping basket so that I can proceed to the checkout and purchase them.
- As a site user I want to be able to see a running total of the items in my basket so that I can manage my spending and know what to expect at the checkout.
- As a site user I want to be able to checkout with a card payment so that I can place an order for the items in my basket.
- As a site user I want to be able to receive an order confirmation email after I purchase from the shop so that I can have a record of what I've purchased in my email inbox.
- As a site user I want to be able to apply discount codes in the checkout so that I can receive a discount on my purchase.

### EPIC 7: Stripe Setup - Purchase / Checkout

As a Developer I can implement Stripe so that it can manage payments for the site products at checkout #46

### EPIC 8: User Profile (CRUD)

- As a customer I would like the ability to create my own Profile page so that I can save my shipping address for future purchases and track my orders
- As a Developer I can implement functionality to allow a customer to save information to a personal Profile so that they can save information i.e. shipping address/orders for future review
- As a customer I would like to add wishlish items to show in my profile so that I can get easy access to view and purchase them.

# EPIC 9: Blog

- As a site user I want to be able to view blog posts on the website so that I can read any posts I feel are relevant to me.
- As a site user I want to be able to add, edit and delete comments on blog so that I can share my view on the blog post.
- As a site admin I want to be able to create blog posts from the front end so that I can share information with site visitors.
- As a site admin I want to be able to edit existing blog posts so that I can ensure that posts are up to date and relevant without having to create them from scratch in case of error.
  As a site admin I want to be able to delete existing blog posts so that I can remove any unwanted posts from the site.

### EPIC 10: Review Products (CRUD)

- As a Customer I would like to leave a review on a Product so that my fellow shoppers can benefit from my feedback and make informed purchasing decisions.
- As a Developer I can build a page to display the Review form so that customer has the ability to write their review and submit it.

### EPIC 11: Contact Us #15

- As a Developer I can add functionality to allow the customer to contact the site owner so that any issue they encounter can be logged and resolved
- As a user/customer I should be able to contact the site owner so that I have a comminucation if any issue arises

### EPIC 12: SEO & Web Marketing #13

- As a Developer I can create a Facebook business page for my site so that I can market my website on the social platform #60
- As a Developer I can implement a newsletter on my site so that customers can subscribe for future updates and deals which should bring them back to the site for future purchases.
- As a Developer I can add helpful description and keywords so that my site can reach a wider audience

### EPIC 13: Error Notification

- As a Developer I can implement a 403 error page to redirect unauthorised users so that I can secure my views.
- As a Developer I can implement a 404 error page so that I can alert users when they have accessed a page that doesn't exist.
- As a Developer I can implement a 500 error page so that I can alert users when an internal server error occurs.

### EPIC 14:

As a User, I must be able to be notified with messages, so that I would know if my request is successful.

### EPIC 15: Documentation

- Create/Write README.md
- Create/Write TESTING.md

## Wireframe

To help with the design of the site, I created wireframes for each page. To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes. I've used Balsamiq to design my site wireframes.

### Desktop

<details close>
<summary>Click to view</summary>
<br>

</details>

### Tablet

<details close>
<summary>Click to view</summary>
<br>

</details>

### Mobile

<details close>
<summary>Click to view</summary>
<br>

</details>

## The Scope Plane

- Responsive Design - The site should be fully functional on all devices from 320px up
  Hamburger menu for mobile devices
- Ability to perform CRUD functionality on Products, Profiles, Reviews, Blog Posts, and Comments
- Restricted features for registered users such as Product reviewing, adding Products to Wishlist, editing Profiles, and Commenting/Liking Blog posts.
- Newsletter Subscribing
