Summary:	Multiple stacked system monitors: 1 process
Summary(pl):	Zestaw wielu monitorów systemu(ów) w jednym procesie
Summary(pt_BR):	Monitoração de atividades do sistema
Name:		gkrellm
Version:	1.2.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://web.wt.net/~billw/gkrellm/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-paths_fix.patch
Icon:		gkrellm.xpm
URL:		http://www.gkrellm.net/
BuildRequires:	glib-devel >= 1.2
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	imlib-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
GKrellM automatycznie wyswietla wykresy aktywno¶ci SMP CPU,
obci±¿enia, dysku oraz aktywnych interfejsów sieciowych. Jest równie¿
przycisk wy³±cznika, czasomierz dla interfejsu PPP, mierniki
wykorzystania pamiêci oraz partycji wymiany, wy¶wietlacz czasy, który
up³yn±³ od w³±czenia maszyny, etykietê nazwy hosta oraz zegar i
kalendarz. Inne funkcje:

 - Samoskaluj±ce sie linie siatki o konfigurowanej gêsto¶ci
 - Wy¶wietlacze imitujace diody LED dla interfejsów sieciowych
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

%package devel
Summary:	gkrellm include files
Summary(pl):	Pliki nag³ówkowe do gkrellm
Summary(pt_BR):	Componentes para desenvolvimento com o gkrellm
Group:		X11/Development/Libraries
Requires:	gtk+-devel
Requires:	imlib-devel

%description devel
gkrellm header files for gkrellm development and plugin support.

%description devel -l pl
Pliki nag³ówkowe do gkrellm.

%description devel -l pt_BR
Componentes para desenvolvimento de plugins para o gkrellm.

%prep
%setup -q
%patch -p1

%build
./enable_nls
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_includedir}/gkrellm} \
	$RPM_BUILD_ROOT{%{_libdir},%{_datadir}}/gkrellm \
	$RPM_BUILD_ROOT{%{_applnkdir}/System,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/locale

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_bindir} \
	INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	LOCALEDIR=$RPM_BUILD_ROOT%{_datadir}/locale

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/System
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf Changelog Changelog-plugins.html Changelog-themes.html \
	README Themes.html

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files  -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gkrellm
%{_mandir}/man1/*
%dir %{_libdir}/gkrellm
%dir %{_datadir}/gkrellm
%{_applnkdir}/System/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
