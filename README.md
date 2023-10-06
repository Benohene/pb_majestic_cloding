# PB MAJESTIC CLODING - PP5

# Table of content

- [ABOUT SITE](#about-pb-majestic-clothing)

- [PROJECT GOAL](#project-goal)

- [UX EXPERIENCE](#ux)

- [AGILE PLANNING](#agile-planning)

- [USER STORIES](#user-stories)

- [WIREFRAMES](#wireframe)

- [DATABASE](#database-design)

- [FEATURES](#features)

- [TOOLS & TECHNLOGIES](#tools--technologies-used)

- [MARKETING](#marketing-strategy)

- [TESTING](#testing)

- [DEPLOYMENT](#deployment)

- [CREDIT](#credits)

- [ACKNOWLEDGEMENT](#acknowledgements)

## Overview

Welcome to the official repository of PB Majestic Clothing, your ultimate destination for high-quality Christian custom t-shirts that blend faith and fashion. We're thrilled to have you here and share our passion for spreading the message of Christ through stylish apparel. This is a B2C e-commerce site to sell christian brands.

### About PB Majestic Clothing

At PB Majestic Clothing, we believe that clothing is not just about fashion; it's also a powerful way to express your faith and devotion. Our brand is dedicated to creating unique and meaningful custom t-shirts that allow you to wear your beliefs proudly. Whether you're looking for eye-catching designs, inspirational quotes, or subtle symbols, our collection has something special for everyone.

## Project Goal

This is my fifth portfolio project for Code Institute, and I hope to demonstrate the abilities I've acquired by doing so. Due to my dream of establishing such an online business, I then decided to use this opportunity to build this for the future.

![Mock up](docs/images/mock.jpg)

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

![Kanban Board](docs/images/kanban-board.jpg)
![Kanban Board](docs/images/user-stories-eg.jpg)

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

### EPIC 9: Blog

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

### Sketches

<details close>
<summary>Click to view</summary>

![Home](docs/images/home.jpg)

![All-product](docs/images/all-prod.jpg)

![product](docs/images/prod-view.jpg)

![cart](docs/images/cart.jpg)

![checkout](docs/images/checkout.jpg)

![complete order](docs/images/order-complete.jpg)

![contact](docs/images/contact.jpg)

![blog](docs/images/blog-list.jpg)

![blog-view](docs/images/blog-view.jpg)

![sign up](docs/images/sign-up.jpg)

![sign in](docs/images/sign-in.jpg)

![sign out](docs/images/sign-out.jpg)

</details>

## The Scope Plane

- Responsive Design - The site should be fully functional on all devices from 320px up
  Hamburger menu for mobile devices
- Ability to perform CRUD functionality on Products, Profiles, Reviews, Blog Posts, and Comments
- Restricted features for registered users such as Product reviewing, adding Products to Wishlist, editing Profiles, and Commenting/Liking Blog posts.
- Newsletter Subscribing

# Database Design

I created an entity relationship diagram using [sqldbm](https://app.sqldbm.com/CreateNew/). This helped me to visualize the relationships between my data structures and made the development process easier as I had everything mapped out in front of me for reference to avoid having to reference each models.py file individually.

![diagram](docs/features_images/sqldbm.jpg)

## Features

### Home Page
The Homepage is the landing page o fthe site which welcomes the user with an overview of the website. It consist of the Navbar, Shop now button and Footer

![features](docs/features_images/home.jpg)

### Navbar with Search field and nav links
The Navbar consist of the search field and menu that navigates to the entire pages on the website. It also has the Logo of the website.

![features](docs/features_images/navbar.jpg)

### Footer with Newletter
The Footer consist of the some details of the websites and some links including the facebook link of the website. 

![features](docs/features_images/footer.jpg)

### All Products
The All Product page display all products with sort field that allows uses to sort products according specific preferences like price, rating, names and others

![features](docs/features_images/all-product.jpg)

### All Products Details
The Product Detail pages gives description to the product and also allows user to Add product to cart by selecting the size and quantity.

![features](docs/features_images/prod-view.jpg)

## Product reviews

![features](docs/features_images/review.jpg)

- No review on product page
  ![features](docs/features_images/no-review.jpg)

- Add product review forms
  ![features](docs/features_images/add-review.jpg)

- Edit product review forms
  ![features](docs/features_images/edit-review.jpg)

- Delete product review forms
  ![features](docs/features_images/delete-review.jpg)

### Product Management

- Add Products
  ![features](docs/features_images/prod-manage.jpg)

- Edit Products
  ![features](docs/features_images/prod-edit.jpg)

- Edit Products
  ![features](docs/features_images/prod-edit.jpg)

### Cart

![features](docs/features_images/cart-view.jpg)

### Checkout

![features](docs/features_images/checkout.jpg)

### Order Completion

![features](docs/features_images/thankyou-page.jpg)

### User Profile

- Detail Profile
  ![features](docs/features_images/profile-info.jpg)

- Orders on Profile
  ![features](docs/features_images/profile-order.jpg)

- Wishlist on Profile
  ![features](docs/features_images/profile-wish.jpg)

### Blog

- Blog view
  ![features](docs/features_images/blog-list.jpg)

- Blog Add
  ![features](docs/features_images/add-blog.jpg)

- Blog Edit
  ![features](docs/features_images/blog-update.jpg)

- Blog Delete
  ![features](docs/features_images/blog-delete.jpg)

- Blog comment
  ![features](docs/features_images/blog-commented.jpg)

- Blog edit comment
  ![features](docs/features_images/edit-blog-comment.jpg)

- Blog delete
  ![features](docs/features_images/blog-delete.jpg)

### Contact Us

![features](docs/features_images/contact-page.jpg)

### Status Error Templates

As a Developer I can implement a 403 error page to redirect unauthorised users so that I can secure my views

As a Developer I can implement a 404 error page so that I can alert users when they have accessed a page that doesn't exist

As a Developer I can implement a 500 error page so that I can alert users when an internal server error occurs

A 403 error page has been implemented to provide feedback to the user when they try to access unauthorized content. Users will be directed to this page if they alter the URLs and attempt to edit, delete, or access pages that are restricted.

A 404 page has been implemented and will display if a user navigates to a broken link.
The 404 page will allow the user to easily navigate back to the main website if they direct to a broken link / missing page, without the need for the browser's back button.
![features](docs/features_images/error-404.jpg)

A 500 error page has been displayed to alert users when an internal server error occurs. The message relays to users that the problem is on our end, not theirs.

![features](docs/features_images/error-500.jpg)

### User Sign Up

Users without an account can register for one through the register link in the main nav menu. This will present them with a form to add their details and created a profile for that user on completion.
Users are sent a confirmation email to complete their account sign up to help avoid people from creating spam accounts on the site.
![features](docs/features_images/sign-up.jpg)

### User Sign In

If a user isn't signed in to the site but has a profile, they can follow the sign in link where they're presented with a log in page. They must input their username or email address and correct password to do so. There's also a checkbox to let the user be remembered on their current device to avoid having to log in every time they visit the site.
There's a link for users who have forgotten their password.
![features](docs/features_images/sign-in.jpg)

### User Sign Out

If a user wants to end their logged in session, they can click logout under the account dropdown in the nav menu.
This will bring them to a page confirming they want to log out.
![features](docs/features_images/sign-out.jpg)

### Password Reset

If a user is trying to log in and has forgotten their password they can visit the password reset page. Here a user must enter their email address they used to sign up with and an email will be sent to them with further instructions on resetting their password to regain access to their account.
![features](docs/features_images/pass-reset.jpg)

## Tools & Technologies Used

This site needed a lot of tools and technologies to make it possible. Therefore the following were used for production.

- HTML used for the main site structure content.
- CSS used for the main site styling, designing and layout.
- CSS :root variables used for reusable styles throughout the site especially the colors.
- CSS Flexbox used for an enhanced responsive layout.
- JavaScript used for user interaction on the site.
- Python used as the back-end programming language.
- Git used for version control. (git add, git commit, git push)
- GitHub used for secure online code storage.
- Gitpod used as a cloud-based IDE for development.
- Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.
- Django used as the Python framework for the site.
- PostgreSQL used as the relational database management.
- ElephantSQL used as the Postgres database.
- Heroku used for hosting the deployed back-end site.
- Stripe used for online secure payments of ecommerce products/services.
- AWS S3 used for online static file storage.
- Django Summernote used for the body field for blog posts.
- Pillow used for handling images.

## Marketing Strategy

### Social Media Marketing
I've established a Facebook Business page and integrated it with the website, aiming to boost sales and foster a community through a robust social media campaign. The Facebook page now features links to the website and a post that highlights details about the site and its free delivery threshold.
![features](docs/features_images/facebook-page.jpg)

## Newsletter Marketing

I employed Mailchimp to establish a website-embedded newsletter sign-up form, enabling users to share their email addresses for deeper insights into the site and to encourage repeat engagement. An automated Welcome email series was configured to promptly acknowledge new subscribers with a message from Mailchimp. Additionally, I've set up a Newsletter campaign that will be manually triggered by the site owner, ensuring every subscriber receives the latest updates. The overarching goal is to cultivate a community that has the potential to attract returning and new customers, thereby fostering business growth.

![features](docs/features_images/newsletter.jpg)

## Search Engine Optimization (SEO)

### Keywords
I used Wordtracker to discover keywords for my website that possess a favorable combination of high search volume and low competition, making use of the KEI (Keyword Effectiveness Index) metric on Wordtracker to guide my keyword selection.

![features](docs/features_images/seo.jpg)

# Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.


# Deployment

The site has been deployed on Heroku. It indicates that the website or web application has been successfully hosted and made accessible to the public using the Heroku platform. Heroku is a cloud platform that allows developers to deploy, manage, and scale web applications with ease. Deploying a site on Heroku often involves uploading code and configuring the necessary settings to run the web application on Heroku's infrastructure. This statement suggests that the deployment process on Heroku has been completed successfully.

## ElephantSQL Database

This project employs ElephantSQL as the backend database using PostgreSQL. To set up your own PostgreSQL database, follow these steps:

1. Sign up with your GitHub account.
2. Click on "Create New Instance" to initiate the creation of a new database.
3. Specify a name for your database, typically the project name like "pb-majestic-cloding."
4. Choose the "Tiny Turtle (Free)" plan.
5. You can leave the Tags field empty.
6. Select the Region and Data Center that is geographically closest to your location.
7. Once the database is successfully created, click on its name to access the database URL and password information.

### Amazon AWS

This project utilizes AWS for the storage of online media and static files because Heroku lacks the ability to retain such data.

After setting up an AWS account and signing in, proceed with the following sequence of actions to establish the connection for your project. Ensure that you are currently on the AWS Management Console page.

### S3 Bucket

- Begin by initiating a search for S3.

- Proceed to create a new bucket and assign it a name that matches your Heroku app's name, selecting the region that is geographically closest to your location.

- Ensure that the "Block all public access" option is unchecked and acknowledge that the bucket must be made public for it to function correctly on Heroku.

- In the Object Ownership section, confirm that ACLs are enabled, and opt for "Bucket owner preferred."

- Within the Properties tab, activate static website hosting and specify "index.html" and "error.html" in their respective fields, then save your changes.

- In the Permissions tab, paste the provided CORS configuration.
	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

- Copy your ARN string.

- In the Bucket Policy tab, select the Policy Generator link and follow these steps:

  - Policy Type: S3 Bucket Policy
  - Effect: Allow
  - Principal: \*
  - Actions: GetObject
  - Amazon Resource Name (ARN): Paste your ARN here
  - Add Statement
  - Generate Policy

- Copy the entire policy generated and insert it into the Bucket Policy Editor.
```
{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
```

- Before clicking "Save," append /\* to the end of the Resource key in the Bucket Policy Editor, as mentioned previously.

- Save your changes.

- In the Access Control List (ACL) section, click "Edit" and enable "List for Everyone" (public access), accepting any associated warnings.

- If the "Edit" button is inactive, adjust the Object Ownership section as mentioned earlier to enable ACLs.

## IAM

Navigate back to the AWS Services Menu and locate IAM (Identity and Access Management). Once you are on the IAM page, follow these steps:

1. Within User Groups, select the option to Create a New Group.
2. Suggested Name: Create a name that combines "group" with the project's name, like "group-pb-majestic-cloding."
3. Tags are not mandatory, but you should select it to proceed to the policy review page.
4. In the User Groups section, choose your newly created group, and go to the Permissions tab.
5. Access the Add Permissions dropdown and choose Attach Policies.
6. Pick the desired policy, and then click Add Permissions at the bottom once you're finished.
7. On the JSON tab, choose the Import Managed Policy link.
8. Search for S3, select the AmazonS3FullAccess policy, and then Import.
9. You'll need to copy the ARN from the S3 Bucket and paste it into the "Resources" field in the Policy.
10. Finally, click on Review Policy.

Suggested Name for the policy: Consider naming it by combining "policy" with the project's name, like "policy-pb-majestic-cloding."

Provide a description for the policy: "This policy grants access to the S3 Bucket for pb-majestic-cloding static files." Click on Create Policy.

11. In the User Groups section, click on your "group-pb-majestic-cloding."
12. Choose Attach Policy.
13. Search for the policy you just created ("policy-pb-majestic-cloding"), select it, and then click Attach Policy.
14. In the User Groups section, click on Add User.
15. Suggested Name: Suggest a name by combining "user" with the project's name, like "user-pb-majestic-cloding."
16. For the "Select AWS Access Type," choose Programmatic Access.
17. Select the group to add your new user to, which should be "group-pb-majestic-cloding."
18. Tags are not mandatory, but you should select it to proceed to the user review page.
19. Click Create User when you're finished.
20. You should see a button to Download a .csv file; click it to save a copy on your system.
21. It's important to note that once you leave this page, you won't be able to return to download it again, so be sure to do it immediately.
22. This file contains the user's Access Key ID and Secret Access Key.
23. AWS_ACCESS_KEY_ID corresponds to the Access Key ID.
24. AWS_SECRET_ACCESS_KEY corresponds to the Secret Access Key.

### Final AWS Setup

- You can now safely eliminate the DISABLE_COLLECTSTATIC variable from Heroku Config Vars, allowing AWS to take over the responsibility of handling static files.
- Within the S3 interface, establish a fresh directory named "media."
- Pick any preexisting media images from your project for the purpose of preparing them for placement in the newly created folder.
- In the "Manage Public Permissions" section, opt for granting public read access to these objects.
- There is no need for any additional configurations; simply proceed by clicking the "Upload" button.

### Stripe API

This project utilizes Stripe for managing ecommerce payments.

After setting up your Stripe account and logging in, follow these steps to establish the connection for your project.

1. Access your Stripe dashboard and expand the "Retrieve your test API keys" section.
2. You will find two keys as follows:
   - STRIPE_PUBLIC_KEY = Publishable Key (starts with pk)
   - STRIPE_SECRET_KEY = Secret Key (starts with sk)

Additionally, to ensure a seamless payment process, we can incorporate Stripe Webhooks as a backup solution in case users accidentally close the purchase order page.

1. Navigate to the Developers section in your Stripe dashboard and select Webhooks.
2. Click on the option to Add Endpoint.
3. Enter the URL: https://pb-majestic-cloding.herokuapp.com/checkout/wh/
4. Select "receive all events."
5. Click Add Endpoint to finalize the setup.
6. You will receive a new key:
   - STRIPE_WH_SECRET = Signing Secret (Webhook) Key (starts with wh)

## Gmail API

This project utilizes Gmail as the platform for sending emails to users to carry out tasks like account verification and purchase order confirmations. To establish a connection for your project, follow these steps after creating a Gmail (Google) account and logging in:

1. Click on the Account Settings, represented by the cog icon, located in the upper-right corner of Gmail.
2. Access the Accounts and Import tab.
3. Under the "Change account settings" section, click on the link that says Other Google Account settings.
4. On the new page, select the Security option from the left-hand menu.
5. Activate 2-Step Verification (which requires password and account verification).
6. After verification, turn on 2FA (Two-Factor Authentication).
7. Return to the Security page, where you will find a new option called App passwords.
8. You may need to confirm your password and account once more.
9. Choose "Mail" as the app type.
10. Opt for "Other (Custom name)" as the device type.
11. Provide a custom name, such as "Django" or "retro-reboot."
12. You will receive a 16-character password (API key).
13. Safely store this key locally because it cannot be retrieved later.
14. Set up the following configurations in your project:
   - EMAIL_HOST_PASS = user's 16-character API key
   - EMAIL_HOST_USER = user's personal Gmail email address

## Heroku Deployment

This project utilizes Heroku, a Platform as a Service (PaaS) that empowers developers to construct, execute, and manage applications entirely within the cloud.

Here are the deployment instructions to be followed after setting up your account:

1. Click on "New" located in the upper-right corner of your Heroku Dashboard, and then choose "Create new app" from the dropdown menu.
2. Ensure that your app name is unique, select a region closest to your location (EU or USA), and finally, click on "Create App."
3. Within the new app's settings, click on "Reveal Config Vars" and configure your environment variables.
4. To ensure proper deployment, Heroku requires two additional files:
   - requirements.txt
   - Procfile
5. You can install the project's requirements (where applicable) using:
   - pip3 install -r requirements.txt
6. If you have custom packages installed, make sure to update the requirements file with the following command:
   - pip3 freeze --local > requirements.txt
7. Create the Procfile using the following command:
   - echo web: gunicorn app_name.wsgi > Procfile
   - Replace "app_name" with the name of your primary Django app, which is the folder where "settings.py" is located.

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Option 1:
- Choose "Automatic Deployment" from the Heroku app.

Option 2:
- In your Terminal/CLI, connect to Heroku using this command: heroku login -i
- Set the remote for Heroku: heroku git:remote -a app_name (replace "app_name" with your app's name)
- After performing the standard Git commands (add, commit, and push) to your GitHub repository, execute:
- git push heroku main
- Your project should now be successfully connected and deployed to Heroku!

## Cloning

To clone the repository, follow these steps:

1. Visit the GitHub repository.
2. Click on the "Code" button located above the list of files.
3. Choose your preferred cloning method, whether it's HTTPS, SSH, or GitHub CLI, and use the copy button to copy the URL to your clipboard.
4. Open either Git Bash or Terminal.
5. Change your current working directory to the desired location for the cloned directory.
6. Within your IDE Terminal, enter the following command to clone my repository:
   - Use the command: "git clone https://github.com/Benohene/pb_majestic_cloding.git"
7. Hit Enter to initiate the creation of your local clone.
   Alternatively, if you're using Gitpod, you can simply click below to generate your own workspace with this repository.

Please keep in mind that to directly open the project in Gitpod, you must have the browser extension installed. You can find a tutorial on how to install it here.

## Forking

"When we fork a GitHub Repository, we create a duplicate of the original repository on our own GitHub account, allowing us to view and edit it without impacting the original owner's repository. You can initiate the forking process by following these steps:

1. Sign in to GitHub and find the desired GitHub Repository.
2. Navigate to the top of the Repository (not the top of the page) just above the "Settings" Button in the menu, where you will find the "Fork" Button.
3. After clicking it, you will have a replica of the original repository in your personal GitHub account!"

## Credits

1. Code Institute Template
   This repository was created using the template provided by Code Institute. Also, without the knowledge gained through the coursework, I would not be able to create this site so thank you Code Institute.

2. Django Documentation
   Thanks to the Django docs which were also used as a step-by-step while going through the project to ensure everything was set up correctly.

3. Allauth Documentation
   Thanks to the Alluath documentation which was referenced during development.

4. Stackoverflow
   I found myself on Stackoverflow so many times researching issues. This a fantastic place to learn and troubleshoot code.

5. Slack
   The Slack community is great and I reached out to fellow students who had already completed their P5 for their advice and got some nice tips and feedback. I attended some webinars by CI staff which I found very beneficial.

# Acknowledgements

- To my mentor Daisy Mc Girr, Daisy always goes above and beyond. Even outside of project planning she is great for advice and is a great help to the Slack community too. Daisy became my Mentor midway through P2 and has been amazing to deal with, she is a great credit to CI and the whole community.

- Also a big one goes to my wife for the support and helping the kids throughout eventhough it was not an easy journey
