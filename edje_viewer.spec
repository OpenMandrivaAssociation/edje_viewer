%define svn 76819

Summary:	A simple viewer for edj files
Name:		edje_viewer
Version:	1.1.0
Release:	0.%{svn}.1
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source:		%{name}-%{version}.%{svn}.tar.xz
Patch0:		edje_viewer-fix-desktop-file.patch
BuildRequires:	edje
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(ecore-file)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(elementary)
Buildrequires:	pkgconfig(evas)
Buildrequires:	pkgconfig(eweather)

%description
A simple viewer for edj files. Should provide more ease of use than the
edje viewer that comes with edje itself.

%prep
%setup -q -n %{name}-%{version}.%{svn}
%patch0 -p1

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING* README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.1.0-0.20101107.2mdv2011.0
+ Revision: 675858
- drop invalide cs translation from desktop file

* Mon Jan 03 2011 Crispin Boylan <crisb@mandriva.org> 0.1.0-0.20101107.1mdv2011.0
+ Revision: 627837
- Rebuild, update tarball

* Sun Jul 25 2010 Funda Wang <fwang@mandriva.org> 0.1.0-0.20100720.1mdv2011.0
+ Revision: 558263
- new snapshot

* Sat Aug 08 2009 Funda Wang <fwang@mandriva.org> 0.1.0-0.20090807.1mdv2010.0
+ Revision: 411567
- new snapshot based on elementary

* Wed Jul 08 2009 Funda Wang <fwang@mandriva.org> 0.0.1-20090227.3mdv2010.0
+ Revision: 393571
- rebuild

* Tue Mar 03 2009 Antoine Ginies <aginies@mandriva.com> 0.0.1-20090227.2mdv2009.1
+ Revision: 347946
- add missing files
- fix %%setup
- SVN SNAPSHOT 20090227, release 0.0.1

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.0.1-20080209.2mdv2009.0
+ Revision: 266613
- rebuild early 2009.0 package (before pixel changes)

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.0.1-20080209.1mdv2009.0
+ Revision: 167863
- fix no-buildroot-tag

* Sat Feb 09 2008 Austin Acton <austin@mandriva.org> 0.0.1-20080209.1mdv2008.1
+ Revision: 164534
- cvs checkout
- tidy spec

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 29 2007 Antoine Ginies <aginies@mandriva.com> 0.0.1-1mdv2008.0
+ Revision: 32298
- CVS snapshot 20070526, adjust buildrequires
- Import edje_viewer

