%define name edje_viewer
%define version 0.0.1
%define release %mkrel 1


Summary:	A simple viewer for edj files
Name:		%{name}
Version:	%{version}
Release:	%release
License: BSD
Group:		Toys
URL: http://www.enlightenment.org/
Source: %{name}-%{version}.tar.bz2
BuildRequires: edje-devel >= 0.5.0.038, ecore-devel >= 0.9.9.038
Buildrequires: edje >= 0.5.0.038
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
A simple viewer for edj files. Should provide more ease of use than the
edje viewer that comes with edje itself.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
%configure2_5x
make

%install
%makeinstall

#%post -p /sbin/ldconfig
#%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING* INSTALL README doc/*
%{_bindir}/%{name}
