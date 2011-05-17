%define name edje_viewer
%define version 0.1.0
%define svn	20101107
%define release %mkrel 0.%svn.2

Summary:	A simple viewer for edj files
Name:		%{name}
Version:	%{version}
Release:	%release
License:	BSD
Group:		Graphics
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.enlightenment.org/
Source:		%{name}-%{version}.tar.bz2
Patch0:		edje_viewer-0.1.0-drop-invalid-cs-translation.patch
BuildRequires:	edje-devel >= 0.9.9.050, edje >= 0.9.9.050
BuildRequires:	ecore-devel >= 0.9.9.050
Buildrequires:	evas-devel >= 0.9.9.050
BuildRequires:	elementary-devel

%description
A simple viewer for edj files. Should provide more ease of use than the
edje viewer that comes with edje itself.

%prep
%setup -q -n %name-%version
%patch0 -p0

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING* README TODO
%{_bindir}/%{name}
%{_datadir}/%name
%{_datadir}/applications/%name.desktop
