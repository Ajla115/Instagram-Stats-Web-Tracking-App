# InstaMetrics — Instagram Stats Web Tracking App

A full-stack web application for tracking Instagram account statistics, researching hashtags, and sending automated direct messages across Instagram, Facebook, and WhatsApp.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | PHP 7.4+ with [Flight](https://flightphp.com/) microframework |
| Frontend | Next.js 14 + React 18 + Material-UI (MUI) 5 |
| Database | MySQL 8.0 |
| Automation Scripts | Python 3.8+ with Selenium & Instaloader |
| Auth | JWT (Firebase JWT library) |
| Email | PHPMailer + SMTP |

---

## Prerequisites

Before setting up the project, make sure you have:

- **PHP** 7.4 or higher
- **Composer** (PHP dependency manager)
- **Node.js** 18 or higher + npm
- **MySQL** 8.0 or higher
- **Python** 3.8 or higher + pip
- **Google Chrome** + matching [ChromeDriver](https://chromedriver.chromium.org/downloads) (for Python Selenium scripts)

---

## Project Structure

```
Instagram-Stats-Web-Tracking-App/
├── backend/
│   └── rest/
│       ├── dao/              # Data Access Objects (DB queries)
│       ├── routes/           # API endpoint definitions
│       │   ├── UserRoutes.php
│       │   ├── InstaAccRoutes.php
│       │   ├── DmRoutes.php
│       │   └── HashtagRoutes.php
│       ├── services/         # Business logic
│       ├── docs/             # Swagger API docs
│       ├── index.php         # Backend entry point
│       └── swagger.json      # OpenAPI spec
├── frontend/
│   ├── public/               # Static assets
│   └── src/
│       ├── components/       # Reusable UI components
│       ├── contexts/         # React context (auth)
│       ├── pages/            # Next.js pages/routes
│       ├── sections/         # Page section components
│       └── theme/            # MUI theme config
├── scripts/                  # Python automation scripts
├── vendor/                   # PHP Composer dependencies (auto-generated)
├── SDP_Project_New.sql       # Original database schema
├── novaBaza.sql              # Latest database schema (use this one)
├── config_example.php        # PHP config template → copy to config.php
├── .env.example              # Python/env vars template → copy to .env
├── composer.json             # PHP dependencies
└── package.json              # Root package config
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repo-url>
cd Instagram-Stats-Web-Tracking-App
```

### 2. Environment Variables

Copy the example files and fill in your credentials:

```bash
# Python .env (Instagram credentials + DB credentials for scripts)
cp .env.example .env

# PHP config (DB, JWT, SMTP)
cp config_example.php config.php
```

**`.env`** — fill in all values:
```env
IGUSERNAME1=your_instagram_username
IGPASSWORD1=your_instagram_password

IGUSERNAME2=second_instagram_username   # optional second account
IGPASSWORD2=second_instagram_password

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=sdp_project
```

**`config.php`** — fill in all values:
```
DB_HOST     → localhost
DB_USERNAME → root
DB_PASSWORD → your_mysql_password
DB_SCHEME   → sdp_project
DB_PORT     → 3306

JWT_SECRET  → any long random string (32+ characters)

SMTP_HOST     → smtp.gmail.com (or your provider)
SMTP_USERNAME → your_email@gmail.com
SMTP_PASSWORD → your_email_app_password
SMTP_PORT     → 587
EMAIL1        → your_email@gmail.com
```

### 3. Database Setup

Create the database and import the schema:

```bash
mysql -u root -p -e "CREATE DATABASE sdp_project;"
mysql -u root -p sdp_project < novaBaza.sql
```

> Use `novaBaza.sql` — it includes all tables (Instagram, Facebook, WhatsApp).

### 4. Backend Setup (PHP)

```bash
composer install
```

This installs Flight, Firebase JWT, PHPMailer, and other PHP dependencies into `vendor/`.

To serve the backend locally (built-in PHP server):
```bash
php -S localhost:8080 -t backend/rest
```

Or configure Apache/Nginx to point to `backend/rest/index.php`.

### 5. Frontend Setup (Next.js)

```bash
cd frontend
npm install
```

### 6. Python Scripts Setup

```bash
cd scripts
python -m venv venv
source venv/bin/activate      # macOS/Linux
# venv\Scripts\activate       # Windows

pip install mysql-connector-python selenium instaloader python-dotenv
```

Download [ChromeDriver](https://chromedriver.chromium.org/downloads) matching your Chrome version and update the `Service(executable_path=...)` path in whichever script you run.

---

## Running the App

### Backend
```bash
php -S localhost:8080 -t backend/rest
```

### Frontend
```bash
cd frontend
npm run dev
```
Open [http://localhost:3000](http://localhost:3000).

### Python Scripts
```bash
cd scripts
source venv/bin/activate
python <script_name>.py
```

---

## API Endpoints

All endpoints (except `/login` and `/register`) require a JWT `Authorization: Bearer <token>` header.

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/login` | Login, returns JWT token |
| POST | `/register` | Register new user |
| GET | `/connection-check` | Database connection check |

### Instagram Accounts
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/accounts` | Add an Instagram account |
| POST | `/accounts/{username}` | Add account by username |
| GET | `/accounts` | Get all accounts for logged-in user |
| DELETE | `/accounts/{id}` | Remove an account |

### Direct Messages
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/dm` | Schedule a direct message |
| GET | `/dms` | Get DM history |
| PUT | `/dms/{id}` | Update DM status |
| DELETE | `/dms/{id}` | Cancel a DM |

### Hashtags
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/hashtags` | Get all active hashtags |
| GET | `/accountsperhashtag/{id}` | Count accounts for a hashtag |
| GET | `/accountsdataperhashtag/{id}` | Get account data for a hashtag |
| DELETE | `/accounts/{id}` | Remove account from hashtag |

Full Swagger documentation is available at `backend/rest/swagger.json`.

---

## Database Schema

Database name: `sdp_project`

| Table | Description |
|-------|-------------|
| `users` | App user accounts with email, hashed password, activation tokens |
| `instagram_accounts` | Tracked IG profiles: username, followers, posts, followings, last scraped date |
| `instagram_hashtags` | Hashtags being tracked, with active/deleted status |
| `accounts_with_hashtag` | Junction: links Instagram accounts to hashtags |
| `users_accounts` | Junction: links app users to their tracked IG accounts |
| `users_hashtags` | Junction: links app users to their tracked hashtags |
| `users_dms` | Scheduled/sent Instagram DMs with status (Scheduled/Sent/Failed) |
| `facebook_accounts` | Facebook accounts to send messages to |
| `facebook_dms` | Scheduled/sent Facebook DMs |
| `users_emails` | Email notification queue |

---

## Python Scripts

All scripts read credentials from `.env` via `python-dotenv`. Make sure `.env` is populated before running.

| Script | Description | How to Run |
|--------|-------------|------------|
| `profile_scrapping_instaloader_database.py` | Scrapes Instagram profile stats (followers, posts, followings) using Instaloader and updates the DB | `python profile_scrapping_instaloader_database.py` |
| `hashtags.py` | Selenium-based scraper that finds Instagram accounts posting under tracked hashtags and stores them in the DB | `python hashtags.py` |
| `hashtags_scrapping_with_functions.py` | Refactored hashtag scraper; prompts for a hashtag name and scrapes 10 accounts from it | `python hashtags_scrapping_with_functions.py` |
| `automatic_dms4.py` | Reads scheduled DMs from DB and sends them via Instagram using Selenium | `python automatic_dms4.py` |
| `send_dms_parallel.py` | Sends DMs via two parallel Chrome sessions (two IG accounts simultaneously) | `python send_dms_parallel.py` |
| `send_dms_parallel_functions.py` | Function-based version of parallel DM sender | `python send_dms_parallel_functions.py` |
| `threads_instagram.py` | Multi-threaded Instagram DM sender with port management for concurrent sessions | `python threads_instagram.py` |
| `threads_fb.py` | Multi-threaded Facebook Messenger automation | `python threads_fb.py` |
| `schedule_ig_dms.py` | Sets all pending Instagram DMs to "Scheduled" status in DB | `python schedule_ig_dms.py` |
| `schedule_fb_dms.py` | Sets all pending Facebook DMs to "Scheduled" status in DB | `python schedule_fb_dms.py` |
| `whatsapp_dms.py` | Sends messages via WhatsApp Web using Selenium | `python whatsapp_dms.py` |
| `whatsapp_parallel_dms.py` | Parallel WhatsApp messaging using threading | `python whatsapp_parallel_dms.py` |

> **Note:** Selenium scripts require ChromeDriver. Update the `Service(executable_path=...)` in each script to point to your local ChromeDriver binary.

---

## Features

- **Account Tracking** — Add Instagram accounts and track their followers, post count, and followings over time
- **Hashtag Research** — Track hashtags and discover which accounts post under them
- **Automated DMs** — Schedule and send direct messages to Instagram accounts automatically
- **Multi-Platform Messaging** — DM automation for Instagram, Facebook Messenger, and WhatsApp
- **Parallel Sending** — Send DMs from multiple accounts simultaneously using threading
- **User Authentication** — JWT-based login with email verification and password recovery
- **Admin Dashboard** — Data visualizations with charts (ApexCharts) and data tables
- **Two-Factor Authentication** — TOTP-based 2FA support
- **DM Status Tracking** — Track message status: Scheduled → Sent / Failed to Send

---

## Security Notes

- Never commit `config.php` or `.env` — they are in `.gitignore`
- All DB passwords and credentials must be stored in environment variables only
- JWT secret should be a long, random string (32+ characters)
- Instagram/Facebook automation scripts operate against platform ToS — use responsibly and only on accounts you own
