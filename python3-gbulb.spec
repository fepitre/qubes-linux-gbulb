%define mod_name gbulb
%define debug_package %{nil}

Name:           python-%{mod_name}
Version:        0.6.0
Release:        2%{?dist}
Url:            http://github.com/nathan-hoad/gbulb
Summary:        GLib event loop for asyncio (PEP 3156)
License:        Apache-2.0
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/0f/99/eab240dcf5fd7f8d86017d5c04147e0d93c29bbc56d8c0394bf090f34e4e/%{mod_name}-%{version}.tar.gz
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{mod_name}}

%description
Gbulb is a python library that implements a PEP 3156 interface for the GLib
main event loop. It is designed to be used together with the tulip reference
implementation.

%package -n python%{python3_pkgversion}-gbulb
Summary:        GLib event loop for asyncio (PEP 3156)

%description -n python%{python3_pkgversion}-gbulb
Gbulb is a python library that implements a PEP 3156 interface for the GLib
main event loop. It is designed to be used together with the tulip reference
implementation.

%prep
%setup -q -n %{mod_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-gbulb
%doc AUTHORS.rst README.md CHANGELOG.md examples 
%{python3_sitelib}/%{mod_name}*

%changelog
