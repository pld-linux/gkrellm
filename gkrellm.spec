Summary:	Multiple stacked system monitors: 1 process
Summary(pl):	Zestaw wielu monitorÛw systemu(Ûw) w jednym procesie
Summary(pt_BR):	MonitoraÁ„o de atividades do sistema
Name:		gkrellm
Version:	1.2.3
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
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
GKrellM automatycznie wyswietla wykresy aktywno∂ci SMP CPU,
obci±øenia, dysku oraz aktywnych interfejsÛw sieciowych. Jest rÛwnieø
przycisk wy≥±cznika, czasomierz dla interfejsu PPP, mierniki
wykorzystania pamiÍci oraz partycji wymiany, wy∂wietlacz czasy, ktÛry
up≥yn±≥ od w≥±czenia maszyny, etykietÍ nazwy hosta oraz zegar i
kalendarz. Inne funkcje:

 - Samoskaluj±ce sie linie siatki o konfigurowanej gÍsto∂ci
 - Wy∂wietlacze imitujace diody LED dla interfejsÛw sieciowych
 - NarzÍdzie gui do konfiguracji rozmiarÛw wykresÛw i rozdzielczo∂ci

%description -l pt_BR
O GKrellM mostra gr·ficos com dados sobre CPUs, carga da m·quina,
discos e todas as interfaces de rede ativas, automaticamente. Um bot„o
liga/desliga e um temporizador para a interface PPP est„o presentes.
Monitores para uso de memÛria e ·rea de troca, sistemas de arquivos,
conexıes Internet, para a bateria de computadores port·teis, para
caixas de correio no estilo mbox e para a temperatura da CPU. TambÈm
inclui um monitor de tempo de atividade da m·quina, um rÛtulo como o
nome da m·quina e um relÛgio e calend·rio.

%package devel
Summary:	gkrellm include files
Summary(pl):	Pliki nag≥Ûwkowe do gkrellm
Summary(pt_BR):	Componentes para desenvolvimento com o gkrellm
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	gtk+-devel
Requires:	imlib-devel

%description devel
gkrellm header files for gkrellm development and plugin support.

%description -l pl devel
Pliki nag≥Ûwkowe do gkrellm.

%description -l pt_BR devel
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
