### Project Overview

**Vinyl Crate** is a full-stack, data-driven web application that empowers users to catalogue, manage, and explore their personal vinyl record collection. Built with **Django**, **PostgreSQL**, and **Bootstrap**, it offers a clean and responsive interface suitable for both desktop and mobile users.

Registered users can add and edit detailed entries for their records — including artist, title, genre, BPM, musical key (Camelot notation), year, and rating — with the option to upload cover art. The app supports secure user authentication, individual dashboards, and record-level control.

**Vinyl Crate** goes beyond simple record keeping — it's a thoughtfully designed platform for music lovers and DJs who want to document and reflect on their collection in a structured, searchable way.

---

### Site Purpose

Vinyl Crate was created to address a common gap in vinyl record management: while many collectors rely on spreadsheets or handwritten lists, these methods lack visual appeal, accessibility, and interactivity. Vinyl Crate brings record cataloguing into the modern age with a secure, user-friendly, and mobile-responsive web app.

This platform empowers collectors and DJs by offering a clean interface to organise and reflect on their collection — complete with cover images, audio metadata, and personal ratings.

The app provides:
- 📀 **Personal record management** – Add, edit, and browse your vinyl collection
- ⭐ **Custom metadata fields** – Track BPM, musical key, year, genre, and star ratings
- 🖼️ **Visual enhancements** – Upload and display album artwork
- 🔐 **Secure access** – Private user accounts and dashboard views
- 📱 **Mobile-ready** – Use it from the crate or the couch

By focusing on clarity, simplicity, and personalisation, Vinyl Crate makes managing your vinyl collection a rewarding, modern experience — for hobbyists, DJs, and dedicated collectors alike.

---

### Target Audience

Vinyl Crate is designed for:

- 🎵 **Vinyl collectors** who want an organised, digital catalogue of their records  
- 🎧 **DJs** who need quick access to metadata like BPM, key, and genre  
- 📱 **Mobile users** looking for a responsive tool they can access from the record shop or DJ booth  
- 🧠 **Music enthusiasts** who enjoy reflecting on and rating their collection  
- 📂 **Users** who want to move beyond spreadsheets and static lists

Whether you're tracking rare jazz pressings, building a DJ setlist, or simply documenting your growing collection, Vinyl Crate offers a streamlined, flexible space to manage your vinyl library.

##  User Experience (UX)

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