Summary:	Basic Networking Tools
Summary(pl):	Podstawowe narzêdzia do obs³ugi i konfiguracji sieci
Name:		net-tools
Version:	1.55
Release:	1
License:	GPL
Group:		Networking/Admin
Group(pl):	Sieciowe/Administracja
Source0:	http://www.tazenda.demon.co.uk/phil/net-tools/%{name}-%{version}.tar.bz2
Source1:	ifconfig.8.pl
Source2:	netstat.8.pl
Patch0:		net-tools-config.patch
Patch1:		net-tools-man.patch
Patch2:		net-tools-mandir.patch
URL:		http://www.tazenda.demon.co.uk/phil/net-tools/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	slattach

%description
This is a collection of the basic tools necessary for setting up networking
on a Linux machine. It includes ifconfig, route, netstat, rarp, and some
other minor tools.

%description -l pl
Pakiet ten zawiera zbiór podstawowych narzêdzi do konfigurowania sieci.
Znajduj± siê tutaj: ifconfig, route, netstat, rarp oraz inne - mniej wa¿ne
aplikacje.

%prep
%setup  -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make COPTS="$RPM_OPT_FLAGS -Wall" I18N=1

%install
rm -rf $RPM_BUILD_ROOT

make install \
	BASEDIR=$RPM_BUILD_ROOT \
	INSTALL="%{_bindir}/install" \
	mandir=%{_mandir} \
	I18N=1

strip $RPM_BUILD_ROOT/{bin/*,sbin/*}

install -d $RPM_BUILD_ROOT%{_mandir}/pl/man8
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man8/ifconfig.8
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man8/netstat.8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/{man{1,5,8}/*,*/man*/*} \
	READ*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc READ*.gz

%attr(755,root,root) /sbin/*
%attr(755,root,root) /bin/*

%lang(de_DE) %{_mandir}/de_DE/man*/*
%lang(fr_FR) %{_mandir}/fr_FR/man*/*
%lang(pt_BR) %{_mandir}/pt_BR/man*/*
%lang(pl)    %{_mandir}/pl/man*/*

%{_mandir}/man*/*
