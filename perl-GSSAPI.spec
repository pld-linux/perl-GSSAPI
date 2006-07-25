#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	GSSAPI
Summary:	GSSAPI - Perl extension providing access to the GSSAPIv2 library
Name:		perl-GSSAPI
Version:	0.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AG/AGROLMS/GSSAPI-0.22.tar.gz
# Source0-md5:	63ea55e46783c028ef6dac0ec2ca0887
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	heimdal-devel
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module gives access to the routines of the GSSAPI library,
as described in rfc2743 and rfc2744 and implemented by the
Kerberos-1.2 distribution from MIT.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/GSSAPI/*.pm
%dir %{perl_vendorarch}/auto/GSSAPI
%{perl_vendorarch}/auto/GSSAPI/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/GSSAPI/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
