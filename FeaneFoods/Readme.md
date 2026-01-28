# Hikari Bento Restaurant Website

A modern, fully functional restaurant website built with **Django**. Users can view the menu, book tables, and contact the restaurant. The project focuses on backend functionality, form handling, and database integration, while maintaining a clean and responsive frontend.



## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)
- [License](#license)

---

## Demo

> You can optionally include a screenshot or link to the live site here.

![Hikari Bento Demo](./FeaneFoods/static/images/hero-bg.jpg)

---

## Features

- **Table Booking:** Users can book tables with date, time, and number of guests.
- **Menu Section:** Showcases menu items with images, prices, and categories.
- **Contact Form:** Users can send messages to the restaurant.
- **Client Testimonials:** Carousel to display customer feedback.
- **Admin Panel:** Manage reservations, messages, and menu items via Django Admin.
- **CSRF Protection & Input Validation:** Secure form submissions with Django’s built-in protections.

---

## Technologies Used

- **Backend:** Django 6.0.1  
- **Frontend:** HTML5, CSS3, Bootstrap 4, jQuery  
- **Database:** SQLite for testing  PostgreSQL for production 
- **Version Control:** Git, GitHub  
- **Other Tools:** Font Awesome, Owl Carousel  

---

## Project Structure

```text
FeaneFoods/
├── FeaneFoods/         # Django project folder
│   ├── settings.py     # Django settings (sensitive, ignored in GitHub)
│   ├── urls.py
│   └── wsgi.py
├── FeanePlace/         # Django app
│   ├── models.py       # Reservation, Contact, MenuItem models
│   ├── views.py        # Views for pages & form handling
│   ├── forms.py        # ModelForms for Reservation & Contact
│   ├── urls.py
│   └── admin.py
├── templates/          # HTML templates
│   ├── index.html
│   ├── about.html
│   ├── menu.html
│   └── book.html
├── static/             # CSS, JS, images, fonts
└── manage.py           # Django management script
