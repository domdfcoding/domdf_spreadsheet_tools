=========================
domdf_spreadsheet_tools
=========================

.. start short_desc

**Tools for creating and formatting spreadsheets with Python and OpenPyXL 🐍 🛠️**

.. end short_desc
.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |travis| |actions_windows| |actions_macos| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| image:: https://img.shields.io/readthedocs/domdf_spreadsheet_tools/latest?logo=read-the-docs
	:target: https://domdf_spreadsheet_tools.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/domdfcoding/domdf_spreadsheet_tools/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/domdf_spreadsheet_tools/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |travis| image:: https://img.shields.io/travis/com/domdfcoding/domdf_spreadsheet_tools/master?logo=travis
	:target: https://travis-ci.com/domdfcoding/domdf_spreadsheet_tools
	:alt: Travis Build Status

.. |actions_windows| image:: https://github.com/domdfcoding/domdf_spreadsheet_tools/workflows/Windows%20Tests/badge.svg
	:target: https://github.com/domdfcoding/domdf_spreadsheet_tools/actions?query=workflow%3A%22Windows+Tests%22
	:alt: Windows Tests Status

.. |actions_macos| image:: https://github.com/domdfcoding/domdf_spreadsheet_tools/workflows/macOS%20Tests/badge.svg
	:target: https://github.com/domdfcoding/domdf_spreadsheet_tools/actions?query=workflow%3A%22macOS+Tests%22
	:alt: macOS Tests Status

.. |requires| image:: https://requires.io/github/domdfcoding/domdf_spreadsheet_tools/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/domdf_spreadsheet_tools/requirements/?branch=master
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/domdf_spreadsheet_tools?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/domdf_spreadsheet_tools
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/domdf_spreadsheet_tools
	:target: https://pypi.org/project/domdf_spreadsheet_tools/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/domdf_spreadsheet_tools?logo=python&logoColor=white
	:target: https://pypi.org/project/domdf_spreadsheet_tools/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/domdf_spreadsheet_tools
	:target: https://pypi.org/project/domdf_spreadsheet_tools/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/domdf_spreadsheet_tools
	:target: https://pypi.org/project/domdf_spreadsheet_tools/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/domdf_spreadsheet_tools?logo=anaconda
	:target: https://anaconda.org/domdfcoding/domdf_spreadsheet_tools
	:alt: Conda - Package Version

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/domdf_spreadsheet_tools?label=conda%7Cplatform
	:target: https://anaconda.org/domdfcoding/domdf_spreadsheet_tools
	:alt: Conda - Platform

.. |license| image:: https://img.shields.io/github/license/domdfcoding/domdf_spreadsheet_tools
	:target: https://github.com/domdfcoding/domdf_spreadsheet_tools/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/domdf_spreadsheet_tools
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/domdf_spreadsheet_tools/v0.1.6
	:target: https://github.com/domdfcoding/domdf_spreadsheet_tools/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/domdf_spreadsheet_tools
	:target: https://github.com/domdfcoding/domdf_spreadsheet_tools/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. |pre_commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
	:target: https://github.com/pre-commit/pre-commit
	:alt: pre-commit

.. end shields


Installation
----------------

.. start installation

``domdf_spreadsheet_tools`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install domdf_spreadsheet_tools

To install with ``conda``:

	* First add the required channels

	.. code-block:: bash

		$ conda config --add channels http://conda.anaconda.org/domdfcoding
		$ conda config --add channels http://conda.anaconda.org/conda-forge

	* Then install

	.. code-block:: bash

		$ conda install domdf_spreadsheet_tools

.. end installation
