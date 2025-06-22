# Vinyl Crate

Visit the deployed site here: [Vinyl Crate](https://vinyl-crate-ab3f8a285d4e.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/sd-powell/portfolio_project_3) ![GitHub repo size](https://img.shields.io/github/repo-size/sd-powell/portfolio_project_3) ![GitHub language count](https://img.shields.io/github/languages/count/sd-powell/portfolio_project_3)

## Introduction

**Vinyl Crate** is a full-stack record collection management app that helps users digitally archive, explore, and celebrate their vinyl records. Built with **Django, Python, HTML, CSS, and JavaScript**, it uses a **PostgreSQL** database and is deployed on **Heroku**. The app blends practical record tracking with a clean, responsive UI styled with Bootstrap.

The platform provides vinyl enthusiasts with a personal digital space to catalogue their analogue collections. Users can upload album art, log detailed metadata, and manage their growing crates — all in one place.

Whether you're a casual listener or seasoned audiophile, Vinyl Crate aims to make record collection management both accessible and rewarding. Features like intuitive search, smart filters, ratings, and tracklists encourage deeper engagement with your music. Highlighted staff picks and future integration plans further enhance the experience.

By supporting mindful collecting and visual storytelling, Vinyl Crate helps users take pride in their collections — not just as lists, but as living archives. The platform is designed to scale with each user’s habits and tastes.

**Target Audience:** Vinyl collectors and music lovers of all ages who want a curated, user-friendly space to manage and revisit their records. Whether you're just starting out or managing hundreds of albums, Vinyl Crate is built for analog enthusiasts in a digital world.

---

<a id="contents"></a>

## CONTENTS

- [User Experience](#ux)
  - [Strategy Plane](#strategy-plane)
  - [Scope Plane](#scope-plane)
  - [Structure Plane](#structure-plane)
  - [Database Schema](#database-schema)
  - [Skeleton Plane](#skeleton-plane)
      - [Wireframes](#wireframes)
        - [Mobile Wireframes](#mobile-frames)
        - [Tablet Wireframes](#tablet-frames)
        - [Desktop Wireframes](#desktop-frames)
  - [Surface Plane](#surface-plane)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Features](#features)
        - [The Home Page](#home-page-features)
        - [The Dashboard Page](#dashboard-features)
        - [The My Crate Page](#my-crate-features)
        - [The Record Detail Page](#record-detail-features)
        - [The 400 Page](#400-page-features)
        - [The 403 Page](#403-page-features)
        - [The 404 Page](#404-page-features)
        - [The 500 Page](#500-page-features)

- [Development Process](#dev-process)
    - [Future Implementations](#future-implementation)
    - [Accessibility](#accessibility)

* [Technologies Used](#technologies)

  - [Languages Used](#languages)
  - [Frameworks, Libraries & Programs Used](#frameworks)

* [Deployment & Local Development](#deployment-development)

  - [Deployment](#development)
  - [Local Development](#local-development)
    - [How to Fork](#fork)
    - [How to clone](#clone)

* [Testing](#testing-readme)

* [Credits & Inspiration](#credits&inspiration)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgement](#acknowledgement)

---

<a id="ux"></a>

##  User Experience (UX)

<a id="strategy-plane"></a>

### Strategy Plane

#### **Project Goals**

**Vinyl Crate** is a **personal record collection management app** built for vinyl enthusiasts, DJs, and music collectors. It allows users to digitally archive and organise their physical records, complete with metadata like artist, title, genre, BPM, musical key, and cover art.

The app replaces basic spreadsheets and paper lists with a **mobile-responsive**, user-friendly interface. Whether at home, preparing a DJ set, or crate-digging in a shop, users can easily search, filter, and update their collections on the go.

As vinyl continues its resurgence, tools like Vinyl Crate empower users to rate, track, and manage their collections in a modern, cloud-based format. Built as part of a Level 5 Web Application Development course, the project focuses on **usability, clean design, and practical functionality** to deliver a polished music library experience.

#### **Target Audience**

Whether you're tracking rare jazz pressings, building a DJ setlist, or simply documenting your growing collection, **Vinyl Crate** offers a streamlined, flexible space to manage your vinyl library.

It’s designed for:

- 🎵 **Vinyl collectors** – Build a searchable, filterable digital catalogue  
- 🎧 **DJs** – Quickly access BPM, key, and genre for set planning  
- 📱 **Mobile users** – Use on the go while browsing or performing  
- 🧠 **Music lovers** – Reflect on and rate your collection  
- 📂 **Spreadsheet migrators** – Move to a cleaner, more visual solution

**Key features include:**

- 📀 **Personal record management** – Add, edit, and browse your vinyl archive
- 🛠️ **Full CRUD functionality** – Easily add, view, update, or remove records from your collection  
- ⭐ **Detailed metadata fields** – BPM, musical key, year, genre, and star ratings  
- 🖼️ **Visual enhancements** – Upload and display cover art  
- 🔐 **Secure access** – Private user accounts and personalised dashboards  
- 📱 **Responsive UI** – Built mobile-first for crate-digging or couch-surfing

---

<a id="scope-plane"></a>

### Scope Plane

#### **Feature Planning**

The table below outlines opportunities for the **Vinyl Crate** project. Each feature has been scored for **importance** and **viability** (1 = low, 5 = high). This helps prioritise core functionality for the MVP. Features scoring highly are **must-haves**, while mid-scoring features are **should-haves**, and low-priority features are **could-haves** for future versions.

User roles are also considered in the planning:
- **Guests** – Unauthenticated visitors browsing public-facing content
- **Users** – Registered members with a personalised dashboard
- **Admins** – Staff or superusers with additional content management access

| User Type     | Feature                                      | Importance | Viability | Priority| Delivered |
|:------------- |:-------------------------------------------- |:----------:|:---------:|:-------:|:---------:|
| All           | View public landing page                     | 5          | 5         | MVP     | ✅        |
| Guest         | Register for an account                      | 5          | 5         | MVP     | ✅        |
| User          | Log in/out and manage session                | 5          | 5         | MVP     | ✅        |
| User          | Password recovery                            | 5          | 5         | MVP     | ✅        |
| User          | Create, view, update, delete own records     | 5          | 5         | MVP     | ✅        |
| User          | Upload cover image for record                | 5          | 5         | MVP     | ✅        |
| User          | Add individual tracks to each record         | 5          | 4         | MVP     | ✅        |
| Admin         | Access Django admin panel                    | 5          | 5         | MVP     | ✅        |
| Admin         | Moderate/edit user records via admin         | 5          | 5         | MVP     | ✅        |
| Admin         | Edit track list inline in Record admin panel | 4          | 5         | Should  | ✅        |
| User          | Filter/sort by genre, year, BPM, rating      | 4          | 5         | Should  | ✅        |
| User          | Search records by title/artist               | 4          | 4         | Should  | ✅        |
| User          | Include BPM, key, and duration per track     | 4          | 4         | Should  | ✅        |
| All           | Responsive design / Bootstrap UI             | 4          | 5         | MVP     | ✅        |
| All           | View mobile-friendly site                    | 4          | 5         | MVP     | ✅        |
| User          | Rate records with 1–5 stars                  | 4          | 5         | MVP     | ✅        |
| User          | Use dropdowns for genre and key              | 4          | 5         | MVP     | ✅        |
| User          | Export collection as CSV                     | 3          | 4         | Could   | ❌        |
| Guest         | Social media login/sign-up                   | 3          | 4         | Could   | ❌        |
| Admin         | Automatically show total track count per record | 3       | 3         | Could   | ❌        |
| User          | Edit/update account profile                  | 2          | 3         | Could   | ❌        |
| All           | Custom 404 and 500 error pages               | 2          | 4         | Could   | ✅        |
| All           | About/Contact page                           | 2          | 3         | Could   | ❌        |
| User          | Pre-populated demo records / staff picks     | 2          | 3         | Could   | ✅        |
| Guest         | Public profile for viewing crates            | 3          | 2         | Could   | ❌        |
| User          | Integrate Discogs API                        | 4          | 2         | Could   | ❌        |

---

<a id="structure-plane"></a>

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
| 25 | All Users      | See a friendly error page (404/500)                 | Know if something has gone wrong and what to do next |
| 26 | User           | See my most recently added records at the top       | Quickly access what I just added                     |

> [!NOTE]
> All user stories were manually tested. See [User Story Testing](TESTING.md) for full test results.

<a id="database-schema"></a>

#### **Database Schema**

This project uses a **relational database (PostgreSQL)** to provide structured, reliable storage with built-in support for **referential integrity** — ideal for managing user-specific vinyl collections.

The **initial MVP** centered on a single `Record` model linked to Django’s built-in `User` model. This model captured core metadata such as title, artist, genre, release year, rating, and a cover image. It allowed for rapid prototyping, admin integration, and full CRUD functionality.

However, during development it became clear that additional granularity was required to represent **individual tracks** on a vinyl release. Initially, fields like BPM and key were stored on the `Record`, which resulted in inaccurate or conflicting data for albums with multiple tracks. This design limitation highlighted the need for normalization.

To address this, a dedicated `Track` model was introduced. Each `Track` is linked to a `Record` via a foreign key, establishing a clear **one-to-many relationship**. Track-specific fields (such as BPM and key) were moved accordingly, improving both **data accuracy** and **model scalability**.

This updated schema follows **relational database best practices**, reducing redundancy, improving clarity, and allowing for future expansion — such as sorting, filtering, or displaying track-level data.

#### Core Models

- `Record`
  - `user` (ForeignKey to User)
  - `title`, `artist`, `genre`, `year`, `rating`, `cover_image`, `slug`, etc.
  
- `Track`
  - `record` (ForeignKey to Record)
  - `title`, `position`, `duration`, `bpm`, `key`

The database schema diagram was generated using [dbdiagram.io](https://dbdiagram.io), which provided a clear visual representation of the relational structure between users, records, and tracks using DBML syntax.

<details>
<summary>Click here to view the database schema</summary>

![Vinyl Crate Database Schema](documentation/readme/structure_plane/database-schema.webp)

</details>


<a id="skeleton-plane"></a>

### Skeleton Plane

<a id="wireframes"></a>

#### **Wireframes**

Initial wireframes were created using [Balsamiq](https://balsamiq.com/) to plan the layout and user flow of the **Vinyl Crate** web application. Wireframes were developed for **mobile, tablet, and desktop** to ensure the site would be fully responsive and accessible across devices.

These wireframes informed the site’s **information hierarchy** and **user journey**, covering key views such as the homepage, dashboard, record collection, and record detail pages. They served as a visual blueprint throughout development, helping guide the placement of search, filter, and CRUD elements with a **mobile-first** approach.

> [!NOTE]
> Individual form views (e.g. add/edit record) were not wireframed, as Django Crispy Forms was used to handle layout and rendering consistently across devices.

<br>
<hr>

<a id="mobile-frames"></a>

#### **Mobile Wireframes**

<details>
<summary> Click here to see the Mobile Wireframes </summary>

|                Home page wireframe                |                Dashboard page wireframe                 |                   My Crate page wireframe                    |
| :-----------------------------------------------: | :-------------------------------------------------: | :-------------------------------------------------------------: |
| ![Home](documentation/readme/skeleton_plane/wireframe-mobile-home.webp) | ![Dashboard](documentation/readme/skeleton_plane/wireframe-mobile-dashboard.webp) | ![My Crate](documentation/readme/skeleton_plane/wireframe-mobile-collection.webp) |

|                   Record Detail page wireframe                   |                400 page wireframe                |                 403 page wireframe                  |
| :-----------------------------------------------------------: | :-----------------------------------------------: | :-----------------------------------------------------: |
| ![Record Detail](documentation/readme/skeleton_plane/wireframe-mobile-detail.webp) | ![400](documentation/readme/skeleton_plane/wireframe-mobile-400.webp) | ![403](documentation/readme/skeleton_plane/wireframe-mobile-403.webp) |

|               404 page wireframe                |               500 page wireframe                |
| :---------------------------------------------: | :---------------------------------------------: |
| ![404](documentation/readme/skeleton_plane/wireframe-mobile-404.webp) | ![500](documentation/readme/skeleton_plane/wireframe-mobile-500.webp) |

</details>

<br>
<hr>

<a id="tablet-frames"></a>

#### Tablet Wireframes

<details>
<summary> Click here to see the Tablet Wireframes </summary>

|                Home page wireframe                |                Dashboard page wireframe                 |
| :-----------------------------------------------: | :-------------------------------------------------: |
| ![Home](documentation/readme/skeleton_plane/wireframe-tablet-home.webp) | ![Dashboard](documentation/readme/skeleton_plane/wireframe-tablet-dashboard.webp) |

|                   My Crate page wireframe                    |                   Record Detail page wireframe                   |
| :-------------------------------------------------------------: | :-----------------------------------------------------------: |
| ![My Crate](documentation/readme/skeleton_plane/wireframe-tablet-collection.webp) | ![Record Detail](documentation/readme/skeleton_plane/wireframe-tablet-detail.webp) |

|                400 page wireframe                |                 403 page wireframe                  |
| :-----------------------------------------------: | :-----------------------------------------------------: |
| ![Record Detail](documentation/readme/skeleton_plane/wireframe-tablet-400.webp) | ![Results](documentation/readme/skeleton_plane/wireframe-tablet-403.webp) |

|               404 page wireframe                |               500 page wireframe                |
| :---------------------------------------------: | :---------------------------------------------: |
| ![404](documentation/readme/skeleton_plane/wireframe-tablet-404.webp) | ![500](documentation/readme/skeleton_plane/wireframe-tablet-500.webp) |

 </details>

<br>
<hr>

<a id="desktop-frames"></a>

#### Desktop Wireframes

<details>
<summary> Click here to see the Desktop Wireframes </summary>

- Home page wireframe

![Home](documentation/readme/skeleton_plane/wireframe-desktop-home.webp)

- Dashboard page wireframe

![Dashboard](documentation/readme/skeleton_plane/wireframe-desktop-dashboard.webp)

- My Crate page wireframe

![My Crate](documentation/readme/skeleton_plane/wireframe-desktop-collection.webp)

- Record Detail page wireframe

![Collection](documentation/readme/skeleton_plane/wireframe-desktop-detail.webp)

- 400 page wireframe

![400](documentation/readme/skeleton_plane/wireframe-desktop-400.webp)

- 403 page wireframe

![403](documentation/readme/skeleton_plane/wireframe-desktop-403.webp)

- 404 page wireframe

![404](documentation/readme/skeleton_plane/wireframe-desktop-404.webp)

- 500 page wireframe

![500](documentation/readme/skeleton_plane/wireframe-desktop-500.webp)

 </details>

<br>
<hr>

 <a id="surface-plane"></a>

### Surface Plane

<a id="colour-scheme"></a>

#### Colour Scheme

The Vinyl Crate colour palette is inspired by the rich textures and nostalgic warmth of analogue sound — drawing from classic **record sleeves**, vintage **audio gear**, and the **glow of golden-hour light** reflecting on a turntable. This scheme balances modern clarity with retro flair, giving the app a tactile, curated feel that aligns with the essence of vinyl collecting.

The primary colours for the site are:

- `#40798c` (**Highlight Blue**) – A muted teal used consistently in headings, buttons, and hyperlinks. It adds a calm, confident tone to the interface, echoing the **cool lacquer of vintage hi-fi systems**. This colour acts as a consistent accent across the interface.
  
- `#ffb633` (**Highlight Yellow**) – A vibrant amber that evokes **sunburst vinyl**, **retro labels**, and **golden details** from 70s/80s record art. It’s used for **call-to-actions**, badges, and **hover states**. In gradients, it transitions into a richer orange to create depth and warmth.

- `#333333` (**Charcoal Footer**) – A near-black tone used for the footer and navigation elements. It provides a grounding base for content, ensuring **clear contrast** and reflecting the **sleek minimalism** of album inner sleeves and turntable platters.

- `#efefef` (**Site Background Grey**) – A soft, neutral background that keeps focus on content while evoking the **matte paper textures** of classic album inserts. It promotes readability and enhances contrast with primary accents.

- `#ffffff` (**Foreground White**) – Used for text, icons, and form elements on dark or coloured backgrounds, ensuring **clean, crisp readability** across devices.

- `linear-gradient(to bottom, #ffb633, #f7931e)` – This gradient is applied to **highlighted sections and banners**, giving them a dynamic, analog **warmth that mimics sunlight** filtering through amber vinyl.

These colours were defined as CSS variables for easy reuse and consistent application. Together, they create a cohesive, brand-forward aesthetic that reflects Vinyl Crate’s blend of nostalgia and modern utility.

> [!NOTE]
> Defined in static/css/style.css

```css
:root {
      --highlight-blue: #305F6D;
      --highlight-yellow: #ffb633;
      --contrast-orange: #f7931e;
      --footer-charcoal: #333333;
      --site-bg-grey: #efefef;
      --search-bg-grey: #e6e6e6;
      --foreground-white: #ffffff;
      --danger-red: #dc3545;
      --danger-red-hover: #a30414;
}
```

> [!NOTE]
> Contrast compliance was fully tested and reported. For full detail, see [TESTING.md](TESTING.md)

<details>
<summary>- Toggle the arrow to view the colour swatches</summary>

![Vinyl Crate Swatch Palette](documentation/readme/surface_plane/colours-swatches.webp)

</details>

<br>
<hr>

<a id="typography"></a>

#### Typography

[Google Fonts](https://fonts.google.com/) was used to import the selected fonts for the site, ensuring high-quality and accessible typography across all devices and browsers. Fonts are imported using CSS @import, with appropriate fallbacks defined for maximum cross-device compatibility.

- **Headings (h1, h2, h3):** The font [Montserrat](https://fonts.google.com/specimen/Montserrat) was chosen for its bold, geometric style that provides a clean, modern look. Its sharp edges and contemporary design help headlines stand out, giving the site a distinctive and polished visual identity while remaining easy to read.

![Montserrat Font Example](documentation/readme/surface_plane/typography-montserrat.webp)

- **Paragraphs and body text:** The font [Lato](https://fonts.google.com/specimen/Lato) was selected for body copy due to its warm, friendly tone and excellent legibility at various sizes. It complements Montserrat without competing for attention, supporting a harmonious and user-friendly reading experience throughout the site.

![Lato Font Example](documentation/readme/surface_plane/typography-lato.webp)

- Together, Montserrat and Lato provide strong typographic contrast—balancing bold headlines with highly readable body text for an accessible, modern feel.

- **Icons and UI elements:** The [Font Awesome](https://fontawesome.com/) icon library was used to support the visual interface with clear, scalable icons. These icons align stylistically with the modern fonts and enhance user experience through recognizable visual cues for actions, navigation, and social media links.

> [!NOTE]
> Defined in static/css/style.css

```css
:root {
    /************ Typography ************/
    --primary-font: "Lato", sans-serif;
    --secondary-font: "Montserrat", sans-serif;
}
```

<br>
<hr>

<a id="imagery"></a>

#### Imagery

The imagery selected for this project was chosen to resonate with vinyl collectors and DJs — the app's core audience. The carousel banners feature high-quality visuals sourced from [Adobe Stock](https://stock.adobe.com/), showcasing vinyl records, listening setups, and DJ environments to immediately immerse users in the culture and aesthetics of record collecting.

The example record covers displayed in the application were sourced from [Discogs](https://www.discogs.com/) to reflect real-world artwork and enhance authenticity. These visuals not only demonstrate how the app works but also give prospective users a sense of the interface when populated with their own collection.

Overall, the use of clean, bold, and culturally relevant imagery reinforces the platform’s purpose: celebrating analogue music collections in a modern digital format.

<br>
<hr>

<a id="features"></a>
 
### Features


**Vinyl Crate** is a full-stack web application designed to help users digitise and manage their vinyl record collections. The site provides a visually engaging and intuitive experience with the following key features:

- **User Dashboard** – A personalised view of each user’s record collection
- **Advanced Filtering and Search** – Filter by genre, year, BPM, rating, or search by title and artist
- **Detailed Record Views** – View album art, metadata, and individual track listings
- **Dynamic Forms** – Add records and tracks with inline, JavaScript-enhanced forms
- **Custom 404 & 500 Error Pages** – Clear, branded error pages to handle broken links or server issues gracefully

These features work together to streamline collection management and enhance user interaction across devices.
 
 All Pages on the website are responsive and have:
 
 - A favicon in the browser tab.
 
 <details>
 <summary> Click here to view the favicon </summary>
 
 ![favicon](documentation/readme/surface_plane/features-home-favicon.webp)
 
 </details>

#### Defensive Programming

**Defensive programming principles** have been applied throughout the site to protect functionality and ensure that only **authorised users** can access sensitive actions. Permission checks are in place to restrict admin-level tasks — such as editing or deleting system-wide content — to superusers only.

If a user attempts to access a **restricted page** or function without the appropriate permissions, they are redirected to the login page. This approach reinforces secure behaviour and improves user experience by clearly communicating access boundaries and preventing unexpected errors.

#### Footer

The footer is divided into three key sections. The first section encourages user engagement by displaying a “Join us on” heading followed by links to the site’s social media profiles, each with accessible icons. The second section provides quick links to key pages such as Home, Register, Contact, and Privacy. The final section includes copyright information and a link to the developer’s GitHub profile. The layout is fully responsive, stacking neatly on smaller screens for optimal usability across devices.

<a id="home-page-features"></a>

#### The Home Page

<details>
<summary>Click here to view the home page</summary>

![Vinyl Crate home page](documentation/readme/surface_plane/features-home.webp)

</details>

---

The Vinyl Crate homepage introduces users to the purpose of the site: a place to catalogue and celebrate their vinyl collection. It balances a welcoming aesthetic with clear direction for both new and returning users.

- **What it does:**
  - Features a carousel designed to deliver key onboarding messages and highlight the unique selling points of the app.
  - Displays a curated selection of staff-picked records to showcase site activity.
  - Introduces the concept of digitising your analogue collection.
  - Offers clear navigation to login, sign up, or explore.

- **User Benefits:**
  - Immediately communicates the site’s value proposition to record collectors and music lovers.
  - Encourages new users to join and existing users to dive into their collection.
  - Builds trust with a clean layout, bold typography, and a focus on usability.

- **Interactive Elements:**
  - Responsive navigation with login/signup for guests and dashboard access for users.
  - Carousel: Sliding panels with bold messaging about features, benefits, and how to get started.
  - Staff Picks: Interactive cards that highlight notable records from the database.
  - Dynamic header and call-to-action tailored to the user’s login state.

The homepage acts as a stylish entry point for the Vinyl Crate experience — whether you're just browsing or ready to log your latest wax addition. It introduces key features, educates through the carousel, and encourages exploration through an intuitive and visually appealing design.

<a id="dashboard-features"></a>

#### The Dashboard

<details>
<summary> Click here to view the dashboard </summary>

![Vinyl Crate dashboard view on multiple devices](documentation/readme/surface_plane/features-dashboard.webp)

</details>

---

The Vinyl Crate dashboard is the user’s personal gateway into their collection. Upon logging in, users are greeted with a streamlined view that highlights recent activity and offers quick access to key actions.

- **What it does:**
  - Automatically redirects users here after login.
  - Welcomes the user back with a personalised greeting and a summary of their crate contents.
  - Displays the latest 6 staff-picked or recently added records for inspiration and quick browsing.
  - Provides access to search, filtering, and record management options.

- **User Benefits:**
  - Offers a personalised landing space for returning users.
  - Encourages engagement by showcasing new or notable records.
  - Reduces friction in managing your collection with direct access to tools.

- **Interactive Elements:**
  - **View Crate** button redirects the user to a full list of records in their collection.
  - **Add Record** button for fast entry of new vinyl.
  - Additional **View all** button on recently added section which takes the user to their collection.
  - A card-shaped **Add Record** icon invites the user to click and begin adding a new record.
  - Clear, responsive layout optimised for desktop and mobile.

The dashboard acts as a central hub for Vinyl Crate users — helping them navigate, discover, and grow their record collection with ease.

<a id="my-crate-features"></a>

#### My Crate Page

<details>
<summary> Click here to view the My Crate page </summary>

![My Crate page showing search, filters, and record cards on multiple devices](documentation/readme/surface_plane/features-mycrate.webp)

</details>

---

The My Crate page serves as the core of the Vinyl Crate experience — a personalised dashboard where users can explore, search, and manage their full record collection.

- **What it does:**
  - Displays all records in the user’s collection as responsive, interactive cards.
  - Provides a search bar for quickly locating specific albums or artists.
  - Offers filters by genre, artist, and rating to narrow results.
  - Enables sorting by: Newest Addition, Oldest Addition, Artist (A–Z), Artist (Z–A), Title (A–Z), and Title (Z–A).
  - Includes a clear **Add Record** button to grow the collection.

- **User Benefits:**
  - Gives users complete control over how they view and organise their collection.
  - Offers quick access to edit or view details for each record.
  - Makes it easy to discover trends, favourites, and gaps in their collection.
  - Mobile-friendly design ensures a seamless experience on any device.

- **Interactive Elements:**
  - Real-time search and filter inputs update the record list based on user selections.
  - Sorting dropdown helps tailor the display to user preferences.
  - Add Record button remains easily accessible for seamless catalogue updates.
  - Each record card links directly to the full record detail view.

This page transforms the idea of a traditional record shelf into a sleek, digital experience — searchable, sortable, and built around the collector’s unique taste.

<a id="record-detail-features"></a>

#### The Record Detail Page

<details>
<summary>Click here to view the Record Detail page</summary>

![Record detail page showing cover image, metadata, and track listing](documentation/readme/surface_plane/features-record-detail.webp)

</details>

---

The Record Detail page is designed to showcase individual records with rich metadata and a full track listing, offering both aesthetic appeal and functional detail for collectors.

- **What it does:**
  - Displays a large banner using the album’s artwork to create an immersive visual header.
  - Shows key metadata including genre, release year, and user rating.
  - Lists associated tracks with position, title, duration, and optional BPM/key data.
  - Offers editing and deletion actions for the owner of the record.

- **User Benefits:**
  - Presents each record with a clean, focused layout that feels personal and polished.
  - Allows easy management of each entry with intuitive controls.
  - Helps users quickly assess the content of a record at a glance, supporting crate digging and browsing habits.

- **Interactive Elements:**
  - Back button to return to the previous page.
  - Album detail box with cover image, title, and artist.
  - Metadata cards with clear visual grouping.
  - Tracklist section styled for readability, with musical metadata.
  - Edit and delete buttons (visible only to the record owner).

This page supports in-depth cataloguing, reflecting the physical experience of pulling a record from the shelf and exploring its contents — all within a responsive, streamlined interface.

<a id="record-track-forms"></a>

#### Record and Track Forms

<details>
<summary>Click here to view the Record and Track Forms page</summary>

![Record detail page showing cover image, metadata, and track listing](documentation/readme/surface_plane/features-record-detail.webp)

</details>

---

The Record and Track forms are central to the user’s ability to create and maintain their collection, offering a seamless way to add detailed information about each vinyl entry.

- **What it does:**
  - Allows users to add or edit records with fields for title, artist, release year, genre, rating, and optional cover image.
  - Supports inline addition of track listings, each with position, title, duration, and optional BPM/key fields.
  - Enforces validation on key fields (e.g. whitespace-only titles, duration format).
  - Enables dynamic add/remove of track forms via JavaScript, with consistent indexing and deletion tracking.

- **User Benefits:**
  - Makes it easy to catalogue both high-level record data and specific track details in one intuitive interface.
  - Inline formsets allow users to build a full track list without navigating away or reloading the page.
  - Real-time error messages ensure users can correct issues before submission, improving form reliability.

- **Interactive Elements:**
  - Add and remove buttons for track forms with JavaScript-driven behaviour.
  - Validation feedback on incorrect or missing inputs (e.g. invalid durations or blank titles).
  - Smart deletion of tracks using Django’s `can_delete` handling — hidden from view but flagged for removal.
  - Dynamically rendered help text for each field to guide the user.

> *Note: Tracks are optional, allowing users to add a record entry without any associated track listings. This provides flexibility for users who wish to catalogue records gradually or with minimal detail.*

This form system balances flexibility and control, making it easy for collectors to maintain a clean, consistent archive of their vinyl library — whether adding just the basics or entering full metadata for every track.


<a id="400-page-features"></a>

#### The 400 Page

<details>
<summary>Click here to view the 400 Page</summary>

![Custom 400 page with vinyl-themed illustration and bad request message](documentation/readme/surface_plane/features-400.webp)

</details>

---

The custom 400 page gracefully handles bad requests caused by malformed or incorrect input. Rather than displaying a generic server error, it provides a polished and brand-consistent response that reassures users and helps them recover quickly.

- **What it does:**
  - Informs users that the request was invalid or could not be understood.
  - Uses a familiar vinyl-themed illustration to maintain visual consistency.
  - Includes a clear call-to-action button to return to the homepage.

- **User Benefits:**
  - Reduces confusion by presenting a friendly explanation of the issue.
  - Maintains trust by avoiding abrupt or technical error messages.
  - Helps users navigate away from error states without frustration.

- **Interactive Elements:**
  - A custom SVG image styled to match the brand identity.
  - A Bootstrap-styled button with an arrow icon for easy return to the home page.

This page reinforces Vinyl Crate’s commitment to thoughtful UX, even when things go wrong, helping users feel supported rather than stuck.

<a id="403-page-features"></a>

#### The 403 Page

<details>
<summary>Click here to view the 403 Page</summary>

![Custom 403 page with vinyl-themed illustration and access denied message](documentation/readme/surface_plane/features-403.webp)

</details>

---

The custom 403 page handles cases where a user attempts to access a restricted page without the necessary permissions. Rather than delivering a cold or technical error, this page keeps the tone friendly and aligned with the Vinyl Crate brand.

- **What it does:**
  - Clearly informs users that access to the page is forbidden.
  - Reinforces site identity using a vinyl-themed illustration.
  - Guides users back to the homepage with a prominent CTA.

- **User Benefits:**
  - Prevents frustration by explaining that the issue is permission-based.
  - Offers a visual experience that feels cohesive and intentional.
  - Helps users recover quickly with a clear path to continue browsing.

- **Interactive Elements:**
  - SVG illustration that keeps the mood light while staying on-brand.
  - A Bootstrap-styled button to return to the homepage, with a left arrow icon for clarity.

This page transforms a potentially confusing moment into a branded touchpoint, ensuring users feel guided and respected even when access is denied.

<a id="404-page-features"></a>

#### The 404 Page

<details>
<summary>Click here to view the 404 Page</summary>

![Custom 404 page with vinyl-themed illustration and return button](documentation/readme/surface_plane/features-404.webp)

</details>

---

The custom 404 page provides a friendly and branded experience for users who encounter a broken or incorrect link. Rather than showing a generic error message, it reinforces Vinyl Crate’s design personality while guiding users back to a valid route.

- **What it does:**
  - Displays a clear message that the requested page could not be found.
  - Uses a vinyl-themed illustration to keep the branding consistent.
  - Offers a single, prominent call-to-action to return to the homepage.

- **User Benefits:**
  - Prevents confusion with a clear, user-friendly explanation of the issue.
  - Maintains brand tone and visual consistency, even in error scenarios.
  - Provides an immediate path back to safety, reducing frustration.

- **Interactive Elements:**
  - Branded SVG illustration to lighten the experience.
  - Return to Home button styled with Bootstrap and an icon.

This page helps maintain trust and polish by turning an error into an opportunity to reinforce the Vinyl Crate experience.

<a id="500-page-features"></a>

#### The 500 Error Page

<details>
<summary> Click here to view the 500 error page </summary>

![Custom 500 error page with vinyl theme](documentation/readme/surface_plane/features-500.webp)

</details>

---

The Vinyl Crate 500 error page provides a calm and friendly experience when an unexpected server error occurs. With its custom visual styling and reassuring message, it ensures that even errors feel intentional and on-brand.

- **What it does:**
  - Displays a custom server error message and themed vinyl graphic.
  - Offers users a clear explanation and path to return to the homepage.
  - Automatically shown when a 500-level error is triggered.

- **User Benefits:**
  - Reduces frustration by delivering a visually appealing and human response to errors.
  - Maintains brand continuity even during service disruptions.
  - Helps users quickly navigate back to a working part of the site.

- **Interactive Elements:**
  - Vinyl-themed illustration to match the site’s tone and theme.
  - Prominent call-to-action button to return to the homepage.

The 500 page ensures Vinyl Crate remains user-friendly and stylish, even in the face of technical errors, maintaining trust and usability throughout the experience.

<br>
<hr>

<a id="dev-process"></a>

### Development Process

Vinyl Crate was developed using an **iterative, feature-driven approach**:

1. Planned the site structure, wireframes, and database schema
2. Set up the Django project with a connected PostgreSQL database
3. Implemented user authentication with Django Allauth
4. Developed core CRUD functionality for records and tracklists
5. Integrated Cloudinary for image uploads and Discogs for record metadata
6. Built dynamic filtering, search, and user dashboard features
7. Focused on accessibility, responsive design, and a clean UI
8. Completed manual and automated testing, README documentation, and deployed to Heroku

Version control was managed using **Git** and **GitHub**, with regular, descriptive commits to track progress and maintain a clear development history.

<a id="future-implementation"></a>

#### Future Implementations

To expand the functionality of Vinyl Crate and improve the user experience, the following features are being considered for future development:

1. **Dark & Light Mode (Manual & Auto Toggle)** – Introduce a theme switcher that enables users to toggle between light and dark modes, with an additional setting that respects their device’s system preference. This would improve accessibility and make the app more comfortable for use in different lighting conditions.

2. **Export Collection to CSV** – Allow users to download their vinyl collection as a `.csv` file for offline reference, backups, or importing into other applications. This supports data portability and collection management flexibility.

3. **User Profile Functionality** – Add a profile page where users can view and edit their personal information, set collection preferences, and track their activity across the app. This lays the groundwork for deeper personalization and community features.

4. **Discogs API Integration & Form Autocomplete** – Connect to the Discogs API to allow users to search for records and auto-populate fields when adding to their crate. This would speed up the submission process and improve data consistency.

5. **Social Media Sign-In Options** – Enhance account creation and login by offering OAuth-based sign-ins through Google, Facebook, or Apple. This simplifies user onboarding and provides a more seamless authentication process.

6. **Public Crate Sharing** – Let users create a public view of their vinyl collection, sharable via a link (e.g. `vinylcrate.app/username`), great for DJs and collectors.

7. **Wishlist Feature** – Allow users to build a "Want List" for records they’d like to add in the future, with possible integration to match against other users or Discogs listings.

8. **Community Comments & Crate Notes** – Add the ability to leave thoughts or mini-reviews on records, fostering a social sense of discovery and shared taste.

9. **Advanced Filtering & Tagging** – Introduce more powerful filtering options using multiple tags like sub-genres, moods, or special editions.

10. **Record Condition & Edition Info** – Allow collectors to log condition (e.g. VG, NM), pressing variant, colour vinyl, and catalogue number for more accurate collection records.

11. **Track Previews via Spotify or YouTube** – Add embedded links to sample music, where available, giving users a quick listen option before adding a record.

12. **Barcode Scanner (Mobile Only)** – Enable users to scan a barcode to look up and autofill album data via the Discogs API.

13. **Bulk Record Upload via CSV** – Provide an option for advanced users to upload large collections at once using a pre-formatted `.csv` template.

14. **Crate Backup & Sync Options** – Let users export a JSON backup of their collection, or link a Google Drive account for automated backups.

15. **Monthly Summary Emails** – Allow opt-in emails that highlight new staff picks, crate activity, or “you haven’t logged anything in a while” reminders.

These enhancements aim to enrich the Vinyl Crate experience while making it easier for users to engage with and manage their collections.

<a id="accessibility"></a>

### Accessibility

Accessibility has been a key consideration throughout the development of Vinyl Crate. Measures taken to ensure the site is inclusive and user-friendly include:

- Using semantic HTML5 elements to improve structure and navigation for assistive technologies
- Adding descriptive `alt` attributes to all meaningful images, including record covers and banners
- Applying `aria-labels` to interactive elements such as icon-only buttons and links for screen reader clarity
- Maintaining strong colour contrast across the UI, particularly in key areas like filters, buttons, and navigation (see [Colour Scheme](#colours))
- Ensuring focus states and keyboard navigability across all interactive components

Accessibility was evaluated using **Lighthouse**, **WAVE**, and manual checks in Chrome DevTools. Detailed results are available in the [TESTING.md](TESTING.md) document.

<a id="deployment-development"></a>

## Deployment & Local Development

<a id="deployment"></a>

### Deployment

The Vinyl Crate project is deployed using **Heroku**, with **Amazon RDS PostgreSQL** for the live database and **Cloudinary** for media file storage.

#### **Create the Live Database**

While `sqlite3` was used for local development, this is not suitable for production. Instead, a free-tier PostgreSQL database from Amazon AWS was used for deployment.

1. Sign in to your [Amazon RDS Console](https://console.aws.amazon.com/rds/) and click **Create Database**.
2. Select **Standard Create**, choose **PostgreSQL**, and select the **Free tier** template.
3. Set a unique DB instance identifier, master username, and password.
4. In the connectivity section, enable public access and ensure security group rules allow inbound connections from your IP.
5. Launch the database and wait for the instance to become available.
6. Once ready, copy the **Endpoint** and construct your `DATABASE_URL` in the following format:
    ```
    postgres://username:password@hostname:5432/dbname
    ```

#### **Heroku App Setup**

1. In the [Heroku Dashboard](https://dashboard.heroku.com/), click **New** → **Create new app**.
2. Name your app uniquely, select a region, and click **Create App**.
3. Go to the **Settings** tab → **Reveal Config Vars** → Add:

    - `DATABASE_URL`: paste your constructed PostgreSQL URL (no quotes)

### Preparation for Deployment in VS Code (with PostgreSQL on AWS)

1. **Install required packages**  
   Install `dj_database_url` and `psycopg2` to enable Django to connect to an external PostgreSQL database:

   ```bash
   pip3 install dj_database_url==0.5.0 psycopg2
   ```

2. **Freeze dependencies**  
   Save the installed packages to your `requirements.txt`:

   ```bash
   pip3 freeze > requirements.txt
   ```

3. **Update `settings.py`**  
   Add the following import near the top of `settings.py`:

   ```python
   import dj_database_url
   ```

4. **Temporarily connect to AWS PostgreSQL**  
   In `settings.py`, comment out the default `DATABASES` block and add the following (replace with your actual AWS RDS connection string):

   > **This is temporary and should NOT be pushed to GitHub.**

   ```python
   DATABASES = {
       'default': dj_database_url.parse('your-aws-rds-db-url-here')
   }
   ```

5. **Test connection**  
   Run the server to confirm the connection works:

   ```bash
   python3 manage.py runserver
   ```

6. **Apply migrations to AWS**  
   If successful, migrate your models to the new external database:

   ```bash
   python3 manage.py migrate
   ```

7. **Create a superuser**  
   Set up admin access on the new database:

   ```bash
   python3 manage.py createsuperuser
   ```

8. **Switch between local and external DB automatically**  
   Replace the temporary block in `settings.py` with the following conditional logic:

   ```python
   if 'DATABASE_URL' in os.environ:
       DATABASES = {
           'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
       }
   else:
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.sqlite3',
               'NAME': BASE_DIR / 'db.sqlite3',
           }
       }
   ```

9. **Install Gunicorn**  
   Add Gunicorn to serve your Django app in production:

   ```bash
   pip3 install gunicorn
   pip3 freeze > requirements.txt
   ```

10. **Create a `Procfile`**  
    In the root of your project, create a file named `Procfile` with the following line (no extension, no blank line below):

    ```Procfile
    web: gunicorn your_project_name.wsgi:application
    ```

    > Replace `your_project_name` with your actual Django project folder name (the one containing `settings.py`).

11. **Disable collectstatic on Heroku (for now)**  
    Prevent Heroku from trying to collect static files during deployment:

    ```bash
    heroku config:set DISABLE_COLLECTSTATIC=1 --app your-heroku-app-name
    ```

12. **Update allowed hosts**  
    In `settings.py`, update `ALLOWED_HOSTS` to include Heroku and local development:

    ```python
    ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'localhost']
    ```

13. **Commit and push changes**  
    Save all changes, commit, and push to GitHub:

    ```bash
    git add .
    git commit -m "Prepare for Heroku deployment with AWS DB"
    git push origin main
    ```

14. **Connect to Heroku Git and deploy**  
    Link your repo and deploy:

    ```bash
    heroku git:remote -a your-heroku-app-name
    git push heroku main
    ```

15. **Verify deployment**  
    Your site should now be live (without static files). Re-enable collectstatic and confirm static assets are served correctly.

16. **Enable automatic deploys**  
    Go to your Heroku app’s **Deploy** tab:
    - Connect your GitHub repo
    - Click **Enable Automatic Deploys**

#### **Generating a Secure SECRET_KEY & Configuring DEBUG Settings**

1. When a Django project is created, it includes a default `SECRET_KEY`. However, using this default in production poses a security risk. Instead, generate a new secure key specifically for deployment and store it safely.

2. Use a tool like the [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) to create a strong, random key. Copy the generated key.

3. In your Heroku dashboard, navigate to the app’s **Settings** tab and add a new Config Var:
   - **Key**: `SECRET_KEY`
   - **Value**: Paste your newly generated secret key

4. In your `settings.py`, update the `SECRET_KEY` definition to retrieve the value securely from the environment:

    ```python
    SECRET_KEY = os.environ.get('SECRET_KEY', ' ')
    ```

5. Update the `DEBUG` setting so it is only enabled during development:

    ```python
    DEBUG = 'DEVELOPMENT' in os.environ
    ```

6. Save your changes, then add, commit, and push them to your repository:

    ```bash
    git add .
    git commit -m "Configure SECRET_KEY and DEBUG for secure deployment"
    git push origin main
    ```

#### **Set Up Cloudinary for Media File Storage**

To handle media files (such as record cover images), this project uses [Cloudinary](https://cloudinary.com/), a cloud-based image and video management service.

---

1. Create a Cloudinary Account

- Go to [cloudinary.com](https://cloudinary.com/) and sign up for a free account.
- After logging in, navigate to the **Dashboard**.
- Copy your **Cloud name**, **API Key**, and **API Secret** – you'll need these for your environment variables.

2. Install Required Packages

    Install the required Python packages using pip:
    ```bash
    pip3 install cloudinary django-cloudinary-storage
    ```

    Then update your requirements.txt:
    ```
    pip3 freeze > requirements.txt
    ```

3. Configure Cloudinary in Django

    In your settings.py, add the following:

    Add to INSTALLED_APPS:
    ```python
    INSTALLED_APPS = [
        ...
        'cloudinary',
        'cloudinary_storage',
        ...
    ]
    ```

    Configure the default file storage:
    ```Python
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ```

    Add your Cloudinary credentials:

    These will be pulled from environment variables for security:
    ```python
    import cloudinary
    import cloudinary.uploader
    import cloudinary.api

    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
        'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
        'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
    }
    ```

4. Set Config Vars in Heroku

    Go to your app on Heroku, open the Settings tab, and add the following Config Vars:

    ```python
    CLOUDINARY_CLOUD_NAME = your_cloud_name
    CLOUDINARY_API_KEY = your_api_key
    CLOUDINARY_API_SECRET = your_api_secret
    ```

5. Use CloudinaryField in Your Models

    Your Record model (or any other models needing media upload) should use:

    ```python
    from cloudinary.models import CloudinaryField

    cover_image = CloudinaryField('image', blank=True, null=True)
    ```

Cloudinary will now automatically handle image storage, optimization, and delivery via CDN.

<a id="local-development"></a>

## Local Development

To run this project locally, you will need to fork and clone the repository, then install the required dependencies in a virtual environment.

---

<a id="fork"></a>

#### How to Fork

To create a personal copy of this repository:

1. Log in (or sign up) to [GitHub](https://github.com/).
2. Navigate to the repository: [sd-powell/vinyl-crate](https://github.com/sd-powell/portfolio_project_3).
3. Click the **Fork** button in the top-right corner of the page.

---

<a id="clone"></a>

#### How to Clone

To clone your forked repository:

1. Log in to [GitHub](https://github.com/).
2. Go to the repository for this project, [sd-powell/portfolio_project_2](https://github.com/sd-powell/portfolio_project_3).
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location where you want to clone the repository.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.
6. Set up a **virtual environment** by running:

    ```bash
    python3 -m venv env
    ```

7. Activate the virtual environment:
    - On **macOS/Linux**:  
      ```bash
      source env/bin/activate
      ```
    - On **Windows**:  
      ```bash
      env\Scripts\activate
      ```

8. Install the required packages from `requirements.txt` by running:

    ```bash
    pip3 install -r requirements.txt
    ```

---

<a id="technologies"></a>

## Technologies Used

<a id="languages"></a>

### Languages Used

- HTML
- CSS
- JavaScript
- Python

<a id="frameworks"></a>

### Frameworks, Libraries & Tools

- [Django](https://www.djangoproject.com/) – Version 4.2.20 - The main web framework used to build the application.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Version 65.8.0 - Used for authentication, registration & account management.
- [Django Environ](https://django-environ.readthedocs.io/en/latest/) – Version 0.12.0 - Used to manage environment variables from a `.env` file.
- [dj-database-url](https://pypi.org/project/dj-database-url/) – Version 0.5.0 - Simplifies database configuration with Heroku's environment.
- [Pillow](https://pillow.readthedocs.io/en/stable/) – Version 11.2.1 - Required for image handling in Django models.
- [psycopg2](https://pypi.org/project/psycopg2/) - Version 2.9.10 (Binary) - a postgres database adapter which allow us to connect with a postgres database
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) – Version 2025.4 - Used to render Django forms with Bootstrap 5 styling.
- [Bootstrap 5](https://getbootstrap.com/) – Front-end framework for responsive design.
- [Gunicorn](https://gunicorn.org/) – Version 20.1.0 - WSGI HTTP server used in production on Heroku.
- [Whitenoise](https://whitenoise.evans.io/en/stable/) – Version 6.5.0 - Used to serve static files in production.

<a id="design"></a>

### Design & Visuals

- [Balsamiq](https://balsamiq.com/) – Used to create wireframes for mobile, tablet and desktop layouts.
- [Adobe Illustrator](https://www.adobe.com/uk/products/illustrator.html) – Used to design the logo and some UI elements.
- [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html) – Used for cropping, resizing and exporting images in webp format for faster load times and modern compression.

<a id="development-tools"></a>

### Development & Deployment

- [Heroku](https://www.heroku.com/) – Cloud platform used to deploy the final version of the application.
- [Cloudinary](https://cloudinary.com/) – Used to host and deliver user-uploaded images.
- [Git](https://git-scm.com/) – For version control.
- [GitHub](https://github.com/) – Repository hosting and collaboration.
- [Pip](https://pypi.org/project/pip/) - A tool for installing Python packages.
- [Visual Studio Code](https://code.visualstudio.com/) – Primary code editor used for development.
- [Google Fonts](https://fonts.google.com/) – For custom font integration.
- [Font Awesome](https://fontawesome.com/) – Icon library for UI icons.

<a id="testing-tools"></a>

### Testing & Accessibility Tools

- [Coverage.py](https://coverage.readthedocs.io/) – Used to evaluate the effectiveness of the test suite by checking code coverage.
- [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) – For debugging and responsive testing.
- [Mobile First Plugin](https://www.webmobilefirst.com/en/) – Used to simulate how the site appears on mobile devices.
- [Aria DevTools](https://github.com/ziolko/aria-devtools) – Used to simulate screen reader accessibility.
- [Webpage Spell-Check](https://chrome.google.com/webstore/detail/webpage-spell-check/mgdhaoimpabdhmacaclbbjddhngchjik) – Chrome extension used to check for spelling errors across the site and README.

<a id="testing-readme"></a>

## Testing

> [!NOTE]
> Manual testing covered all user flows, including edge cases and JavaScript interactions. For full detail, see [TESTING.md](TESTING.md)

<a id="content"></a>

## Content

The content displayed throughout the site is based on my own personal vinyl collection. Record details such as album titles, artists, tracklists, genres, and release years were sourced from [Discogs](https://www.discogs.com/) ensuring accurate and comprehensive metadata for each entry.

All other written content — including UI text, instructions, labels, button copy, and page descriptions — was created by me to align with the app’s tone, functionality, and user experience goals.

<a id="media"></a>

### Media

- [Adobe Stock](https://stock.adobe.com/) - Used to source royalty free imagery for the site.

- User-uploaded images are handled securely and efficiently using [Cloudinary](https://cloudinary.com/), which provides scalable cloud-based image storage and delivery.

<a id="acknowledgement"></a>

### Acknowledgments

I would like to acknowledge the following people:

- [Jubril Akolade](https://github.com/Jubrillionaire) - My Code Institute Mentor.

- Ax de Klerk, Jordan Acomba & Robert Lewis - My fellow Code Institute cohort, who helped each other over the course of our milestone projects.

- The music fans in my family for helping me test my site.

- The Code Institute Slack channel Peer Code Review - Thank you to everyone who took the time to view my site and look over the code.

<br><hr>
[🔼 Back to top](#contents)