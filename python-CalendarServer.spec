
# TODO:
# - FHS

%define		module	CalendarServer
%define	snap	20090311

Summary:	Python modules to share calendaring information
Summary(pl.UTF-8):	Moduły Pythona do współdzielenia informacji kalendarzowych
Name:		python-%{module}
Version:	0.0.0
Release:	0.%{snap}.1
License:	Apache
Group:		Libraries/Python
Source0:	%{module}-%{snap}.tar.bz2
# Source0-md5:	8cbbd6f9cf9b8f22cb0535f12f6a048a
URL:		http://trac.calendarserver.org/
Requires:	python-TwistedWeb2 >= 0.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Darwin Calendar Server is a standards-compliant server that allows
multiple users to collaboratively share calendaring information. It
provides a shared location on the network to store schedules, and
allows users to send each other and manage invitations.

In order to provide interoperability with multiple calendaring
clients, the server implements the CalDAV protocol, which is an
extension of WebDAV, which is in turn an extension of HTTP.

%description -l pl.UTF-8
Darwin Calendar Server to zgodny ze standardami serwer pozwalający
wielu użytkownikom współdzielić informacje kalendarzowe. Udostępnia
współdzielone miejsce w siedzi do przechowywania terminarzy i pozwala
użytkownikom wysyłać między sobą i zarządzać zaproszeniami.

Dla zapewnienia współpracy z wieloma klientami kalendarza serwer
implementuje protokół CalDAV, który jest rozszerzeniem WebDAV, który z
kolei jest rozszerzeniem HTTP.

%prep
%setup -q -n %{module}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/caldavd
%attr(755,root,root) %{_bindir}/caldav_export
%{_prefix}/caldavd
%{py_sitescriptdir}/*.py[co]
%dir %{py_sitescriptdir}/calendarserver
%{py_sitescriptdir}/calendarserver/*.py[co]
%dir %{py_sitescriptdir}/calendarserver/platform
%{py_sitescriptdir}/calendarserver/platform/*.py[co]
%dir %{py_sitescriptdir}/calendarserver/platform/darwin
%{py_sitescriptdir}/calendarserver/platform/darwin/*.py[co]
%dir %{py_sitescriptdir}/calendarserver/provision
%{py_sitescriptdir}/calendarserver/provision/*.py[co]
%dir %{py_sitescriptdir}/calendarserver/tap
%{py_sitescriptdir}/calendarserver/tap/*.py[co]
%dir %{py_sitescriptdir}/calendarserver/tap/test
%{py_sitescriptdir}/calendarserver/tap/test/*.py[co]
%dir %{py_sitescriptdir}/calendarserver/test
%{py_sitescriptdir}/calendarserver/test/*.py[co]
%dir %{py_sitescriptdir}/calendarserver/tools/
%{py_sitescriptdir}/calendarserver/tools/*.py[co]
%dir %{py_sitescriptdir}/calendarserver/webcal
%{py_sitescriptdir}/calendarserver/webcal/*.py[co]
%dir %{py_sitescriptdir}/twext
%{py_sitescriptdir}/twext/*.py[co]
%dir %{py_sitescriptdir}/twext/internet
%{py_sitescriptdir}/twext/internet/*.py[co]
%dir %{py_sitescriptdir}/twext/python
%{py_sitescriptdir}/twext/python/*.py[co]
%dir %{py_sitescriptdir}/twisted
%dir %{py_sitescriptdir}/twisted/plugins
%{py_sitescriptdir}/twisted/plugins/*.py[co]
%dir %{py_sitescriptdir}/twistedcaldav
%{py_sitescriptdir}/twistedcaldav/*.py[co]
%dir %{py_sitescriptdir}/twistedcaldav/admin
%{py_sitescriptdir}/twistedcaldav/admin/*.py[co]
%dir %{py_sitescriptdir}/twistedcaldav/directory
%{py_sitescriptdir}/twistedcaldav/directory/*.py[co]
%dir %{py_sitescriptdir}/twistedcaldav/directory/test
%{py_sitescriptdir}/twistedcaldav/directory/test/*.py[co]
%dir %{py_sitescriptdir}/twistedcaldav/method
%{py_sitescriptdir}/twistedcaldav/method/*.py[co]
%dir %{py_sitescriptdir}/twistedcaldav/scheduling
%{py_sitescriptdir}/twistedcaldav/scheduling/*.py[co]
%dir %{py_sitescriptdir}/twistedcaldav/scheduling/test
%{py_sitescriptdir}/twistedcaldav/scheduling/test/*.py[co]
%dir %{py_sitescriptdir}/twistedcaldav/test
%{py_sitescriptdir}/twistedcaldav/test/*.py[co]
%dir %{py_sitescriptdir}/twistedcaldav/query
%{py_sitescriptdir}/twistedcaldav/query/*.py[co]
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo
%{py_sitescriptdir}/twistedcaldav/zoneinfo/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/Africa
%{py_sitescriptdir}/twistedcaldav/zoneinfo/Africa/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/America
%{py_sitescriptdir}/twistedcaldav/zoneinfo/America/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/America/Argentina
%{py_sitescriptdir}/twistedcaldav/zoneinfo/America/Argentina/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/America/Indiana
%{py_sitescriptdir}/twistedcaldav/zoneinfo/America/Indiana/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/America/Kentucky
%{py_sitescriptdir}/twistedcaldav/zoneinfo/America/Kentucky/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/America/North_Dakota
%{py_sitescriptdir}/twistedcaldav/zoneinfo/America/North_Dakota/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/Antarctica
%{py_sitescriptdir}/twistedcaldav/zoneinfo/Antarctica/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/Asia
%{py_sitescriptdir}/twistedcaldav/zoneinfo/Asia/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/Arctic
%{py_sitescriptdir}/twistedcaldav/zoneinfo/Arctic/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/Atlantic
%{py_sitescriptdir}/twistedcaldav/zoneinfo/Atlantic/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/Australia
%{py_sitescriptdir}/twistedcaldav/zoneinfo/Australia/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/Brazil
%{py_sitescriptdir}/twistedcaldav/zoneinfo/Brazil/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/Canada
%{py_sitescriptdir}/twistedcaldav/zoneinfo/Canada/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/Chile
%{py_sitescriptdir}/twistedcaldav/zoneinfo/Chile/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/Europe
%{py_sitescriptdir}/twistedcaldav/zoneinfo/Europe/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/Indian
%{py_sitescriptdir}/twistedcaldav/zoneinfo/Indian/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/Mexico
%{py_sitescriptdir}/twistedcaldav/zoneinfo/Mexico/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/Pacific
%{py_sitescriptdir}/twistedcaldav/zoneinfo/Pacific/*.ics
%dir %{py_sitescriptdir}/twistedcaldav/zoneinfo/US
%{py_sitescriptdir}/twistedcaldav/zoneinfo/US/*.ics

%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/twistedcaldav-*.egg-info
%endif
