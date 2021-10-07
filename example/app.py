from webpet.application import ASGIApplication
from webpet.conf import Configuration
from webpet.middleware import XFrameOptionsMiddleware


from router import router

import os


BASE_DIR = os.getcwd() + '/'

# Define configuration
configuration = Configuration()
configuration.router = router
configuration.templates_dir = BASE_DIR + 'templates/'
configuration.middleware = [XFrameOptionsMiddleware()]

# Create instance
app = ASGIApplication()
