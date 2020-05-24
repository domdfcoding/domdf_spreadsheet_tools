# This file is managed by `git_helper`. Don't edit it directly
# Copyright (C) 2018-2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# This script based on https://github.com/rocky/python-uncompyle6/blob/master/__pkginfo__.py

import pathlib

__all__ = [
		"__copyright__",
		"__version__",
		"modname",
		"pypi_name",
		"py_modules",
		"entry_points",
		"__license__",
		"short_desc",
		"author",
		"author_email",
		"github_username",
		"web",
		"github_url",
		"project_urls",
		"repo_root",
		"long_description",
		"install_requires",
		"extras_require",
		"classifiers",
		"keywords",
		"import_name",
		]

__copyright__ = """
2018-2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
"""

__version__ = "0.1.4"

modname = "domdf_spreadsheet_tools"
pypi_name = "domdf_spreadsheet_tools"
import_name = "domdf_spreadsheet_tools"
py_modules = ['domdf_spreadsheet_tools']
entry_points = {
		"console_scripts": []
		}

__license__ = "GNU Lesser General Public License v3 or later (LGPLv3+)"

short_desc = "Tools for creating and formatting spreadsheets with Python and OpenPyXL"

__author__ = author = "Dominic Davis-Foster"
author_email = "dominic@davis-foster.co.uk"
github_username = "domdfcoding"
web = github_url = f"https://github.com/domdfcoding/domdf_spreadsheet_tools"
project_urls = {
		"Documentation": f"https://domdf_spreadsheet_tools.readthedocs.io",  # TODO: Make this link match the package version
		"Issue Tracker": f"{github_url}/issues",
		"Source Code": github_url,
		}

repo_root = pathlib.Path(__file__).parent

# Get info from files; set: long_description
long_description = (repo_root / "README.rst").read_text().replace("0.1.4", __version__) + '\n'
conda_description = """Tools for creating and formatting spreadsheets with Python and OpenPyXL


Before installing please ensure you have added the following channels: domdfcoding, conda-forge"""
__all__.append("conda_description")

install_requires = (repo_root / "requirements.txt").read_text().split('\n')
extras_require = {'all': []}

classifiers = [
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
		'Operating System :: OS Independent',
		'Development Status :: 4 - Beta',
		'Programming Language :: Python :: Implementation :: CPython',
		'Programming Language :: Python :: Implementation :: PyPy',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3 :: Only',
		'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',

		]

keywords = ""