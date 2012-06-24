Summary:	Multiple stacked system monitors: 1 process
Summary(pl):	Zestaw wielu monitor�w systemu(�w) w jednym procesie
Summary(pt_BR):	Monitora��o de atividades do sistema
Summary(ru):	GKrellM - ��� ���� ��������� ��������� � ������ ������ ��������
Summary(uk):	GKrellM - �� ���� ��������� ��Φ��Ҧ� � ������ ������ �������
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
GKrellM automatycznie wyswietla wykresy aktywno�ci SMP CPU,
obci��enia, dysku oraz aktywnych interfejs�w sieciowych. Jest r�wnie�
przycisk wy��cznika, czasomierz dla interfejsu PPP, mierniki
wykorzystania pami�ci oraz partycji wymiany, wy�wietlacz czasy, kt�ry
up�yn�� od w��czenia maszyny, etykiet� nazwy hosta oraz zegar i
kalendarz. Inne funkcje:

 - Samoskaluj�ce sie linie siatki o konfigurowanej g�sto�ci
 - Wy�wietlacze imitujace diody LED dla interfejs�w sieciowych
 - Narz�dzie gui do konfiguracji rozmiar�w wykres�w i rozdzielczo�ci

%description -l pt_BR
O GKrellM mostra gr�ficos com dados sobre CPUs, carga da m�quina,
discos e todas as interfaces de rede ativas, automaticamente. Um bot�o
liga/desliga e um temporizador para a interface PPP est�o presentes.
Monitores para uso de mem�ria e �rea de troca, sistemas de arquivos,
conex�es Internet, para a bateria de computadores port�teis, para
caixas de correio no estilo mbox e para a temperatura da CPU. Tamb�m
inclui um monitor de tempo de atividade da m�quina, um r�tulo como o
nome da m�quina e um rel�gio e calend�rio.

%description -l ru
GKrellM ���������� ������� ��� SMP CPU, ��������, ������ � ����
�������� ������� ����������� �������������. ���� ������ on/off �
������ ������� ������ ��� PPP ����������. ���� �������� �����������
������ � swap, �������� ������, ��������� �� ���������, APM, ��������
������ � ����������� CPU. �������� ����� ������� uptime, ����� �����
�����, ���� � ���������.

%description -l uk
GKrellM צ�������� ���Ʀ�� ��� SMP CPU, ������������, ���˦� �� �Ӧ�
�������� ��������� ��������Ӧ� �����������. � ������ on/off �� ������
������-���� ��� PPP ����������. � ��Φ���� ���������ϧ ���'�Ԧ ��
swap, �������� ������, �������� � ���������, APM, �������� �������� ��
����������� CPU. ������� ����� ��Φ��� uptime, ͦ��� ���Φ �����,
�������� �� ��������.

%package devel
Summary:	gkrellm include files
Summary(pl):	Pliki nag��wkowe do gkrellm
Summary(pt_BR):	Componentes para desenvolvimento com o gkrellm
Summary(ru):	����� C ������� ��� GKrellM
Summary(uk):	����� C ����Ҧ� ��� GKrellM
Group:		X11/Development/Libraries
Requires:	gtk+2-devel

%description devel
gkrellm header files for gkrellm development and plugin support.

%description devel -l pl
Pliki nag��wkowe do gkrellm.

%description devel -l pt_BR
Componentes para desenvolvimento de plugins para o gkrellm.

%description devel -l ru
����� C ������� ��� GKrellM - ��� ���������� � ��������� �������.

%description devel -l uk
����� C ����Ҧ� ��� GKrellM - ��� �������� �� Ц������� ����̦�.

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
