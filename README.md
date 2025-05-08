# Vinyl Crate

**Vinyl Crate** is a full-stack record collection management web application built using Django, Python, HTML, CSS, and JavaScript. The app uses PostgreSQL for data storage and is deployed to Heroku with a responsive front-end styled using Bootstrap.

This project was created as my third milestone project for the Level 5 Diploma in Web Application Development with the Code Institute.

---

##  User Experience (UX)

### Strategy Plane

#### Project Goals

**Vinyl Crate** is a **personal record collection management app** created for vinyl enthusiasts, DJs, and music collectors. The platform allows users to build and organise a digital library of their physical records — complete with metadata such as artist, title, genre, BPM, musical key, and cover art.

This app is designed to replace basic spreadsheets and paper lists with a user-friendly, mobile-responsive interface. Users can easily search, filter, and update their collections on the go — whether they're browsing at home, preparing a DJ set, or crate digging in a record shop.

Vinyl records have seen a major resurgence in popularity, and tools like **Vinyl Crate** empower collectors to track, rate, and catalogue their collections in a modern, cloud-based format. Built as part of a Level 5 Web Application Development course, Vinyl Crate focuses on usability, functionality, and clean design to deliver a polished user experience for managing music libraries.

#### Target Audience

Whether you're tracking rare jazz pressings, building a DJ setlist, or simply documenting your growing collection, Vinyl Crate offers a streamlined, flexible space to manage your vinyl library.

**Vinyl Crate** is designed for:

- 🎵 **Vinyl collectors** who want an organised, digital catalogue of their records  
- 🎧 **DJs** who need quick access to metadata like BPM, key, and genre  
- 📱 **Mobile users** looking for a responsive tool they can access from the record shop or DJ booth  
- 🧠 **Music enthusiasts** who enjoy reflecting on and rating their collection  
- 📂 **Users** who want to move beyond spreadsheets and static lists

**Vinyl Crate** provides:

- 📀 **Personal record management** – Add, edit, and browse your vinyl collection
- ⭐ **Custom metadata fields** – Track BPM, musical key, year, genre, and star ratings
- 🖼️ **Visual enhancements** – Upload and display album artwork
- 🔐 **Secure access** – Private user accounts and dashboard views
- 📱 **Mobile-ready** – Use it from the crate or the couch

---

### Scope Plane

#### Feature Planning

The table below outlines opportunities for the **Vinyl Crate** project. Each feature has been scored for **importance** and **viability** (1 = low, 5 = high). This helps prioritise core functionality for the MVP. Features scoring highly are **must-haves**, while mid-scoring features are **should-haves**, and low-priority features are **could-haves** for future versions.

User roles are also considered in the planning:
- **Guests** – Unauthenticated visitors browsing public-facing content
- **Users** – Registered members with a personalised dashboard
- **Admins** – Staff or superusers with additional content management access

| User Type     | Feature                                      | Importance | Viability | Scope   | Delivered |
|:-------------:|:--------------------------------------------:|:----------:|:---------:|:-------:|:---------:|
| All           | View public landing page                     | 5          | 5         | MVP     | ⬜        |
| Guest         | Register for an account                      | 5          | 5         | MVP     | ⬜        |
| User          | Log in/out and manage session                | 5          | 5         | MVP     | ⬜        |
| User          | Password recovery                            | 5          | 5         | MVP     | ⬜        |
| User          | Create, view, update, delete own records     | 5          | 5         | MVP     | ⬜        |
| User          | Upload cover image for record                | 5          | 5         | MVP     | ⬜        |
| Admin         | Access Django admin panel                    | 5          | 5         | MVP     | ⬜        |
| Admin         | Moderate/edit user records via admin         | 5          | 5         | MVP     | ⬜        |
| User          | Filter/sort by genre, year, BPM, rating      | 4          | 5         | Should  | ⬜        |
| User          | Search records by title/artist               | 4          | 4         | Should  | ⬜        |
| All           | Responsive design / Bootstrap UI             | 4          | 5         | MVP     | ⬜        |
| All           | View mobile-friendly site                    | 4          | 5         | MVP     | ⬜        |
| User          | Rate records with 1–5 stars                  | 4          | 5         | MVP     | ⬜        |
| User          | Use dropdowns for genre and key              | 4          | 5         | MVP     | ⬜        |
| User          | Export collection as CSV                     | 3          | 4         | Could   | ⬜        |
| Guest         | Social media login/sign-up                   | 3          | 4         | Could   | ⬜        |
| User          | Edit/update account profile                  | 2          | 3         | Could   | ⬜        |
| All           | Custom 404 and error pages                   | 2          | 4         | Could   | ⬜        |
| All           | About / Contact page                         | 2          | 3         | Could   | ⬜        |
| User          | Pre-populated demo records / staff picks     | 2          | 3         | Could   | ⬜        |


###  User Stories

As a **new visitor**, I want to:
- Browse a public record or staff-picked collection so that I can see what the site is about before registering
- See a clear call to action to sign up or log in so that I know how to get started using the platform
- View example record entries with cover art and metadata so that I can understand how records are displayed and organised

As a **registered user**, I want to:
- Add new records to my collection so that I can keep an up-to-date log of the vinyl I own
- Upload cover images when creating or editing a record so that my collection is visually rich and easier to browse
- Edit existing records so that I can correct mistakes or update information as needed
- Delete records I no longer want in my collection so that I can keep my library clean and relevant
- View a detailed page for each record so that I can see all the metadata and images in one place

As an **admin**, I want to:
- Access the Django admin panel so that I can manage user accounts and database records directly
- Review and manage user-submitted content so that I can ensure the platform remains appropriate and consistent
- Edit or delete any record in the system so that I can support users and maintain data integrity across the platform

As a **mobile user**, I want to:
- Browse and manage my record collection on a phone or tablet so that I can access my library on the go, such as while crate digging or DJing
- Upload cover images directly from my device so that I can quickly add new records without needing a desktop computer

*All user stories were manually tested. See [ User Story Testing]() for full test results.*