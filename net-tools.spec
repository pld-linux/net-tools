Summary:	Basic Networking Tools
Summary(pl):	Podstawowe narzêdzia do obs³ugi i konfiguracji sieci
Name:		net-tools
Version:	1.57
Release:	4
License:	GPL
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administacyjne
Source0:	http://www.tazenda.demon.co.uk/phil/net-tools/%{name}-%{version}.tar.bz2
Source1:	ifconfig.8.pl
Source2:	netstat.8.pl
Patch0:		%{name}-config.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-mandir.patch
Patch3:		%{name}-ipvs.patch
URL:		http://www.tazenda.demon.co.uk/phil/net-tools/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gettext-devel
Obsoletes:	slattach

%description
This is a collection of the basic tools necessary for setting up
networking on a Linux machine. It includes ifconfig, route, netstat,
rarp, and some other minor tools.

%description -l pl
Pakiet ten zawiera zbiór podstawowych narzêdzi do konfigurowania
sieci. Znajduj± siê tutaj: ifconfig, route, netstat, rarp oraz inne -
mniej wa¿ne aplikacje.

%package -n slattach
Summary:	slattach - attach a network interface to a serial line
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administacyjne
Requires:	%{name} = %{version}

%description -n slattach
Slattach is a tiny little program that can be used to put a normal
terminal ("serial") line into one of several "network" modes, thus
allowing you to use it for point-to-point links to other computers.

%package -n plipconfig
Summary:	plipconfig - fine tune PLIP device parameters
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administacyjne
Requires:	%{name} = %{version}

%description -n plipconfig
Plipconfig is used to (hopefully) improve PLIP performance by changing
the default timing parameters used by the PLIP protocol. Results are
dependent on the parallel port hardware, cable, and the CPU speed of
each machine on each end of the PLIP link.

If the single interface argument is given, plipconfig displays the
status of the given interface only. Otherwise, it will try to set the
options.

%prep
%setup  -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} COPTS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g} -Wall" I18N=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BASEDIR=$RPM_BUILD_ROOT \
	INSTALL="%{_bindir}/install" \
	mandir=%{_mandir} \
	I18N=1

install -d $RPM_BUILD_ROOT%{_mandir}/pl/man8
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man8/ifconfig.8
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man8/netstat.8

gzip -9nf READ*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc READ*.gz

%attr(755,root,root) /bin/*
%attr(755,root,root) /sbin/arp
%attr(755,root,root) /sbin/ifconfig
%attr(755,root,root) /sbin/mii-tool
%attr(755,root,root) /sbin/rarp
%attr(755,root,root) /sbin/route

%lang(de) %{_mandir}/de_DE/man[15]/*
%lang(de) %{_mandir}/de_DE/man8/arp.8*
%lang(de) %{_mandir}/de_DE/man8/ifconfig.8*
%lang(de) %{_mandir}/de_DE/man8/netstat.8*
%lang(de) %{_mandir}/de_DE/man8/rarp.8*
%lang(de) %{_mandir}/de_DE/man8/route.8*
%lang(fr) %{_mandir}/fr_FR/man[15]/*
%lang(fr) %{_mandir}/fr_FR/man8/arp.8*
%lang(fr) %{_mandir}/fr_FR/man8/ifconfig.8*
%lang(fr) %{_mandir}/fr_FR/man8/netstat.8*
%lang(fr) %{_mandir}/fr_FR/man8/rarp.8*
%lang(fr) %{_mandir}/fr_FR/man8/route.8*
%lang(pt) %{_mandir}/pt_BR/man*/*
%lang(pl) %{_mandir}/pl/man*/*

%{_mandir}/man[15]/*
%{_mandir}/man8/arp.8*
%{_mandir}/man8/ifconfig.8*
%{_mandir}/man8/netstat.8*
%{_mandir}/man8/mii-tool.8*
%{_mandir}/man8/rarp.8*
%{_mandir}/man8/route.8*

%files -n slattach
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/slattach
%lang(de) %{_mandir}/de_DE/man8/slattach.8*
%lang(fr) %{_mandir}/fr_FR/man8/slattach.8*
%{_mandir}/man8/slattach.8*

%files -n plipconfig
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/plipconfig
%lang(de) %{_mandir}/de_DE/man8/plipconfig.8*
%lang(fr) %{_mandir}/fr_FR/man8/plipconfig.8*
%{_mandir}/man8/plipconfig.8*
