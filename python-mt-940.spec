Name:		python-mt-940
Version:	4.30.0
Release:	2
Summary:	A library to parse MT940 files and returns smart Python collections for
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/mt-940/
Source0:	mt-940-4.30.0.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
A library to parse MT940 files and returns smart Python collections for.

%files
%{py_sitedir}/*
