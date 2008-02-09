%define name edje_viewer
%define version 0.0.1
%define cvs	20080209
%define release %mkrel %cvs.1

Summary:	A simple viewer for edj files
Name:		%{name}
Version:	%{version}
Release:	%release
License:	BSD
Group:		Graphics
URL:		http://www.enlightenment.org/
Source:		%{name}-%{cvs}.tar.bz2
BuildRequires:	edje-devel edje
BuildRequires:	ecore-devel
Buildrequires:	evas-devel
BuildRequires:	etk-devel

%description
A simple viewer for edj files. Should provide more ease of use than the
edje viewer that comes with edje itself.

%prep
%setup -q -n %name

%build
./autogen.sh
%configure2_5x
%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING* README TODO
%{_bindir}/%{name}
%{_datadir}/%name/data
