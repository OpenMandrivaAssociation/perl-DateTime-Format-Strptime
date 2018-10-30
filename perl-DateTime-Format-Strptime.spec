%define upstream_name    DateTime-Format-Strptime
%define upstream_version 1.51

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	14
Epoch:		1

Summary:	Parse and format strp and strf time patterns
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(DateTime)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements most of strptime(3), the POSIX function that is the
reverse of strftime(3), for DateTime. While strftime takes a DateTime and a
pattern and returns a string, strptime takes a string and a pattern and returns
the DateTime object associated.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
#make test

%files 
%doc Changes README
%{perl_vendorlib}/DateTime
%{_mandir}/*/*

%changelog
* Fri Jun 01 2012 Götz Waschk <waschk@mandriva.org> 1:1.510.0-1mdv2012.0
+ Revision: 801779
- update build deps
- update to new version 1.51

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1:1.500.0-2
+ Revision: 681391
- mass rebuild

* Fri Dec 24 2010 Götz Waschk <waschk@mandriva.org> 1:1.500.0-1mdv2011.0
+ Revision: 624459
- new version
- update source URL

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.400.0-1mdv2011.0
+ Revision: 553118
- update to 1.4000

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.200.0-1mdv2010.1
+ Revision: 526437
- update to 1.2000

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.100.0-1mdv2010.0
+ Revision: 398894
- forgot to commit new tarball
- update to 1.1000

* Tue Jul 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.90.100-1mdv2010.0
+ Revision: 393105
- update to 1.0901
- using %%perl_convert_version
- fixed license field

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0900-1mdv2010.0
+ Revision: 383958
- update to new version 1.0900

* Mon Sep 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0800-1mdv2009.0
+ Revision: 289465
- 1.0800

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Nov 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0702-1mdv2008.1
+ Revision: 105822
- import perl-DateTime-Format-Strptime


* Sun Nov 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0702-1mdv2008.1
- first mdv release 
