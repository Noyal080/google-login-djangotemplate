
# Django Project with Google OAuth and Templates
This is a Django project that demonstrates user authentication using Google OAuth and displays using Django templates.

## Requirements

-   Python 3.8+
-   Django 3.2+
-   pip (Python package installer)
-   Google Developer Console account

## Setup

### 1. Clone the repository
    git clone https://github.com/Noyal080/google-login-djangotemplate.git                                                  
    cd /google-login-djangotemplate
    
### 2. Create a virtual environment and activate it
#### In git bash
    python -m venv .venv
    source .venv/Source/activate 
#### In Windows cmd
    python -m venv .venv
    .venv\Scripts\activate

### 3. Install dependencies
    pip install -r requirements.txt

### 4. Set up Google OAuth

1.  Go to the <a href="https://console.cloud.google.com/"> Google Developer Console <a>.
2.  Create a new project.
3.  Enable the "Google+ API" for your project.
4.  Create OAuth 2.0 credentials.
5.  Add the authorized redirect URI (e.g., `http://localhost:8000/accounts/google/login/callback/`).
6.  Copy the Client ID and Client Secret.

### 5. Apply migrations and create a superuser
`python manage.py migrate`
`python manage.py createsuperuser` 

### 6. Run the server
`python manage.py runserver`
