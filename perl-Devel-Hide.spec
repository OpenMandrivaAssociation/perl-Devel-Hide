
%define realname   Devel-Hide
%define version    0.0008
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Forces the unavailability of specified Perl modules (for testing)
Source:     http://www.cpan.org/modules/by-module/Devel/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

%description
Given a list of Perl modules/filenames, this module makes 'require' and
'use' statements fail (no matter the specified files/modules are installed
or not).

They _die_ with a message like:

    Can't locate Module/ToHide.pm (hidden)

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


