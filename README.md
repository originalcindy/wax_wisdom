# **Wax Wisdom**
Wax Wisdom is a fictious candle making blog which posts blogs weekly on various fragrance combinations, tips etc as well as how to tutorials for its readers. The blog became so popular and received so many messages that the owner Lechner decided to host candle making workshops for her loyal customers. 

## **Table of Contents**
## Table of Contents
1. [Introduction](#introduction)
2. [Overview](#overview)
3. [UX - User Experience](#ux---user-experience)
    - [Design Inspiration](#design-inspiration)
    - [Colour Scheme](#colour-scheme)
    - [Font](#font)
4. [Project Planning](#project-planning)
    - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
    - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [MoSCoW Prioritization](#moscow-prioritization)
    - [Sprints](#sprints)
    - [User Stories](#user-stories)
5. [Scope Plane](#scope-plane)
6. [Structural Plane](#structural-plane)
7. [Skeleton & Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
8. [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
9. [Security](#security)
10. [Features](#features)
    - [User View - Registered/Unregistered](#user-view---registeredunregistered)
    - [Role-Based Dashboard Features](#role-based-dashboard-features)
    - [Role-Based Navigation](#role-based-navigation)
    - [Soft Delete/Archiving for Patient Accounts](#soft-deletearchiving-for-patient-accounts)
    - [Appointment Booking System](#appointment-booking-system)
    - [Messaging System](#messaging-system)
    - [Profile Management](#profile-management)
    - [Confirmation Messages](#confirmation-messages)
    - [CRUD Functionality](#crud-functionality)
    - [Feature Showcase](#feature-showcase)
11. [Future Features](#future-features)
12. [Technologies & Languages Used](#technologies--languages-used)
13. [Libraries & Frameworks](#libraries--frameworks)
14. [Tools & Programs](#tools--programs)
15. [Testing](#testing)
  - [Validation Testing](#validation-testing)
  - [User Testing](#user-testing)
  - [Bugs](#bugs)
16. [Deployment](#deployment)
    - [Connecting to GitHub](#connecting-to-github)
    - [Django Project Setup](#django-project-setup)
    - [Cloudinary API](#cloudinary-api)
    - [PostgreSQL](#postgresql)
    - [Heroku deployment](#heroku-deployment)
    - [Clone project](#clone-project)
    - [Fork Project](#fork-project)
17. [Privacy Policy](#privacy-policy)
18. [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
    - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
19. [Acknowledgements](#acknowledgements)

## overview
Wax wisdom is an online blog website which offers customers weekly candle making workshop that allows users to:

register and create a profile
Book a candle workshop
leave a review
contact us via a form
UX - User Experience
Design Inspiration
My inspiration for Wax wisdom came from my joy of making candles .

## UX - User Experience

Colour Scheme
alt text In line with the healthcare theme, I chose a neutral, clean palette:
![alt text]
Primary Color: #17A2B8 (Navy Blue-Grey)
Secondary Color: #132B67 (Hospital Blue)
Accent Color: #333 (grey)
Background: #fff (White) This combination ensures clarity, accessibility, and a professional appearance, allowing for easy navigation throughout the site.
Font
For the logo and headers, I will be using Lora.
The rest of the body text and interactive elements will use Catamaran for its readability and clean look.
Project Planning

## Strategy Plane
### Design Inspiration
The primary objective of Calm Candles is to bring together an informative blog about candle creation and ecommerce. By offering an intuitive interface, users can easily buy candles safely and seamlessly from a trusted company who beleive in high quality.

Your site goals for the Wax Wisdom project will align with the purpose of the site, its intended audience, and the core functionalities you plan to implement. Here’s a detailed breakdown of the site goals:

1. Provide Candle-Related Information
Goal: Establish Wax Wisdom as a trusted source of information about candles and candle-making.
Features Supporting This Goal:
Blog section with engaging and informative posts about candles, DIY tips, and related topics.
Easy-to-navigate structure for users to browse blog posts.
2. Offer Workshop Booking
Goal: Enable users to easily book candle-making workshops to enhance their skills and learn about the art of candle-making.
Features Supporting This Goal:
Workshop listing with details (e.g., date, time, location, capacity).
Workshop booking system with availability and validation for user bookings.
Confirmation and notification system for bookings.
3. Build a Community of Candle Enthusiasts
Goal: Create an engaging platform for users who are passionate about candles and candle-making.
Features Supporting This Goal:
User authentication to allow interaction with the site (e.g., booking, leaving reviews).
Review system for users to share their feedback on workshops.
Potential for future community features, like user comments on blog posts or forums.
4. Enhance Brand Identity
Goal: Promote the Wax Wisdom brand as a leading candle-making workshop provider.
Features Supporting This Goal:
Consistent and aesthetically pleasing design aligned with the brand.
Content that highlights the expertise and unique selling points of Wax Wisdom workshops.
A "About Us" section to build trust and provide background about the company.
5. Ensure Usability and Accessibility
Goal: Deliver a user-friendly and accessible experience for all users, regardless of device or ability.
Features Supporting This Goal:
Responsive design that adapts to all screen sizes (mobile, tablet, desktop).
Adherence to Web Content Accessibility Guidelines (WCAG).
Clear navigation and intuitive user interface.
6. Drive Business Growth
Goal: Increase workshop attendance and grow Wax Wisdom’s customer base.
Features Supporting This Goal:
Easy-to-use booking process that minimizes user friction.
SEO-friendly blog content to drive organic traffic.
Integration of social sharing options to promote content and workshops.
7. Gather Feedback and Insights
Goal: Collect valuable feedback from users to improve the workshops and the overall user experience.
Features Supporting This Goal:
Reviews and ratings system for workshops.
Data collection on user behavior and popular blog topics (for potential analytics).

#### MoSCoW Prioritization
## Must Have 
User Authentication

Registration, login, and logout functionality.
Role-based access (admin vs. customer).
Password security using Django's built-in authentication.
Workshop Booking System

Form for users to book workshops.
Database to store booking information.
Booking validation (e.g., availability, duplicate bookings).
Blog Section

Create, read, update, delete (CRUD) functionality for blog posts (admin-only).
Blog post listings and detailed views for users.
SEO-friendly structure for blog posts.
Workshop Review System

Users can leave reviews for workshops.
Display reviews on the workshop detail pages.
Responsive Design

Fully functional on mobile, tablet, and desktop.
Accessible layout adhering to Web Content Accessibility Guidelines (WCAG).
Database and Models

Custom models for workshops, bookings, and reviews.
Properly managed migrations to reflect database structure.
Basic Deployment

Host the application on a cloud platform (e.g., Heroku or Render).
Secure deployment (environment variables, DEBUG mode off).
Should Have (Important but not critical for immediate delivery)
These features add significant value and should be included if time permits.

About Us Page

Informational page about the company and its mission.
Improved Notificatons
Confirmation emails for workshop bookings.
Feedback messages after booking or submitting a review.
Pagination and Filtering

Blog post pagination.
Filtering workshops by date, location, or availability.
Admin Dashboard Enhancements

Admin view to manage bookings and reviews.
Charts or stats to track booking trends.
Could Have (Desirable but not necessary)
These features can be deferred to later phases of the project.
## Wont Have
Search Functionality

Search bar for blog posts or workshops.
Wishlist for Workshops

Allow users to "save" workshops they are interested in.
Social Sharing

Buttons to share blog posts or workshops on social media.
Workshop Recommendations

Suggest workshops based on user preferences or past bookings.
User Profile Page

View past bookings and reviews submitted.


E-commerce Integration

Selling candles or workshop-related products online.
Advanced Analytics

User behavior tracking and advanced reporting tools.
Gamification

Reward systems or badges for workshop participation or reviews.
Live Chat or Chatbot

Customer support features like live chat.

Won’t Have (For Now) (Not in scope for the current project)
Won’t Have (For Now) (Not in scope for the current project)

## Sprints

**sprint 1** Project setup, GitHub configuration, Agile board setup, and initial database setup.
**sprint 2**Create blog models and views, implement list and detail pages, and add styling.
**sprint 3**Create workshop and booking models, forms, and views. Test booking functionality.
**sprint 4**Implement user authentication (register, login, logout) and role-based access.
**sprint 5**Create review model, forms, and views. Link reviews to workshops.
**sprint 6**Complete front-end styling (home page, blog, booking, reviews).
**sprint 7**Write tests for models, forms, and views. Perform manual testing.
**sprint 8**Prepare deployment (static files, environment variables).
**sprint 9**Deploy project to the cloud. Finalise README file with documentation.

## Sample User Stories
Blog
As a user, I want to view a list of blog posts so that I can read about candle-related topics.
As an admin, I want to create, edit, and delete blog posts so that I can manage content on the website.
Workshop Booking
As a user, I want to view available workshops so that I can choose one to attend.
As a user, I want to book a workshop so that I can learn candle-making.
Review System
As a user, I want to leave a review after attending a workshop so that I can share my feedback.
As an admin, I want to manage reviews so that I can ensure quality feedback on the website.
User Authentication
As a user, I want to register and log in so that I can book workshops and leave reviews.
As an admin, I want to manage users so that I can monitor bookings and reviews.

The Wax Wisdom platform will include the following MVP functionalities:

User registration and role-based dashboards.
Candle workshop scheduling for customers
Specialist profiles showcasing specialty, experience, and availability.
Structural Plane
The site is structured around an easy-to-use interface. The primary menu includes links to specialist searches, appointment bookings, and user profile management.

## Skeleton & Surface Planes
Wireframes
Wireframes were created for the following key pages to ensure an intuitive user journey:

Home Page
mobile home page view

alt text

Tablet home page view

alt text

Desktop home page view

alt text

Blog post page
![alt text](<static/images/Blog Post wireframe.png>)

User Dashboards (Patient and Specialist)
Admin Panel
Wireframes were designed using Balsamiq, ensuring responsiveness across devices.

## Database Schema - Entity Relationship Diagram
The ERD for Wax wisdom illustrates the relationships between the users, candle enthusiasts, bookings, and more. This is essential to demonstrate the relationships between the different models in the PostgreSQL database.

The ERD also demonstrates the platform's role-based structure. Each user is assigned to a specific group that determines their access level. PatientProfile and SpecialistProfile models are linked to the User model, and each profile type has specific fields relevant to their role. Admins have broader access to manage both specialist vetting and platform data.

ERD Illustration
![alt text](<static/ERD wax wisdom (1).png>)
The above ERD was generated using lucid.app

Security
All data is securely handled with Django’s security features, including:

CSRF protection for form submissions.
Data encryption for sensitive information like passwords using Django's built-in authentication.
Role-based access control to restrict sensitive data to authorized users.
Role-based access control (RBAC) is implemented using Django's Group and Permission systems. Patients, specialists, and admins are grouped based on their role, and their access to features and sensitive information is restricted accordingly. Patients can only access their own medical data and booking history, while specialists can only view data related to their consultations. Admins have the broadest access for system management.
