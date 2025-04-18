#
# Conditional build:
%bcond_without	gnutls		# gnutls instead of OpenSSL (for mail check support)
%bcond_without	lm_sensors	# sensors support by libsensors
#
Summary:	Multiple stacked system monitors: 1 process
Summary(pl.UTF-8):	Zestaw wielu monitorów systemu(ów) w jednym procesie
Summary(pt_BR.UTF-8):	Monitoração de atividades do sistema
Summary(ru.UTF-8):	GKrellM - это стек системных мониторов в рамках одного процесса
Summary(uk.UTF-8):	GKrellM - це стек системних моніторів у рамках одного процесу
Name:		gkrellm
Version:	2.4.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://gkrellm.srcbox.net/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	752a8591bb09cca793dfbe85e6ad2fd1
Source3:	%{name}d.init
Source4:	%{name}d.sysconf
Patch0:		%{name}-opt.patch
Patch1:		%{name}-home_etc.patch
Patch2:		%{name}-pl.po-update.patch
Patch3:		%{name}-lm_sensors.patch
Patch4:		%{name}-desktop.patch
URL:		https://gkrellm.srcbox.net/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32
%{?with_gnutls:BuildRequires:	gnutls-devel >= 1.2.5}
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libntlm-devel
%{?with_lm_sensors:BuildRequires:	lm_sensors-devel}
%{!?with_gnutls:BuildRequires:	openssl-devel}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	which
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	glib2 >= 1:2.32
Requires:	gtk+2 >= 2:2.4
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

%description -l pl.UTF-8
GKrellM automatycznie wyświetla wykresy aktywności SMP CPU,
obciążenia, dysku oraz aktywnych interfejsów sieciowych. Jest również
przycisk wyłącznika, czasomierz dla interfejsu PPP, mierniki
wykorzystania pamięci oraz partycji wymiany, wyświetlacz czasy, który
upłynął od włączenia maszyny, etykietę nazwy hosta oraz zegar i
kalendarz.

Inne funkcje:
- Samoskalujące się linie siatki o konfigurowanej gęstości
- Wyświetlacze imitujące diody LED dla interfejsów sieciowych
- Narzędzie gui do konfiguracji rozmiarów wykresów i rozdzielczości

%description -l pt_BR.UTF-8
O GKrellM mostra gráficos com dados sobre CPUs, carga da máquina,
discos e todas as interfaces de rede ativas, automaticamente. Um botão
liga/desliga e um temporizador para a interface PPP estão presentes.
Monitores para uso de memória e área de troca, sistemas de arquivos,
conexões Internet, para a bateria de computadores portáteis, para
caixas de correio no estilo mbox e para a temperatura da CPU. Também
inclui um monitor de tempo de atividade da máquina, um rótulo como o
nome da máquina e um relógio e calendário.

%description -l ru.UTF-8
GKrellM отображает графики для SMP CPU, загрузки, дисков и всех
активных сетевых интерфейсов автоматически. Есть кнопка on/off и
таймер времени онлайн для PPP интерфейса. Есть мониторы оперативной
памяти и swap, файловых систем, обращений из интернета, APM, почтовых
ящиков и температуры CPU. Включает также монитор uptime, метку имени
хоста, часы и календарь.

%description -l uk.UTF-8
GKrellM відображає графіки для SMP CPU, завантаження, дисків та всіх
активних мережевих інтерфейсів автоматично. Є кнопка on/off та таймер
онлайн-часу для PPP інтерфейсу. Є монітори оперативної пам'яті та
swap, файлових систем, звертань з інтернету, APM, поштових скриньок та
температури CPU. Включає також монітор uptime, мітку імені хоста,
годинник та календар.

%package gkrellmd
Summary:	gkrellmd - The GNU Krell Monitors Server
Summary(pl.UTF-8):	gkrellmd - Serwer monitorów GKrellM
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	glib2 >= 1:2.32
Requires:	rc-scripts

%description gkrellmd
gkrellmd listens for connections from gkrellm clients. When a gkrellm
client connects to a gkrellmd server all builtin monitors collect
their data from the server.

%description gkrellmd -l pl.UTF-8
gkrellmd nasłuchuje połączeń z klientów gkrellm. Gdy klient gkrellm
łączy się z serwerem gkrellmd, wszystkie wbudowane monitory pobierają
dane z serwera.

%package devel
Summary:	gkrellm include files
Summary(pl.UTF-8):	Pliki nagłówkowe do gkrellm
Summary(pt_BR.UTF-8):	Componentes para desenvolvimento com o gkrellm
Summary(ru.UTF-8):	Файлы C хедеров для GKrellM
Summary(uk.UTF-8):	Файли C хедерів для GKrellM
Group:		X11/Development/Libraries
Requires:	glib2-devel >= 1:2.32
Requires:	gtk+2-devel >= 2:2.4

%description devel
gkrellm header files for gkrellm development and plugin support.

%description devel -l pl.UTF-8
Pliki nagłówkowe do gkrellm.

%description devel -l pt_BR.UTF-8
Componentes para desenvolvimento de plugins para o gkrellm.

%description devel -l ru.UTF-8
Файлы C хедеров для GKrellM - для разработки и поддержки модулей.

%description devel -l uk.UTF-8
Файли C хедерів для GKrellM - для розробки та підтримки модулів.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%{__sed} -i -e 's,/lib/,/%{_lib}/,g' README server/gkrellmd.h src/gkrellm.h

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	PKGCONFIGDIR=%{_pkgconfigdir} \
	INSTALLROOT=%{_prefix} \
	%{?with_gnutls:without-ssl=yes} \
	%{!?with_lm_sensors:without-libsensors=yes}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins \
	$RPM_BUILD_ROOT%{_datadir}/gkrellm2/themes

%{__make} install \
	STRIP= \
	INSTALLROOT=$RPM_BUILD_ROOT%{_prefix} \
	CFGDIR=$RPM_BUILD_ROOT%{_sysconfdir} \
	PKGCONFIGDIR=$RPM_BUILD_ROOT%{_pkgconfigdir} \
	SERVICE_DIR=$RPM_BUILD_ROOT%{systemdunitdir}

install -Dp %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/gkrellmd
install -Dp %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/gkrellmd

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post gkrellmd
/sbin/chkconfig --add gkrellmd
%service gkrellmd restart

%preun gkrellmd
if [ "$1" = "0" ]; then
	%service gkrellmd stop
	/sbin/chkconfig --del gkrellmd
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changelog* README Themes.html
%attr(755,root,root) %{_bindir}/gkrellm
%{_mandir}/man1/gkrellm.1*
%dir %{_libdir}/gkrellm2
%dir %{_libdir}/gkrellm2/plugins
%dir %{_datadir}/gkrellm2
%dir %{_datadir}/gkrellm2/themes
%{_datadir}/metainfo/net.srcbox.gkrellm.GKrellM.metainfo.xml
%{_desktopdir}/gkrellm.desktop
%{_iconsdir}/hicolor/*x*/apps/gkrellm.png

%files gkrellmd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gkrellmd
%{_mandir}/man1/gkrellmd.1*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gkrellmd.conf
%attr(754,root,root) /etc/rc.d/init.d/gkrellmd
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/gkrellmd
%{systemdunitdir}/gkrellmd.service

%files devel
%defattr(644,root,root,755)
%{_includedir}/gkrellm2
%{_pkgconfigdir}/gkrellm.pc
