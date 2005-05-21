Summary:	Multiple stacked system monitors: 1 process
Summary(pl):	Zestaw wielu monitorów systemu(ów) w jednym procesie
Summary(pt_BR):	Monitoração de atividades do sistema
Summary(ru):	GKrellM - ÜÔÏ ÓÔÅË ÓÉÓÔÅÍÎÙÈ ÍÏÎÉÔÏÒÏ× × ÒÁÍËÁÈ ÏÄÎÏÇÏ ÐÒÏÃÅÓÓÁ
Summary(uk):	GKrellM - ÃÅ ÓÔÅË ÓÉÓÔÅÍÎÉÈ ÍÏÎ¦ÔÏÒ¦× Õ ÒÁÍËÁÈ ÏÄÎÏÇÏ ÐÒÏÃÅÓÕ
Name:		gkrellm
Version:	2.2.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://members.dslextreme.com/users/billw/gkrellm/%{name}-%{version}.tar.gz	
# Source0-md5:	2613a625479babbac3a962fe6a2cb43e
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	gkrellmd.init
Source4:	gkrellmd.sysconf
Patch0:		%{name}-opt.patch
Patch1:		%{name}-home_etc.patch
Icon:		gkrellm.xpm
URL:		http://www.gkrellm.net/
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gnutls-devel
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GKrellM charts SMP CPU, load, Disk, and all active net interfaces
automatically. An on/off button and online timer for the PPP interface
is provided. Includes meters for memory and swap usage, an uptime
monitor, a hostname label, and a clock/calendar. are provided.
Additional features are:

  - Autoscaling grid lines with configurable grid line resolution.
  - LED indicators for the net interfaces.
  - A gui popup for configuration of chart sizes and resolutions.

%description -l pl
GKrellM automatycznie wy¶wietla wykresy aktywno¶ci SMP CPU,
obci±¿enia, dysku oraz aktywnych interfejsów sieciowych. Jest równie¿
przycisk wy³±cznika, czasomierz dla interfejsu PPP, mierniki
wykorzystania pamiêci oraz partycji wymiany, wy¶wietlacz czasy, który
up³yn±³ od w³±czenia maszyny, etykietê nazwy hosta oraz zegar i
kalendarz. Inne funkcje:

 - Samoskaluj±ce siê linie siatki o konfigurowanej gêsto¶ci
 - Wy¶wietlacze imituj±ce diody LED dla interfejsów sieciowych
 - Narzêdzie gui do konfiguracji rozmiarów wykresów i rozdzielczo¶ci

%description -l pt_BR
O GKrellM mostra gráficos com dados sobre CPUs, carga da máquina,
discos e todas as interfaces de rede ativas, automaticamente. Um botão
liga/desliga e um temporizador para a interface PPP estão presentes.
Monitores para uso de memória e área de troca, sistemas de arquivos,
conexões Internet, para a bateria de computadores portáteis, para
caixas de correio no estilo mbox e para a temperatura da CPU. Também
inclui um monitor de tempo de atividade da máquina, um rótulo como o
nome da máquina e um relógio e calendário.

%description -l ru
GKrellM ÏÔÏÂÒÁÖÁÅÔ ÇÒÁÆÉËÉ ÄÌÑ SMP CPU, ÚÁÇÒÕÚËÉ, ÄÉÓËÏ× É ×ÓÅÈ
ÁËÔÉ×ÎÙÈ ÓÅÔÅ×ÙÈ ÉÎÔÅÒÆÅÊÓÏ× Á×ÔÏÍÁÔÉÞÅÓËÉ. åÓÔØ ËÎÏÐËÁ on/off É
ÔÁÊÍÅÒ ×ÒÅÍÅÎÉ ÏÎÌÁÊÎ ÄÌÑ PPP ÉÎÔÅÒÆÅÊÓÁ. åÓÔØ ÍÏÎÉÔÏÒÙ ÏÐÅÒÁÔÉ×ÎÏÊ
ÐÁÍÑÔÉ É swap, ÆÁÊÌÏ×ÙÈ ÓÉÓÔÅÍ, ÏÂÒÁÝÅÎÉÊ ÉÚ ÉÎÔÅÒÎÅÔÁ, APM, ÐÏÞÔÏ×ÙÈ
ÑÝÉËÏ× É ÔÅÍÐÅÒÁÔÕÒÙ CPU. ÷ËÌÀÞÁÅÔ ÔÁËÖÅ ÍÏÎÉÔÏÒ uptime, ÍÅÔËÕ ÉÍÅÎÉ
ÈÏÓÔÁ, ÞÁÓÙ É ËÁÌÅÎÄÁÒØ.

%description -l uk
GKrellM ×¦ÄÏÂÒÁÖÁ¤ ÇÒÁÆ¦ËÉ ÄÌÑ SMP CPU, ÚÁ×ÁÎÔÁÖÅÎÎÑ, ÄÉÓË¦× ÔÁ ×Ó¦È
ÁËÔÉ×ÎÉÈ ÍÅÒÅÖÅ×ÉÈ ¦ÎÔÅÒÆÅÊÓ¦× Á×ÔÏÍÁÔÉÞÎÏ. ´ ËÎÏÐËÁ on/off ÔÁ ÔÁÊÍÅÒ
ÏÎÌÁÊÎ-ÞÁÓÕ ÄÌÑ PPP ¦ÎÔÅÒÆÅÊÓÕ. ´ ÍÏÎ¦ÔÏÒÉ ÏÐÅÒÁÔÉ×ÎÏ§ ÐÁÍ'ÑÔ¦ ÔÁ
swap, ÆÁÊÌÏ×ÉÈ ÓÉÓÔÅÍ, Ú×ÅÒÔÁÎØ Ú ¦ÎÔÅÒÎÅÔÕ, APM, ÐÏÛÔÏ×ÉÈ ÓËÒÉÎØÏË ÔÁ
ÔÅÍÐÅÒÁÔÕÒÉ CPU. ÷ËÌÀÞÁ¤ ÔÁËÏÖ ÍÏÎ¦ÔÏÒ uptime, Í¦ÔËÕ ¦ÍÅÎ¦ ÈÏÓÔÁ,
ÇÏÄÉÎÎÉË ÔÁ ËÁÌÅÎÄÁÒ.

%package gkrellmd
Summary:	gkrellmd - The GNU Krell Monitors Server
Summary(pl):	gkrellmd - Serwer monitorów GKrellM
Group:		Daemons
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig

%description gkrellmd
gkrellmd listens for connections from gkrellm clients.  When a gkrellm
client connects to a gkrellmd server all builtin monitors collect their
data from the server.

%description gkrellmd -l pl
gkrellmd nas³uchuje po³±czeñ z klientów gkrellm.  Gdy klient gkrellm
³±czy siê z serwerem gkrellmd, wszystkie wbudowane monitory pobieraj±
dane z serwera.

%package devel
Summary:	gkrellm include files
Summary(pl):	Pliki nag³ówkowe do gkrellm
Summary(pt_BR):	Componentes para desenvolvimento com o gkrellm
Summary(ru):	æÁÊÌÙ C ÈÅÄÅÒÏ× ÄÌÑ GKrellM
Summary(uk):	æÁÊÌÉ C ÈÅÄÅÒ¦× ÄÌÑ GKrellM
Group:		X11/Development/Libraries
Requires:	gtk+2-devel

%description devel
gkrellm header files for gkrellm development and plugin support.

%description devel -l pl
Pliki nag³ówkowe do gkrellm.

%description devel -l pt_BR
Componentes para desenvolvimento de plugins para o gkrellm.

%description devel -l ru
æÁÊÌÙ C ÈÅÄÅÒÏ× ÄÌÑ GKrellM - ÄÌÑ ÒÁÚÒÁÂÏÔËÉ É ÐÏÄÄÅÒÖËÉ ÍÏÄÕÌÅÊ.

%description devel -l uk
æÁÊÌÉ C ÈÅÄÅÒ¦× ÄÌÑ GKrellM - ÄÌÑ ÒÏÚÒÏÂËÉ ÔÁ Ð¦ÄÔÒÉÍËÉ ÍÏÄÕÌ¦×.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	OPTFLAGS="%{rpmcflags}" \
	PKGCONFIGDIR=%{_pkgconfigdir} \
	INSTALLROOT=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/gkrellm2} \
	$RPM_BUILD_ROOT%{_libdir}/gkrellm2{,/plugins} \
	$RPM_BUILD_ROOT%{_datadir}/gkrellm2 \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/locale

%{__make} install \
	%{?debug:STRIP=} \
	PKGCONFIGDIR=$RPM_BUILD_ROOT%{_pkgconfigdir} \
	INSTALLROOT=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install -D %{SOURCE3} $RPM_BUILD_ROOT%{_initrddir}/gkrellmd
install -D %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/gkrellmd
install -D server/gkrellmd.conf $RPM_BUILD_ROOT%{_sysconfdir}/gkrellmd.conf

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post gkrellmd
/sbin/chkconfig --add gkrellmd
if [ -f %{_localstatedir}/lock/subsys/gkrellmd ]; then
	%{_initrddir}/gkrellmd restart >&2
else
	echo "Run \"%{_initrddir}/gkrellmd start\" to start gkrellmd." >&2
fi

%preun gkrellmd
if [ "$1" = "0" ]; then
	if [ -f %{_localstatedir}/lock/subsys/gkrellmd ]; then
		%{_initrddir}/gkrellmd stop
	fi
	/sbin/chkconfig --del gkrellmd
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changelog* README Themes.html
%attr(755,root,root) %{_bindir}/gkrellm
%{_mandir}/man1/gkrellm.*
%dir %{_libdir}/gkrellm2
%dir %{_libdir}/gkrellm2/plugins
%dir %{_datadir}/gkrellm2
%{_desktopdir}/*
%{_pixmapsdir}/*

%files gkrellmd
%defattr(644,root,root,755)
%{_mandir}/man1/gkrellmd.*
%attr(755,root,root) %{_bindir}/gkrellmd
%attr(755,root,root) %{_initrddir}/gkrellmd
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/sysconfig/gkrellmd
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/gkrellmd.conf

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_pkgconfigdir}/*
