#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	GSSAPI
Summary:	GSSAPI - Perl extension providing access to the GSSAPIv2 library
Summary(pl.UTF-8):	GSSAPI - rozszerzenie Perla dające dostęp do biblioteki GSSAPIv2
Name:		perl-GSSAPI
Version:	0.28
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AG/AGROLMS/GSSAPI-%{version}.tar.gz
# Source0-md5:	65f00a0749212af064289c8a05e59b3f
URL:		http://search.cpan.org/dist/GSSAPI/
BuildRequires:	heimdal-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module gives access to the routines of the GSSAPI library, as
described in RFC 2743 and RFC 2744 and implemented by the Kerberos-1.2
distribution from MIT.

%description -l pl.UTF-8
Ten moduł daje dostęp do funkcji bibliotecznych GSSAPI określonych
przez RFC 2743 i RFC 2744 i zaimplementowanych przez MIT w dystrybucji
Kerberos-1.2.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/GSSAPI.pm
%dir %{perl_vendorarch}/GSSAPI
%{perl_vendorarch}/GSSAPI/*.pm
%dir %{perl_vendorarch}/GSSAPI/OID
%{perl_vendorarch}/GSSAPI/OID/Set.pm
%dir %{perl_vendorarch}/auto/GSSAPI
%attr(755,root,root) %{perl_vendorarch}/auto/GSSAPI/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
