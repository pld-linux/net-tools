Summary:	Basic Networking Tools
Summary(es.UTF-8):	Herramientas básicas de Red
Summary(ja.UTF-8):	ネットワークをセットアップするための基本的なツール
Summary(pl.UTF-8):	Podstawowe narzędzia do obsługi i konfiguracji sieci
Summary(pt_BR.UTF-8):	Ferramentas básicas de Rede
Summary(ru.UTF-8):	Базовые сетевые программы
Summary(uk.UTF-8):	Базові програми мережі
Name:		net-tools
Version:	1.60
Release:	27
License:	GPL
Group:		Networking/Admin
Source0:	http://download.berlios.de/net-tools/%{name}-%{version}.tar.bz2
# Source0-md5:	888774accab40217dde927e21979c165
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	9cee6ac0a07a0bf34fbc71add1eb2ead
Patch0:		%{name}-config.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-ipvs.patch
Patch3:		%{name}-et.patch

Patch5:		%{name}-x25_address_is_struct.patch
Patch6:		%{name}-make_config_h.patch
Patch7:		%{name}-mii.patch
Patch8:		%{name}-gcc34.patch
Patch9:		%{name}-nameif.patch
Patch10:	%{name}-inet6-lookup.patch
Patch11:	%{name}-ipx.patch
Patch12:	%{name}-manydevs.patch
Patch13:	%{name}-get_name.patch
Patch14:	%{name}-arp_overflow.patch
Patch15:	%{name}-virtualname.patch
Patch16:	%{name}-cycle.patch
Patch17:	%{name}-interface.patch
Patch18:	%{name}-ifaceopt.patch
Patch19:	%{name}-netstat-overflow.patch
Patch20:	%{name}-mii-tool-GigE.patch
URL:		http://net-tools.berlios.de/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		_sbindir	/sbin

%define		specflags	-fno-strict-aliasing

%description
This is a collection of the basic tools necessary for setting up
networking on a Linux machine. It includes ifconfig, route, netstat,
rarp, and some other minor tools.

%description -l es.UTF-8
Esta es una colección de herramientas básicas necesarias para la
configuración de la red en una máquina Linux. Incluye ifconfig, route,
netstat, rarp, y algunas otras herramientas menores.

%description -l pl.UTF-8
Pakiet ten zawiera zbiór podstawowych narzędzi do konfigurowania
sieci. Znajdują się tutaj: ifconfig, route, netstat, rarp oraz inne -
mniej ważne aplikacje.

%description -l ja.UTF-8
net-tools パッケージはネットワークをセットアップする基本的なツールを
含んでいます: arp、rarp、ifconfig、netstat、ethers そして route です。

%description -l pt_BR.UTF-8
Essa é uma coleção de ferramentas básicas necessárias para a
configuração da rede em uma máquina Linux. Inclui ifconfig, route,
netstat, rarp, e algumas outras ferramentas menores.

%description -l ru.UTF-8
Это набор базовых программ, необходимых для установки и настройки
сети. Он включает ifconfig, netstat, route и другие программы.

Программы ifconfig и route для ядер 2.4.x являются устаревшими, т.к.
не позволяют управлять всеми возможностями, предоставляемыми этими
ядрами. Взамен их для конфигурации системы рекомендуется пользоваться
программой ip из пакета iproute2.

%description -l uk.UTF-8
Це набір базових програм, необхідних для конфігурування мережі. Він
включає ifconfig, netstat, route та інші програми.

Програми ifconfig та route для ядер 2.4.x є застарілими, тому що не
дозволяють керувати всіма можливостями, які надають ці ядра. Замість
них для конфігурування мережі рекомендується користуватись програмою
ip з пакету iproute2.

%package -n slattach
Summary:	slattach - attach a network interface to a serial line
Summary(pl.UTF-8):	slattach - dołącz interfejs sieciowy do lini szeregowej
Group:		Networking/Admin
Requires:	%{name} = %{version}-%{release}

%description -n slattach
Slattach is a tiny little program that can be used to put a normal
terminal ("serial") line into one of several "network" modes, thus
allowing you to use it for point-to-point links to other computers.

%description -n slattach -l pl.UTF-8
Slattach jest prostym programem, który umożliwia zamianę zwykłej linii
terminala ("szeregowej") w jeden z kilku trybów "sieciowych" przez co
umożliwia na połączenia point-to-point z innym komputerem.

%package -n plipconfig
Summary:	plipconfig - fine tune PLIP device parameters
Summary(pl.UTF-8):	plipconfig - dostrajanie parametrów urządzenia PLIP
Group:		Networking/Admin
Requires:	%{name} = %{version}-%{release}

%description -n plipconfig
Plipconfig is used to (hopefully) improve PLIP performance by changing
the default timing parameters used by the PLIP protocol. Results are
dependent on the parallel port hardware, cable, and the CPU speed of
each machine on each end of the PLIP link.

If the single interface argument is given, plipconfig displays the
status of the given interface only. Otherwise, it will try to set the
options.

%description -n plipconfig -l pl.UTF-8
Plipconfig jest używany do poprawienia wydajności PLIP poprzez zmianę
domyślnych czasowych parametrów używanych w protokole PLIP. Rezultaty
zależą od hardware portu równoległego, kabla, szybkości CPU każdej
maszyny połączonej poprzez PLIP.

%prep
%setup -q
%patch20 -p2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1

mv po/et_EE.po po/et.po

%build
%{__make} \
	CC="%{__cc}" \
	COPTS="%{rpmcflags} -Wall" \
	I18N=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	BASEDIR=$RPM_BUILD_ROOT \
	INSTALL="install" \
	mandir=%{_mandir} \
	I18N=1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT%{_mandir}/README.net-tools-non-english-man-pages

# standardize localized man dirs
mv -f $RPM_BUILD_ROOT%{_mandir}/{de_DE/man1/*,de/man1}
rmdir $RPM_BUILD_ROOT%{_mandir}/de_DE/man1
mv -f $RPM_BUILD_ROOT%{_mandir}/{de_DE/*,de}
mv -f $RPM_BUILD_ROOT%{_mandir}/{fr_FR,fr}
# we can do it safely as no pt/pt_PT man pages appeared here yet
mv $RPM_BUILD_ROOT%{_mandir}/{pt_BR,pt}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/mactab <<EOF
# Each line here contains an interface name and a Ethernet MAC address. Like:
#lan 00:13:d3:05:15:d2
EOF

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc READ*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mactab
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/arp
%attr(755,root,root) %{_sbindir}/ifconfig
%attr(755,root,root) %{_sbindir}/mii-tool
%attr(755,root,root) %{_sbindir}/rarp
%attr(755,root,root) %{_sbindir}/route
%attr(755,root,root) %{_sbindir}/nameif

%lang(de) %{_mandir}/de/man[15]/*
%lang(de) %{_mandir}/de/man8/[!ps]*
%lang(es) %{_mandir}/es/man[15]/*
%lang(es) %{_mandir}/es/man8/[!ps]*
%lang(fi) %{_mandir}/fi/man[15]/*
# No fi man8
%lang(fr) %{_mandir}/fr/man[15]/*
%lang(fr) %{_mandir}/fr/man8/[!ps]*
%lang(hu) %{_mandir}/hu/man[15]/*
%lang(hu) %{_mandir}/hu/man8/[!ps]*
%lang(id) %{_mandir}/id/man[15]/*
%lang(id) %{_mandir}/id/man8/[!ps]*
%lang(it) %{_mandir}/it/man[15]/*
%lang(it) %{_mandir}/it/man8/[!ps]*
%lang(ja) %{_mandir}/ja/man[15]/*
%lang(ja) %{_mandir}/ja/man8/[!ps]*
# No nl man[15]
%lang(nl) %{_mandir}/nl/man8/[!ps]*
%lang(pt) %{_mandir}/pt/man[15]/*
%lang(pt) %{_mandir}/pt/man8/[!ps]*
%lang(pl) %{_mandir}/pl/man[15]/*
%lang(pl) %{_mandir}/pl/man8/[!ps]*

%{_mandir}/man[15]/*
%{_mandir}/man8/[!ps]*

%files -n slattach
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/slattach
%lang(de) %{_mandir}/de/man8/slattach.8*
%lang(fr) %{_mandir}/fr/man8/slattach.8*
%lang(ja) %{_mandir}/ja/man8/slattach.8*
%lang(pl) %{_mandir}/pl/man8/slattach.8*
%{_mandir}/man8/slattach.8*

%files -n plipconfig
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/plipconfig
%lang(de) %{_mandir}/de/man8/plipconfig.8*
%lang(fr) %{_mandir}/fr/man8/plipconfig.8*
%lang(ja) %{_mandir}/ja/man8/plipconfig.8*
%{_mandir}/man8/plipconfig.8*
