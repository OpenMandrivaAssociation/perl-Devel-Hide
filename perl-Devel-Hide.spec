%define upstream_name    Devel-Hide
%define upstream_version 0.0009

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	Forces the unavailability of specified Perl modules (for testing)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/Devel-Hide-%{upstream_version}.tar.gz

BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Given a list of Perl modules/filenames, this module makes 'require' and
'use' statements fail (no matter the specified files/modules are installed
or not).

They _die_ with a message like:

    Can't locate Module/ToHide.pm (hidden)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

