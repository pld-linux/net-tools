Summary:	Basic Networking Tools
Summary(pl):	Podstawowe narz�dzia do obs�ugi i konfiguracji sieci
Name:		net-tools
Version:	1.52
Release:	1
Copyright:	GPL
Group:		Networking/Admin
Group(pl):	Sieci/Administracja
Source0:	http://www.tazenda.demon.co.uk/phil/net-tools/%{name}-%{version}.tar.bz2
Source1:	ifconfig.8.pl
Source2:	netstat.8.pl
Patch0:		net-tools-config.patch
Patch1:		net-tools-man.patch
URL:		http://www.tazenda.demon.co.uk/phil/net-tools/
Buildroot:	/tmp/%{name}-%{version}-root
Obsoletes:	slattach

%description
This is a collection of the basic tools necessary for setting up networking
on a Linux machine. It includes ifconfig, route, netstat, rarp, and
some other minor tools.

%description -l pl
Pakiet ten zawiera zbi�r podstawowych narz�dzi do konfigurowania sieci.
Znajduj� si� tutaj: ifconfig, route, netstat, rarp oraz inne - mniej wa�ne
aplikacje.   

%prep
%setup  -q 
%patch0 -p1
%patch1 -p1

%build
make COPTS="$RPM_OPT_FLAGS -Wall" 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/man/pl/man8

make BASEDIR=$RPM_BUILD_ROOT install

strip $RPM_BUILD_ROOT/{bin/*,sbin/*}

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/usr/man/pl/man8

gzip -9nf $RPM_BUILD_ROOT/usr/man/{man1/*,man5/*,man8/*} READ*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc READ*.gz

%attr(755,root,root) /sbin/*
%attr(755,root,root) /bin/*

%lang(pt_BR) /usr/share/locale/pt_BR/LC_MESSAGES/*
%lang(fr)    /usr/share/locale/fr/LC_MESSAGES/*
%lang(de)    /usr/share/locale/de/LC_MESSAGES/*

%lang(de_DE) /usr/man/de_DE/man*/*
%lang(fr_FR) /usr/man/fr_FR/man*/*
%lang(pt_BR) /usr/man/pt_BR/man*/*
%lang(pl)    /usr/man/pl/man*/*

/usr/man/man*/*

%changelog
* Fri Apr 23 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.52-1]
- compiled on rpm 3
- added IRDa support
- added more locales

* Thu Apr 15 1999 Micha� Kuratczyk <kura@pld.org.pl>
  [1.51-2]
- gzipping documentation (instead bzipping)
- removed man group from man pages

* Mon Nov 30 1998 Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>
  [1.48-1d]
- new upstream release
- added slattach and plipconfig

* Tue Sep 02 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.47-1d]
- updated to 1.47,
- added sockek, glibc21 & config patches prepared by
  Maciej W. Rozycki <macro@ds2.pg.gda.pl>,
- using $RPM_OPT_FLAGS.   

* Tue Sep 02 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.46-1d]
- transaltion modified for pl,
- added Buildroot support,
- fixed permissions of all binaries,
- build from non root's account.

* Fri Jun 12 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.45-1d]
- build against glibc-2.1,

* Fri Feb 27 1998 Jason Spangler <jasons@usemail.com>
- added config patch

* Fri Feb 27 1998 Jason Spangler <jasons@usemail.com>
- changed to net-tools 1.432
- removed old glibc 2.1 patch

* Wed Oct 22 1997 Erik Troan <ewt@redhat.com>
- added extra patches for glibc 2.1

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- included complete set of network protocols (some were removed for
  initial glibc work)

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- updated glibc patch for glibc 2.0.5

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- updated to 1.33
