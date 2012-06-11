# Refer to this file as an example to create your own settings_local.py file

DB_PATH        = '/Users/203683/projects/employeeware/db/'
TEMPLATES_PATH = "/Users/203683/projects/employeeware/templates/"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DB_PATH + 'orgchartapp.db',  # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'y%f!#uy%x2($v95j^^rfqf@8&amp;#o&amp;%=&amp;-5xbt$cd-830r!stc@9'
