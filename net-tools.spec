Summary:	Basic Networking Tools
Summary(es):	Herramientas bАsicas de Red
Summary(ja):	╔м╔ц╔х╔О║╪╔╞╓Р╔╩╔ц╔х╔╒╔ц╔в╓╧╓К╓©╓А╓н╢Пкэе╙╓й╔д║╪╔К
Summary(pl):	Podstawowe narzЙdzia do obsЁugi i konfiguracji sieci
Summary(pt_BR):	Ferramentas bАsicas de Rede
Summary(ru):	Базовые сетевые программы
Summary(uk):	Базов╕ програми мереж╕
Name:		net-tools
Version:	1.60
Release:	7
License:	GPL
Group:		Networking/Admin
Source0:	http://www.tazenda.demon.co.uk/phil/net-tools/%{name}-%{version}.tar.bz2
# Source0-md5: 888774accab40217dde927e21979c165
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5: 9cee6ac0a07a0bf34fbc71add1eb2ead
Patch0:		%{name}-config.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-ipvs.patch
Patch3:		%{name}-et.patch
URL:		http://www.tazenda.demon.co.uk/phil/net-tools/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		_sbindir	/sbin

%description
This is a collection of the basic tools necessary for setting up
networking on a Linux machine. It includes ifconfig, route, netstat,
rarp, and some other minor tools.

%description -l es
Esta es una colecciСn de herramientas bАsicas necesarias para la
configuraciСn de la red en una mАquina Linux. Incluye ifconfig, route,
netstat, rarp, y algunas otras herramientas menores.

%description -l pl
Pakiet ten zawiera zbiСr podstawowych narzЙdzi do konfigurowania
sieci. Znajduj╠ siЙ tutaj: ifconfig, route, netstat, rarp oraz inne -
mniej wa©ne aplikacje.

%description -l ja
net-tools ╔я╔ц╔╠║╪╔╦╓о╔м╔ц╔х╔О║╪╔╞╓Р╔╩╔ц╔х╔╒╔ц╔в╓╧╓К╢Пкэе╙╓й╔д║╪╔К╓Р
╢ч╓С╓г╓╓╓ч╓╧: arp║╒rarp║╒ifconfig║╒netstat║╒ethers ╓╫╓╥╓ф route ╓г╓╧║ё

%description -l pt_BR
Essa И uma coleГЦo de ferramentas bАsicas necessАrias para a
configuraГЦo da rede em uma mАquina Linux. Inclui ifconfig, route,
netstat, rarp, e algumas outras ferramentas menores.

%description -l ru
Это набор базовых программ, необходимых для установки и настройки
сети. Он включает ifconfig, netstat, route и другие программы.

Программы ifconfig и route для ядер 2.4.x являются устаревшими, т.к.
не позволяют управлять всеми возможностями, предоставляемыми этими
ядрами. Взамен их для конфигурации системы рекомендуется пользоваться
программой ip из пакета iproute2.

%description -l uk
Це наб╕р базових програм, необх╕дних для конф╕гурування мереж╕. В╕н
включа╓ ifconfig, netstat, route та ╕нш╕ програми.

Програми ifconfig та route для ядер 2.4.x ╓ застар╕лими, тому що не
дозволяють керувати вс╕ма можливостями, як╕ надають ц╕ ядра. Зам╕сть
них для конф╕гурування мереж╕ рекоменду╓ться користуватись програмою
ip з пакету iproute2.

%package -n slattach
Summary:	slattach - attach a network interface to a serial line
Summary(pl):	slattach - doЁ╠cz interfejs sieciowy do lini szeregowej
Group:		Networking/Admin
Requires:	%{name} = %{version}

%description -n slattach
Slattach is a tiny little program that can be used to put a normal
terminal ("serial") line into one of several "network" modes, thus
allowing you to use it for point-to-point links to other computers.

%description -n slattach -l pl
Slattach jest prostym programem, ktСry umo©liwia zamianЙ zwykЁej lini
terminala ("szeregowej") w jednen z kilku trybСw "sieciowych" przez co
umo©liwia na poЁ╠czenia point-to-point z innym komputerem.

%package -n plipconfig
Summary:	plipconfig - fine tune PLIP device parameters
Summary(pl):	plipconfig - dostrajanie parametrСw urz╠dzenia PLIP
Group:		Networking/Admin
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
Plipconfig jest u©ywany do poprawienia wydajno╤ci PLIP poprzez zmianЙ
domy╤lnych czasowych parametrСw u©ywanych w protokole PLIP. Rezultaty
zale©╠ od hardware portu rСwnolegЁego, kabla, szybko╤ci CPU ka©dej
maszyny poЁ╠czonej poprzez PLIP.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

%build
mv po/et_EE.po po/et.po
%{__make} COPTS="%{rpmcflags} -Wall" I18N=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BASEDIR=$RPM_BUILD_ROOT \
	INSTALL="install" \
	mandir=%{_mandir} \
	I18N=1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# standardize localized man dirs
(cd $RPM_BUILD_ROOT%{_mandir}
mv -f de_DE/*/* de/*/
mv -f fr_FR fr
# we can do it safely as no pt/pt_PT man pages appeared here yet
mv -f pt_BR pt
)

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc READ*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/arp
%attr(755,root,root) %{_sbindir}/ifconfig
%attr(755,root,root) %{_sbindir}/mii-tool
%attr(755,root,root) %{_sbindir}/rarp
%attr(755,root,root) %{_sbindir}/route
%attr(755,root,root) %{_sbindir}/nameif

# No de man8
%lang(de) %{_mandir}/de/man[15]/*
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
%lang(ja) %{_mandir}/ja/man[15]/*
%lang(ja) %{_mandir}/ja/man8/[^ps]*
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
%attr(755,root,root) %{_sbindir}/slattach
%lang(fr) %{_mandir}/fr/man8/slattach.8*
%lang(ja) %{_mandir}/ja/man8/slattach.8*
%lang(pl) %{_mandir}/pl/man8/slattach.8*
%{_mandir}/man8/slattach.8*

%files -n plipconfig
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/plipconfig
%lang(fr) %{_mandir}/fr/man8/plipconfig.8*
%lang(ja) %{_mandir}/ja/man8/plipconfig.8*
%{_mandir}/man8/plipconfig.8*
