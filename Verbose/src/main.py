"""
Verbose: A Twitter competitor with unique features
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Verbose.src.settings')

application = get_wsgi_application()