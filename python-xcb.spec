%define src_name xpyb

Name:    python-xcb
Version: 1.2
Release: %mkrel 2

Summary:   X Python Binding, based on the X C Binding (XCB) library
Group:     Development/Python
License:   Public Domain
URL:       http://xcb.freedesktop.org/XcbPythonBinding/
BuildRoot: %{_tmppath}/%{src_name}-root
Source:    http://xcb.freedesktop.org/dist/xpyb-%{version}.tar.bz2

BuildRequires: x11-proto-devel
%py_requires -d

Provides: %{src_name}

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

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/pkgconfig/%{src_name}.pc
%{py_platsitedir}/*
%{_docdir}/%{src_name}

