Summary:	Multiple stacked system monitors: 1 process
Name:		gkrellm
Version:	0.10.5
Release:	1
License:	GPL
Vendor:		Bill Wilson <billw@wt.net>
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://web.wt.net/~billw/gkrellm/%{name}-%{version}.tar.gz
patch0:		%{name}-CFLAGS.patch
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
GKrellM automatycznie wyswietla wykresy aktywno�ci SMP CPU,
obci��enia, dysku oraz aktywnych interfejs�w sieciowych. Jest r�wnie�
przycisk wy��cznika, czasomierz dla interfejsu PPP, mierniki
wykorzystania pami�ci oraz partycji wymiany, wy�wietlacz czasy, kt�ry
up�yn�� od w��czenia maszyny, etykiet� nazwy hosta oraz zegar i
kalendarz. Inne funkcje:

 - Samoskaluj�ce sie linie siatki o konfigurowanej g�sto�ci
 - Wy�wietlacze imitujace diody LED dla interfejs�w sieciowych
 - Narz�dzie gui do konfiguracji rozmiar�w wykres�w i rozdzielczo�ci

%prep
%setup -q
%patch -p1

%build
%{__make} CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_includedir}/gkrellm}

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_bindir} \
	INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir}

gzip -9nf Changelog README gkrellmrc \
	Themes.html Changelog-plugins.html Changelog-themes.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gkrellm
%{_includedir}/*
