# RealHome - Real Estate Listing Website

## Project Overview

RealHome is a Django-based real estate listing website currently under development. It aims to provide a platform for users to browse, search, and list properties for sale or rent.

## Current Status

The project is in its initial development phase. Basic models and templates have been set up, and we're working on implementing core functionalities.

## Features (Planned/In Progress)

- User authentication (registration, login, logout)
- Property listing creation and management
- Property search functionality
- Image uploads for property listings
- Responsive design for mobile and desktop

## Tech Stack

- Python 3.8+
- Django 3.2+
- HTML/CSS for frontend
- SQLite (development database)

## Project Structure

```
realhome/
│
├── realhome/             # Project configuration
├── main/                 # Main application
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   └── urls.py           # URL patterns
├── templates/            # HTML templates
├── static/               # Static files (CSS, JS, images)
└── manage.py             # Django management script
```

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/realhome.git
   cd realhome
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Access the site at `http://127.0.0.1:8000`

## Next Steps

- Implement user authentication views and templates
- Create forms for property listing submission
- Develop the property search functionality
- Design and implement the frontend user interface
