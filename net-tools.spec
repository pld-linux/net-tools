Summary:	Basic Networking Tools
Summary(pl):	Podstawowe narzêdzia do obs³ugi i konfiguracji sieci
Name:		net-tools
Version:	1.52
Release:	3
Copyright:	GPL
Group:		Networking/Admin
Group(pl):	Sieciowe/Administracyjne
Source0:	http://www.tazenda.demon.co.uk/phil/net-tools/%{name}-%{version}.tar.bz2
Source1:	ifconfig.8.pl
Source2:	netstat.8.pl
Patch0:		net-tools-config.patch
Patch1:		net-tools-man.patch
Patch2:		net-tools-compile.patch
URL:		http://www.tazenda.demon.co.uk/phil/net-tools/
Buildroot:	/tmp/%{name}-%{version}-root
Obsoletes:	slattach

%description
This is a collection of the basic tools necessary for setting up networking
on a Linux machine. It includes ifconfig, route, netstat, rarp, and
some other minor tools.

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
make COPTS="$RPM_OPT_FLAGS -Wall" 

%install
rm -rf $RPM_BUILD_ROOT

make \
    BASEDIR=$RPM_BUILD_ROOT \
    INSTALL="/bin/install" install

strip $RPM_BUILD_ROOT/{bin/*,sbin/*}

mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}

install -d $RPM_BUILD_ROOT%{_mandir}/pl/man8
install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/{man1/*,man5/*,man8/*} READ*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc READ*.gz

%attr(755,root,root) /sbin/*
%attr(755,root,root) /bin/*

%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/*
%lang(fr)    %{_datadir}/locale/fr/LC_MESSAGES/*
%lang(de)    %{_datadir}/locale/de/LC_MESSAGES/*

%lang(de_DE) %{_mandir}/de_DE/man*/*
%lang(fr_FR) %{_mandir}/fr_FR/man*/*
%lang(pt_BR) %{_mandir}/pt_BR/man*/*
%lang(pl)    %{_mandir}/pl/man*/*

%{_mandir}/man*/*

%changelog
* Sun May 23 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.52-3]
- fixes fo compiling,
- minor changes.

* Fri Apr 23 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.52-1]
- compiled on rpm 3
- added IRDa support
- added more locales

* Thu Apr 15 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [1.51-2]
- gzipping documentation (instead bzipping)
- removed man group from man pages

* Mon Nov 30 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [1.48-1d]
- new upstream release
- added slattach and plipconfig

* Tue Sep 02 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.47-1d]
- updated to 1.47,
- added sockek, glibc21 & config patches prepared by

  Maciek W. Ro¿ycki <macro@ds2.pg.gda.pl>,

- using $RPM_OPT_FLAGS.   

* Tue Sep 02 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.46-1d]
- transaltion modified for pl,
- added Buildroot support,
- fixed permissions of all binaries,
- build from non root's account.

* Fri Jun 12 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.45-1d]
- build against glibc-2.1,
- start at RH spec file.
