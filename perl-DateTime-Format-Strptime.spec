%define upstream_name    DateTime-Format-Strptime
%define upstream_version 1.2000

Name:    perl-%{upstream_name}
Version: %perl_convert_version %{upstream_version}
Release: %mkrel 1
Epoch:   1

Summary: Parse and format strp and strf time patterns
License: GPL+ or Artistic
Group:   Development/Perl
URL:     http://search.cpan.org/dist/%{upstream_name}
Source0: http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(DateTime)
Buildarch: noarch
BuildRoot:%{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements most of strptime(3), the POSIX function that is the
reverse of strftime(3), for DateTime. While strftime takes a DateTime and a
pattern and returns a string, strptime takes a string and a pattern and returns
the DateTime object associated.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
#%__make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/DateTime
%{_mandir}/*/*
