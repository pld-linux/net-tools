Summary:	Basic Networking Tools
Summary(pl):	Podstawowe narzêdzia do obs³ugi i konfiguracji sieci
Name:		net-tools
Version:	1.60
Release:	3
License:	GPL
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administacyjne
Source0:	http://www.tazenda.demon.co.uk/phil/net-tools/%{name}-%{version}.tar.bz2
Source1:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-config.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-ipvs.patch
URL:		http://www.tazenda.demon.co.uk/phil/net-tools/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Summary(pl):	slattach - do³±cz interfejs sieciowy do lini szeregowej
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administacyjne
Requires:	%{name} = %{version}

%description -n slattach
Slattach is a tiny little program that can be used to put a normal
terminal ("serial") line into one of several "network" modes, thus
allowing you to use it for point-to-point links to other computers.

%description -n slattach -l pl
Slattach jest prostym programem, który umo¿liwia zamianê zwyk³ej lini
terminala ("szeregowej") w jednen z kilku trybów "sieciowych" przez co
umo¿liwia na po³±czenia point-to-point z innym komputerem.

%package -n plipconfig
Summary:	plipconfig - fine tune PLIP device parameters
Summary(pl):	plipconfig - dostrajanie parametrów urz±dzenia PLIP
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

%description -n plipconfig -l pl
Plipconfig jest u¿ywany do poprawienia wydajno¶ci PLIP poprzez zmianê
domy¶lnych czasowych parametrów u¿ywanych w protokole PLIP. Rezultaty
zale¿± od hardware portu równoleg³ego, kabla, szybko¶ci CPU ka¿dej
maszyny po³±czonej poprzez PLIP.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} COPTS="%{rpmcflags} -Wall" I18N=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man8

%{__make} install \
	BASEDIR=$RPM_BUILD_ROOT \
	INSTALL="%{_bindir}/install" \
	mandir=%{_mandir} \
	I18N=1

bzip2 -dc %{SOURCE1} | tar -xf - -C $RPM_BUILD_ROOT%{_mandir}

# standardize localized man dirs
(cd $RPM_BUILD_ROOT%{_mandir}
mv -f de_DE de
mv -f fr_FR fr
# we can do it safely as no pt/pt_PT man pages appeared here yet
mv -f pt_BR pt
)

gzip -9nf READ*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /bin/*
%attr(755,root,root) /sbin/arp
%attr(755,root,root) /sbin/ifconfig
%attr(755,root,root) /sbin/mii-tool
%attr(755,root,root) /sbin/rarp
%attr(755,root,root) /sbin/route

%lang(da) %{_mandir}/da/man[15]/*
# No da man8
%lang(de) %{_mandir}/de/man[15]/*
%lang(de) %{_mandir}/de/man8/[^ps]*
%lang(es) %{_mandir}/es/man[15]/*
%lang(es) %{_mandir}/es/man8/[^ps]*
%lang(fi) %{_mandir}/fi/man[15]/*
# No fi man8
%lang(fr) %{_mandir}/fr/man[15]/*
%lang(fr) %{_mandir}/fr/man8/[^ps]*
%lang(hu) %{_mandir}/hu/man[15]/*
%lang(hu) %{_mandir}/hu/man8/[^ps]*
%lang(id) %{_mandir}/id/man[15]/*
%lang(id) %{_mandir}/id/man8/[^ps]*
%lang(it) %{_mandir}/it/man[15]/*
%lang(it) %{_mandir}/it/man8/[^ps]*
# No nl man[15]
%lang(nl) %{_mandir}/nl/man8/[^ps]*
%lang(pt) %{_mandir}/pt/man[15]/*
%lang(pt) %{_mandir}/pt/man8/[^ps]*
%lang(pl) %{_mandir}/pl/man[15]/*
%lang(pl) %{_mandir}/pl/man8/[^ps]*

%{_mandir}/man[15]/*
%{_mandir}/man8/[^ps]*

%files -n slattach
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/slattach
%lang(de) %{_mandir}/de/man8/slattach.8*
%lang(fr) %{_mandir}/fr/man8/slattach.8*
%lang(pl) %{_mandir}/pl/man8/slattach.8*
%{_mandir}/man8/slattach.8*

%files -n plipconfig
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/plipconfig
%lang(de) %{_mandir}/de/man8/plipconfig.8*
%lang(fr) %{_mandir}/fr/man8/plipconfig.8*
%{_mandir}/man8/plipconfig.8*
