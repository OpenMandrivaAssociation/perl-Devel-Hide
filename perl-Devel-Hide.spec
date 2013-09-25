%define upstream_name    Devel-Hide
%define upstream_version 0.0009

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Epoch:		1

Summary:	Forces the unavailability of specified Perl modules (for testing)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/Devel-Hide-%{upstream_version}.tar.gz

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

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1:0.0.800-2mdv2011.0
+ Revision: 653407
- rebuild for updated spec-helper

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.0.800-1mdv2011.0
+ Revision: 505729
- bump epoch
- rebuild using %%perl_convert_version

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.0008-1mdv2010.0
+ Revision: 376243
- import perl-Devel-Hide


* Fri May 15 2009 cpan2dist 0.0008-1mdv
- initial mdv release, generated with cpan2dist


