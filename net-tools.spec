# TODO
# - changing config.in is not sufficent, must patch config.h and config.make manually
Summary:	Basic Networking Tools
Summary(es.UTF-8):	Herramientas básicas de Red
Summary(ja.UTF-8):	ネットワークをセットアップするための基本的なツール
Summary(pl.UTF-8):	Podstawowe narzędzia do obsługi i konfiguracji sieci
Summary(pt_BR.UTF-8):	Ferramentas básicas de Rede
Summary(ru.UTF-8):	Базовые сетевые программы
Summary(uk.UTF-8):	Базові програми мережі
Name:		net-tools
Version:	2.10
Release:	2
License:	GPL v2+
Group:		Networking/Admin
Source0:	https://sourceforge.net/projects/net-tools/files/%{name}-%{version}.tar.xz
# Source0-md5:	78aae762c95e2d731faf88d482e4cde5
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	9cee6ac0a07a0bf34fbc71add1eb2ead
Patch0:		%{name}-config.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-opt.patch
Patch3:		%{name}-make_config_h.patch
Patch4:		%{name}-tr.patch
Patch5:		%{name}-netstat-netlink-diag.patch
Patch6:		net-tools-interface.patch
URL:		https://sourceforge.net/projects/net-tools/
BuildRequires:	gettext-tools
Requires:	hostname
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
Summary(pl.UTF-8):	slattach - dołączanie interfejsu sieciowego do linii szeregowej
Group:		Networking/Admin
Requires:	%{name} = %{version}-%{release}

%description -n slattach
Slattach is a tiny little program that can be used to put a normal
terminal ("serial") line into one of several "network" modes, thus
allowing you to use it for point-to-point links to other computers.

%description -n slattach -l pl.UTF-8
Slattach jest prostym programem, który umożliwia zamianę zwykłej linii
terminala ("szeregowej") w jeden z kilku trybów "sieciowych", co
pozwala na połączenia point-to-point z innym komputerem.

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
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1

%build
%{__make} -j1 \
	CC="%{__cc}" \
	COPTS="%{rpmcppflags} %{rpmcflags} -Wall" \
	I18N=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	BASEDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p" \
	mandir=%{_mandir} \
	I18N=1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.net-tools-non-english-man-pages

# standardize localized man dirs
rmdir $RPM_BUILD_ROOT%{_mandir}/de_DE/man1
mv -f $RPM_BUILD_ROOT%{_mandir}/{de_DE/*,de}
mv -f $RPM_BUILD_ROOT%{_mandir}/{fr_FR,fr}
# we can do it safely as no pt/pt_PT man pages appeared here yet
mv $RPM_BUILD_ROOT%{_mandir}/{pt_BR,pt}

# for compatibility
ln -s %{_bindir}/ifconfig $RPM_BUILD_ROOT%{_sbindir}/ifconfig
ln -s %{_bindir}/route $RPM_BUILD_ROOT%{_sbindir}/route

# remove hostname (has its own package)
%{__rm} $RPM_BUILD_ROOT%{_mandir}/*/man1/dnsdomainname*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/*/man1/domainname*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/*/man1/hostname*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/*/man1/nisdomainname*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/*/man1/ypdomainname*

cat > $RPM_BUILD_ROOT%{_sysconfdir}/mactab <<EOF
# Each line here contains an interface name and a Ethernet MAC address. Like:
#lan 00:13:d3:05:15:d2
EOF

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mactab
%attr(755,root,root) %{_bindir}/ifconfig
%attr(755,root,root) %{_bindir}/netstat
%attr(755,root,root) %{_bindir}/route
%attr(755,root,root) %{_sbindir}/arp
%attr(755,root,root) %{_sbindir}/ifconfig
%attr(755,root,root) %{_sbindir}/mii-tool
%attr(755,root,root) %{_sbindir}/nameif
%attr(755,root,root) %{_sbindir}/rarp
%attr(755,root,root) %{_sbindir}/route

%lang(de) %{_mandir}/de/man5/ethers.5*
%lang(de) %{_mandir}/de/man8/[!ps]*
%lang(es) %{_mandir}/es/man5/ethers.5*
%lang(es) %{_mandir}/es/man8/[!ps]*
%lang(fr) %{_mandir}/fr/man5/ethers.5*
%lang(fr) %{_mandir}/fr/man8/[!ps]*
%lang(hu) %{_mandir}/hu/man8/[!ps]*
%lang(id) %{_mandir}/id/man8/[!ps]*
%lang(it) %{_mandir}/it/man8/[!ps]*
%lang(ja) %{_mandir}/ja/man5/ethers.5*
%lang(ja) %{_mandir}/ja/man8/[!ps]*
%lang(nl) %{_mandir}/nl/man8/[!ps]*
%lang(pt) %{_mandir}/pt/man8/[!ps]*
%lang(pl) %{_mandir}/pl/man8/[!ps]*
%{_mandir}/man5/ethers.5*
%{_mandir}/man8/arp.8*
%{_mandir}/man8/ifconfig.8*
%{_mandir}/man8/mii-tool.8*
%{_mandir}/man8/nameif.8*
%{_mandir}/man8/netstat.8*
%{_mandir}/man8/rarp.8*
%{_mandir}/man8/route.8*

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
