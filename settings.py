#  This file is part of TxtAlert.
#
#  TxtALert is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  TxtAlert is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with TxtAlert.  If not, see <http://www.gnu.org/licenses/>.


from config import *


PROJECT_NAME = 'txtalert'

SECRET_KEY = ''

TEMPLATE_DEBUG = DEBUG

TEST_DATABASE_CHARSET = 'utf8'

ADMINS = (
    ('Joe Developer', 'a@b.xyz'),
)

MANAGERS = ADMINS

SERVER_EMAIL = 'a@b.xyz'

EMAIL_SUBJECT_PREFIX = '[TxtAlert] '
EMAIL_HOST = 'smtp.somehost.xyz'
EMAIL_PORT = 25
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'email_user'
EMAIL_HOST_PASSWORD = 'email_user_password'

TIME_ZONE = 'Africa/Johannesburg'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True

MEDIA_ROOT = '/home/django/' + ENVIRONMENT + '/projects/' + PROJECT_NAME + '/webroot/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_DIRS = (
    '/home/django/' + ENVIRONMENT + '/projects/' + PROJECT_NAME + '/templates',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'general.settings',
    'general.cron',
    'general.jquery',
    'mobile.sms',
    'therapyedge',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
)