##Wax Wisdom
Wax Wisdom was originally created as a Bi weekly blog which posted candle frangrance combinations as well as how to tutorials for its readers. The blog became so popular and received so many messages for sales of the products featured that the owners decided to create a shop.

Table of Contents
Introduction
Overview
UX - User Experience
Design Inspiration
Colour Scheme
Font
Project Planning
Strategy Plane
Site Goals
Agile Methodologies - Project Management
MoSCoW Prioritization
Sprints
User Stories
Scope Plane
Structural Plane
Skeleton & Surface Planes
Wireframes
Database Schema - Entity Relationship Diagram
Security
Features
User View - Registered/Unregistered
Role-Based Dashboard Features
Role-Based Navigation
Soft Delete/Archiving for Patient Accounts
Appointment Booking System
Messaging System
Profile Management
Confirmation Messages
CRUD Functionality
Feature Showcase
Future Features
Technologies & Languages Used
Libraries & Frameworks
Tools & Programs
Testing
Validation Testing
User Testing
Bugs
Deployment
Connecting to GitHub
Django Project Setup
Cloudinary API
PostgreSQL
Heroku deployment
Clone project
Fork Project
Privacy Policy
Credits
Code
Media
Additional reading/tutorials/books/blogs
Acknowledgements
Overview
Wax wisdom is an online blog website which offers customers weekly candle making workshop that allows users to:

register and create a profile
Book a candle workshop
leave a review
contact us via a form
UX - User Experience
Design Inspiration
My inspiration for Wax wisdom came from my joy of making candles .

Colour Scheme
alt text In line with the healthcare theme, I chose a neutral, clean palette:
![alt text](<static/images/colour scheme calm candles.png>)
Primary Color: #17A2B8 (Navy Blue-Grey)
Secondary Color: #132B67 (Hospital Blue)
Accent Color: #333 (grey)
Background: #fff (White) This combination ensures clarity, accessibility, and a professional appearance, allowing for easy navigation throughout the site.
Font
For the logo and headers, I will be using Lora.
The rest of the body text and interactive elements will use Catamaran for its readability and clean look.
Project Planning
Strategy Plane
The primary objective of Calm Candles is to bring together an informative blog about candle creation and ecommerce. By offering an intuitive interface, users can easily buy candles safely and seamlessly from a trusted company who beleive in high quality.

Site Goals
Provide customers with a user-friendly platform to buy candles.
Allow customers to register a username so they can track their orders with ease.
Offer an intuitive interface with role-based dashboards for admins.
Agile Methodologies - Project Management
I used an agile approach to project management. The HealMate development process was broken into sprints, and tasks were added to the GitHub project board to be tracked and managed through issues.

MoSCoW Prioritization
Must-Haves: User registration and login,  workshop booking.
Should-Haves: Feedback system, health tools, advanced filtering options.
Could-Haves: Profile pictures for users and specialists, messaging system.
Won’t-Haves: Full payment integration, doctor-patient messaging for now.
Sprints
Sprint 1: Initial Setup - Project, repository, environment setup.
Sprint 2: User Authentication & Role-Based Dashboards.
Sprint 3: Specialist Search & Appointment Booking System.
Sprint 4: Static Pages & UI/UX Improvements.
Sprint 5: Deployment & Testing.
Sample User Stories
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

Skeleton & Surface Planes
Wireframes
Wireframes were created for the following key pages to ensure an intuitive user journey:

Home Page
mobile home page view

alt text

Tablet home page view

alt text

Desktop home page view

alt text

Specialist Search Results
Homepage Wireframe

Homepage Wireframe

Appointment Booking
Homepage Wireframe

Homepage Wireframe

User Dashboards (Patient and Specialist)
Admin Panel
Wireframes were designed using Balsamiq, ensuring responsiveness across devices.

Database Schema - Entity Relationship Diagram
The ERD for HealMate illustrates the relationships between the users, specialists, appointments, and more. This is essential to demonstrate the relationships between the different models in the PostgreSQL database.

The ERD also demonstrates the platform's role-based structure. Each user is assigned to a specific group (patient, specialist, or admin) that determines their access level. PatientProfile and SpecialistProfile models are linked to the User model, and each profile type has specific fields relevant to their role. Admins have broader access to manage both specialist vetting and platform data.

ERD Illustration
![alt text](<static/ERD wax wisdom (1).png>)
The above ERD was generated using Python Extension - pygraphviz and pydotplus. Documentation at https://django-extensions.readthedocs.io/en/latest/graph_models.html.

Security
All data is securely handled with Django’s security features, including:

CSRF protection for form submissions.
Data encryption for sensitive information like passwords using Django's built-in authentication.
Role-based access control to restrict sensitive data to authorized users.
Role-based access control (RBAC) is implemented using Django's Group and Permission systems. Patients, specialists, and admins are grouped based on their role, and their access to features and sensitive information is restricted accordingly. Patients can only access their own medical data and booking history, while specialists can only view data related to their consultations. Admins have the broadest access for system management.