# Customizable Blog Posting Web Application

A simple and customizable Django web application designed to help users quickly set up and manage small projects with ease. This app allows users to personalize the web application according to their needs.

---

## Introduction

This Django web application allows users to write, publish, and manage blog posts. It provides an intuitive interface for creating posts, managing drafts, and viewing published content. The app is customizable, making it suitable for small to medium-sized blogging projects.

---

## Features

- **Create and Edit Posts**: Users can create, edit, and publish blog post.
- **Admin Interface**: Easy-to-use admin panel for managing blog posts.
- **Responsive Design**: Works seamlessly on both desktop and mobile devices.
- **User Authentication**: Users can register, log in, and manage their own posts.
- **Simple UI**: Clean and user-friendly layout for both admins and users.

---

## Folder Structure

The folder structure of the project is as follows:

basicNavbar/
├── basicNavbar/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── navbar/
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   │   └── navbar/
│   │     └── style.css
│   ├── templates/
│   │   └── navbar/
│   │     └── about.html
│   │     └── add_post.html
│   │     └── blog_page.html
│   │     └── contact.html
│   │     └── delete_post.html
│   │     └── edit_post.html
│   │     └── home.html
│   │     └── nav.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
└── manage.py


---

## Customization

You can customize the blog app by modifying the following:

### **Themes and Layout**
- Modify the templates in the `templates/` folder to change the blog's layout.
- The main blog template is in `templates/navbar/nav.html`. Update this to fit your design.

### **Categories and Tags**
- Edit the `models.py` file to add more fields or change how categories and tags are handled.

### **Admin Interface**
- You can add more fields or change how posts appear in the admin panel by editing `admin.py`.

---

## Disclaimer

This project is built for learning purposes only.

---
