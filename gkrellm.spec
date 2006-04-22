Summary:	Multiple stacked system monitors: 1 process
Summary(pl):	Zestaw wielu monitorСw systemu(Сw) w jednym procesie
Summary(pt_BR):	MonitoraГЦo de atividades do sistema
Summary(ru):	GKrellM - это стек системных мониторов в рамках одного процесса
Summary(uk):	GKrellM - це стек системних мон╕тор╕в у рамках одного процесу
Name:		gkrellm
Version:	2.2.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://members.dslextreme.com/users/billw/gkrellm/%{name}-%{version}.tar.gz
# Source0-md5:	27ef6961440db14ce54ecd4c8a841a08
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}d.init
Source4:	%{name}d.sysconf
Patch0:		%{name}-opt.patch
Patch1:		%{name}-home_etc.patch
URL:		http://www.gkrellm.net/
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gnutls-devel >= 1.2.5
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
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
GKrellM automatycznie wy╤wietla wykresy aktywno╤ci SMP CPU,
obci╠©enia, dysku oraz aktywnych interfejsСw sieciowych. Jest rСwnie©
przycisk wyЁ╠cznika, czasomierz dla interfejsu PPP, mierniki
wykorzystania pamiЙci oraz partycji wymiany, wy╤wietlacz czasy, ktСry
upЁyn╠Ё od wЁ╠czenia maszyny, etykietЙ nazwy hosta oraz zegar i
kalendarz.

Inne funkcje:
- Samoskaluj╠ce siЙ linie siatki o konfigurowanej gЙsto╤ci
- Wy╤wietlacze imituj╠ce diody LED dla interfejsСw sieciowych
- NarzЙdzie gui do konfiguracji rozmiarСw wykresСw i rozdzielczo╤ci

%description -l pt_BR
O GKrellM mostra grАficos com dados sobre CPUs, carga da mАquina,
discos e todas as interfaces de rede ativas, automaticamente. Um botЦo
liga/desliga e um temporizador para a interface PPP estЦo presentes.
Monitores para uso de memСria e Аrea de troca, sistemas de arquivos,
conexУes Internet, para a bateria de computadores portАteis, para
caixas de correio no estilo mbox e para a temperatura da CPU. TambИm
inclui um monitor de tempo de atividade da mАquina, um rСtulo como o
nome da mАquina e um relСgio e calendАrio.

%description -l ru
GKrellM отображает графики для SMP CPU, загрузки, дисков и всех
активных сетевых интерфейсов автоматически. Есть кнопка on/off и
таймер времени онлайн для PPP интерфейса. Есть мониторы оперативной
памяти и swap, файловых систем, обращений из интернета, APM, почтовых
ящиков и температуры CPU. Включает также монитор uptime, метку имени
хоста, часы и календарь.

%description -l uk
GKrellM в╕добража╓ граф╕ки для SMP CPU, завантаження, диск╕в та вс╕х
активних мережевих ╕нтерфейс╕в автоматично. ╢ кнопка on/off та таймер
онлайн-часу для PPP ╕нтерфейсу. ╢ мон╕тори оперативно╖ пам'ят╕ та
swap, файлових систем, звертань з ╕нтернету, APM, поштових скриньок та
температури CPU. Включа╓ також мон╕тор uptime, м╕тку ╕мен╕ хоста,
годинник та календар.

%package gkrellmd
Summary:	gkrellmd - The GNU Krell Monitors Server
Summary(pl):	gkrellmd - Serwer monitorСw GKrellM
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts

%description gkrellmd
gkrellmd listens for connections from gkrellm clients. When a gkrellm
client connects to a gkrellmd server all builtin monitors collect
their data from the server.

%description gkrellmd -l pl
gkrellmd nasЁuchuje poЁ╠czeЯ z klientСw gkrellm. Gdy klient gkrellm
Ё╠czy siЙ z serwerem gkrellmd, wszystkie wbudowane monitory pobieraj╠
dane z serwera.

%package devel
Summary:	gkrellm include files
Summary(pl):	Pliki nagЁСwkowe do gkrellm
Summary(pt_BR):	Componentes para desenvolvimento com o gkrellm
Summary(ru):	Файлы C хедеров для GKrellM
Summary(uk):	Файли C хедер╕в для GKrellM
Group:		X11/Development/Libraries
Requires:	gtk+2-devel >= 2:2.2.0

%description devel
gkrellm header files for gkrellm development and plugin support.

%description devel -l pl
Pliki nagЁСwkowe do gkrellm.

%description devel -l pt_BR
Componentes para desenvolvimento de plugins para o gkrellm.

%description devel -l ru
Файлы C хедеров для GKrellM - для разработки и поддержки модулей.

%description devel -l uk
Файли C хедер╕в для GKrellM - для розробки та п╕дтримки модул╕в.

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
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/gkrellmd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gkrellmd.conf

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_pkgconfigdir}/*
