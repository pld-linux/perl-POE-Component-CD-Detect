#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-CD-Detect
Summary:	POE::Component::CD::Detect - detects CD insertions and provides TOC
Summary(pl):	POE::Component::CD::Detect - wykrywanie w³o¿enia CD i odczytanie TOC
Name:		perl-POE-Component-CD-Detect
Version:	1.1
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	92b8377a52c3a67e9084c51ba9c2cdf2
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-POE >= 0.22
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This POE component detects the insertion of a CD into a given drive and
issues a callback to the caller with the disc's table of contents.

%description -l pl
Ten komponent POE wykrywa fakt w³o¿enia p³yty CD do danego napêdu i
wywo³uje funkcjê callback podan± przy wywo³aniu przekazuj±c spis
zawarto¶ci p³yty (TOC).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%{perl_vendorlib}/%{pdir}/Component/CD/*.pm
%{_mandir}/man3/*
