Summary:	Multiple stacked system monitors: 1 process
Name:		gkrellm
Version:	1.0.6
Release:	1
License:	GPL
Vendor:		Bill Wilson <billw@wt.net>
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://web.wt.net/~billw/gkrellm/%{name}-%{version}.tar.gz
Patch0:		%{name}-paths_fix.patch
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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

%package devel
Summary:	gkrellm include files
Summary(pl):	Pliki nag³ówkowe do gkrellm
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki

%description devel
gkrellm header files for gkrellm development and plugin support.

%description -l pl devel
Pliki nag³ówkowe do gkrellm.

%prep
%setup -q
%patch -p1

%build
%{__make} CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_includedir}/gkrellm} \
	$RPM_BUILD_ROOT{%{_libdir},%{_datadir}}/gkrellm

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_bindir} \
	INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir}

gzip -9nf Changelog README Themes.html gkrellmrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gkrellm
%dir %{_libdir}/gkrellm
%dir %{_datadir}/gkrellm

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
