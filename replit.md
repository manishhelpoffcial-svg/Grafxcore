# GrafxCore Agency Website

## Overview

GrafxCore is a creative agency website showcasing graphic design and video editing services. The application uses a Flask (Python) backend that serves static HTML/CSS/JavaScript frontend pages. The site includes a public-facing portfolio, about page, and contact form, along with an admin panel for managing portfolio items and viewing customer inquiries.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python) - lightweight web framework serving as a static file server
- **Entry Point**: `main.py` at root level serves files from `Grafxcore-V1zip/agency-site/`
- **Secondary Backend**: `Grafxcore-V1zip/main.py` contains extended functionality including:
  - PostgreSQL database connection using `psycopg2`
  - Admin authentication with hardcoded credentials
  - API endpoints for inquiries

### Frontend Architecture
- **Structure**: Multi-page static site with separate HTML files per page
- **Pages**:
  - Home (`index.html`) - Landing page with hero section
  - About (`about.html`) - Company information and stats
  - Portfolio (`wpage.html`) - Filterable work showcase
  - Contact (`ct.html`) - Contact form with API submission
  - Admin (`admin.html`) - Portfolio and inquiry management
- **Styling**: Page-specific CSS files (`style.css`, `ct.css`, `wpage.css`, `admin.css`)
- **JavaScript**: Vanilla JS for interactivity (`script.js`, `ct.js`, `wpage.js`, `admin.js`)
- **Design System**: CSS custom properties for consistent theming
  - Primary color: Emerald green (`#10b981`)
  - Font: Inter (Google Fonts)

### Data Storage
- **Portfolio Items**: Currently stored in browser `localStorage` as JSON
  - Managed through admin panel (add/delete operations)
  - Data is client-side only, not shared across devices
- **Database**: PostgreSQL connection configured via `DATABASE_URL` environment variable
  - Used for storing contact form inquiries
  - Connection handled with `psycopg2` and `RealDictCursor`

### Key Design Decisions

1. **Dual Entry Points**: Two `main.py` files exist - root level for simple serving, nested one for extended features
   - Pro: Separation of concerns between simple static serving and backend logic
   - Con: Can cause confusion about which file is active

2. **Client-Side Portfolio Storage**: Using localStorage instead of database
   - Pro: No database setup required for portfolio, works offline
   - Con: Data is per-browser, not persistent across users/devices
   - **Recommendation**: Migrate to PostgreSQL for production use

3. **Hardcoded Admin Credentials**: Authentication uses constants in Python file
   - Pro: Simple implementation
   - Con: Security risk, not suitable for production

4. **Static File Serving Pattern**: Flask primarily serves pre-built HTML
   - Pro: Simple deployment, minimal server logic
   - Con: Limited dynamic content generation

## External Dependencies

### Backend
- **Flask**: Web framework for Python
- **psycopg2**: PostgreSQL database adapter
- **PostgreSQL**: Database (configured via `DATABASE_URL` environment variable)

### Frontend (CDN)
- **Google Fonts**: Inter font family
- **Font Awesome 6.5.0**: Icon library
- **No JavaScript frameworks**: Vanilla JS only

### Environment Variables
- `DATABASE_URL`: PostgreSQL connection string (required for inquiry storage)