Summary:	Multiple stacked system monitors: 1 process
Summary(pl):	Zestaw wielu monitorСw systemu(Сw) w jednym procesie
Summary(pt_BR):	MonitoraГЦo de atividades do sistema
Summary(ru):	GKrellM - это стек системных мониторов в рамках одного процесса
Summary(uk):	GKrellM - це стек системних мон╕тор╕в у рамках одного процесу
Name:		gkrellm
Version:	2.1.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://web.wt.net/~billw/gkrellm/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-paths_fix.patch
Icon:		gkrellm.xpm
URL:		http://www.gkrellm.net/
BuildRequires:	glib2-devel >= 2.1.3
BuildRequires:	gtk+2-devel >= 2.1.3
BuildRequires:	gettext-devel
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
GKrellM automatycznie wyswietla wykresy aktywno╤ci SMP CPU,
obci╠©enia, dysku oraz aktywnych interfejsСw sieciowych. Jest rСwnie©
przycisk wyЁ╠cznika, czasomierz dla interfejsu PPP, mierniki
wykorzystania pamiЙci oraz partycji wymiany, wy╤wietlacz czasy, ktСry
upЁyn╠Ё od wЁ╠czenia maszyny, etykietЙ nazwy hosta oraz zegar i
kalendarz. Inne funkcje:

 - Samoskaluj╠ce sie linie siatki o konfigurowanej gЙsto╤ci
 - Wy╤wietlacze imitujace diody LED dla interfejsСw sieciowych
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

%package devel
Summary:	gkrellm include files
Summary(pl):	Pliki nagЁСwkowe do gkrellm
Summary(pt_BR):	Componentes para desenvolvimento com o gkrellm
Summary(ru):	Файлы C хедеров для GKrellM
Summary(uk):	Файли C хедер╕в для GKrellM
Group:		X11/Development/Libraries
Requires:	gtk+2-devel

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
%patch -p1

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_includedir}/gkrellm2} \
	$RPM_BUILD_ROOT{%{_libdir},%{_datadir}}/gkrellm2 \
	$RPM_BUILD_ROOT{%{_applnkdir}/System,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/locale

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_bindir} \
	INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	LOCALEDIR=$RPM_BUILD_ROOT%{_datadir}/locale

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/System
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files  -f %{name}.lang
%defattr(644,root,root,755)
%doc Changelog* README Themes.html
%attr(755,root,root) %{_bindir}/gkrellm
%attr(755,root,root) %{_bindir}/gkrellmd
%{_mandir}/man1/*
%dir %{_libdir}/gkrellm2
%dir %{_datadir}/gkrellm2
%{_applnkdir}/System/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
