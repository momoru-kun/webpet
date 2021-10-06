from webpet.application import ASGIApplication
from webpet.conf import Configuration

from router import router

import os

BASE_DIR = os.getcwd() + '/'

# Define configuration
configuration = Configuration()
configuration.router = router
configuration.templates_dir = BASE_DIR + 'templates/'

# Create instance
app = ASGIApplication()
