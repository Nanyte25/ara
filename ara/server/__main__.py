#!/usr/bin/env python
#  Copyright (c) 2019 Red Hat, Inc.
#
#  This file is part of ARA Records Ansible.
#
#  ARA is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ARA is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with ARA.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

from ara.setup.exceptions import MissingDjangoException


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ara.server.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise MissingDjangoException

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
