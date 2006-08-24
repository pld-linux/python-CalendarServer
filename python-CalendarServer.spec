
# TODO:
# - FHS

%define		module	CalendarServer
%define	snap	20060823

Summary:	Python modules designed for writing games
Summary(pl):	Modu³y Pythona dla pisz±cych gry
Name:		python-%{module}
Version:	0.0.0
Release:	0.%{snap}.1
License:	Apache Group License
Group:		Libraries/Python
Source0:	%{module}-%{snap}.tar.gz
# Source0-md5:	5cb9954cbd1235e9534b1eea2fe711c5
URL:		http://trac.macosforge.org/projects/calendarserver
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

%prep
%setup -q -n %{module}

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/caldavd
%{_prefix}/caldavd
%dir %{py_sitescriptdir}/twistedcaldav
%{py_sitescriptdir}/twistedcaldav/*.py[co]
%dir %{py_sitescriptdir}/twistedcaldav/method/
%{py_sitescriptdir}/twistedcaldav/method/*.py[co]
%dir %{py_sitescriptdir}/twistedcaldav/query/
%{py_sitescriptdir}/twistedcaldav/query/*.py[co]
