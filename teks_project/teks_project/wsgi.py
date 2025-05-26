"""
WSGI config for teks_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teks_project.settings')

application = get_wsgi_application()

# Run migrations on startup in production
if os.environ.get('RUN_MIGRATIONS_ON_STARTUP', 'False') == 'True':
    # Add the project path to the Python path
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_path not in sys.path:
        sys.path.append(project_path)
    
    # Import and run the management command
    import django
    django.setup()
    
    from django.core.management import call_command
    call_command('migrate_and_seed')
