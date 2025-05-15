# Vinyl Crate

**Vinyl Crate** is a full-stack record collection management web application built using Django, Python, HTML, CSS, and JavaScript. The app uses PostgreSQL for data storage and is deployed to Heroku with a responsive front-end styled using Bootstrap.

This project was created as my third milestone project for the Level 5 Diploma in Web Application Development with the Code Institute.

---

##  User Experience (UX)

### Strategy Plane

#### **Project Goals**

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

#### **Feature Planning**

The table below outlines opportunities for the **Vinyl Crate** project. Each feature has been scored for **importance** and **viability** (1 = low, 5 = high). This helps prioritise core functionality for the MVP. Features scoring highly are **must-haves**, while mid-scoring features are **should-haves**, and low-priority features are **could-haves** for future versions.

User roles are also considered in the planning:
- **Guests** – Unauthenticated visitors browsing public-facing content
- **Users** – Registered members with a personalised dashboard
- **Admins** – Staff or superusers with additional content management access

| User Type     | Feature                                      | Importance | Viability | Scope   | Delivered |
|:------------- |:-------------------------------------------- |:----------:|:---------:|:-------:|:---------:|
| All           | View public landing page                     | 5          | 5         | MVP     | ⬜        |
| Guest         | Register for an account                      | 5          | 5         | MVP     | ⬜        |
| User          | Log in/out and manage session                | 5          | 5         | MVP     | ⬜        |
| User          | Password recovery                            | 5          | 5         | MVP     | ⬜        |
| User          | Create, view, update, delete own records     | 5          | 5         | MVP     | ⬜        |
| User          | Upload cover image for record                | 5          | 5         | MVP     | ⬜        |
| User          | Add individual tracks to each record         | 5          | 4         | MVP     | ⬜        |
| Admin         | Access Django admin panel                    | 5          | 5         | MVP     | ⬜        |
| Admin         | Moderate/edit user records via admin         | 5          | 5         | MVP     | ⬜        |
| Admin         | Edit track list inline in Record admin panel | 4          | 5         | Should  | ⬜        |
| User          | Filter/sort by genre, year, BPM, rating      | 4          | 5         | Should  | ⬜        |
| User          | Search records by title/artist               | 4          | 4         | Should  | ⬜        |
| User          | Include BPM, key, and duration per track     | 4          | 4         | Should  | ⬜        |
| All           | Responsive design / Bootstrap UI             | 4          | 5         | MVP     | ⬜        |
| All           | View mobile-friendly site                    | 4          | 5         | MVP     | ⬜        |
| User          | Rate records with 1–5 stars                  | 4          | 5         | MVP     | ⬜        |
| User          | Use dropdowns for genre and key              | 4          | 5         | MVP     | ⬜        |
| User          | Export collection as CSV                     | 3          | 4         | Could   | ⬜        |
| Guest         | Social media login/sign-up                   | 3          | 4         | Could   | ⬜        |
| Admin         | Automatically show total track count per record | 3          | 3         | Could   | ⬜        |
| User          | Edit/update account profile                  | 2          | 3         | Could   | ⬜        |
| All           | Custom 404 and 500 error pages               | 2          | 4         | Could   | ⬜        |
| All           | About/Contact page                           | 2          | 3         | Could   | ⬜        |
| User          | Pre-populated demo records / staff picks     | 2          | 3         | Could   | ⬜        |

---

### Structure Plane

#### **User Stories**

| ID | As a/an        | I want to be able to...                             | So that I can... |
|:---|:---------------|:----------------------------------------------------|:-----------------|
| 1  | New Visitor    | Browse a public record or staff-picked collection   | See what the site is about before registering |
| 2  | New Visitor    | View example record entries with metadata           | Understand how records are displayed and organised |
| 3  | New Visitor    | See a clear sign-up or log-in prompt                | Know how to get started |
| 4  | User           | Register and log in                                 | Access my personal dashboard and collection |
| 5  | User           | Add new records to my collection                    | Keep an up-to-date log of the vinyl I own |
| 6  | User           | Upload a cover image for a record                   | Make my collection visually rich |
| 7  | User           | Edit existing records                               | Correct mistakes or update metadata |
| 8  | User           | Delete a record from my collection                  | Keep my library clean and relevant |
| 9  | User           | View full details for a single record               | See all metadata and visuals in one place |
| 10 | User           | Sort and filter my collection                       | Quickly find records by genre, BPM, or rating |
| 11 | User           | Search for a specific record                        | Find entries fast without scrolling |
| 12 | User           | Rate a record using 1–5 stars                       | Track how much I value or enjoy a record |
| 13 | User           | Export my collection as a CSV                       | Back it up or use it in another system |
| 14 | User           | Recover my password                                 | Regain access if I forget my login details |
| 15 | User           | Edit my account profile                             | Update my display name, location, or bio |
| 16 | User           | Sign in via social media (optional)                 | Log in more quickly or conveniently |
| 17 | User           | Add individual tracks to each record                | Log full tracklists for more detailed entries |
| 18 | User           | Include BPM, key, and duration for each track       | Help with DJing or playlist curation |
| 19 | Admin          | Access the Django admin panel                       | Manage users and records directly |
| 20 | Admin          | Edit or delete any record in the system             | Support users and maintain database integrity |
| 21 | Admin          | Review user-submitted content                       | Ensure the platform remains clean and appropriate |
| 22 | Admin          | Manage tracks directly from the Record admin view   | Save time editing metadata without switching models |
| 23 | Mobile User    | Access my collection on a phone or tablet           | View or update records while crate digging or DJing |
| 24 | Mobile User    | Upload cover images from my device                  | Add new records quickly without needing a computer |


*All user stories were manually tested. See [ User Story Testing]() for full test results.*