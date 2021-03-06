# Copyright (c) 2009, Jurie-Jan Botha
#
# This file is part of the 'cron' Django application.
#
# 'cron' is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# 'cron' is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with the 'cron' application. If not, see
# <http://www.gnu.org/licenses/>.


from django.http import HttpResponse
from cron import cron


def start(request):
    cron.start()
    return HttpResponse('Cron Thread Started')

def stop(request):
    cron.stop()
    return HttpResponse('Cron Thread Stopped')
