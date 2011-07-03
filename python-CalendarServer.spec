
# TODO:
# - FHS

%define		module	CalendarServer
%define	snap	20110703

Summary:	Python modules to share calendaring information
Summary(pl.UTF-8):	Moduły Pythona do współdzielenia informacji kalendarzowych
Name:		python-%{module}
Version:	3.0
Release:	0.%{snap}.1
License:	Apache v2.0
Group:		Libraries/Python
# svn export http://svn.calendarserver.org/repository/calendarserver/CalendarServer/trunk/ CalendarServer-3.0
# revision 7704
Source0:	%{module}-%{version}-%{snap}.tgz
# Source0-md5:	8cbbd6f9cf9b8f22cb0535f12f6a048a
URL:		http://trac.calendarserver.org/
Requires:	python-TwistedMail
Requires:	python-TwistedWeb
Requires:	python-TwistedWeb2 >= 0.2.0
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
%setup -q -n %{module}-%{version}

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
%attr(755,root,root) %{_bindir}/calendarserver_*
%{_prefix}/caldavd
%{py_sitedir}/calendarserver
%{py_sitedir}/contrib
%{py_sitedir}/twext
%{py_sitedir}/twisted
%{py_sitedir}/twistedcaldav
%{py_sitedir}/txdav

%if "%{py_ver}" > "2.4"
%{py_sitedir}/Calendar_and_Contacts_Server-*-py2.7.egg-info
%endif
