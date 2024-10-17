%define src_name xpyb

Name:		python-xcb
Version:	1.3.1
Release:	1

Summary:	X Python Binding, based on the X C Binding (XCB) library
Group:		Development/Python
License:	Public Domain
URL:		https://xcb.freedesktop.org/XcbPythonBinding/
Source0:	http://xcb.freedesktop.org/dist/xpyb-%{version}.tar.bz2
Patch0:		xpyb-1.2-link.patch
BuildRequires:	libxcb-devel
BuildRequires:	python-devel

Provides: %{src_name} = %version-%release

%description
The Python binding for XCB allows the X protocol to be accessed directly from
Python. There are two components:

- A Python extension written in C. This exposes XCB-specific objects and
  library functions, as well as providing various base classes used by the
  generated code.
- Python modules which are generated directly from the XCB-XML protocol
  descriptions.

The Python binding requires libxcb.so to work. The additional extension
libraries are not required.

%prep
%setup -q -n %{src_name}-%{version}
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std


%files
%{_libdir}/pkgconfig/%{src_name}.pc
%{py_platsitedir}/*
%{_docdir}/%{src_name}

