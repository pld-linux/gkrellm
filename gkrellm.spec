Summary:	Multiple stacked system monitors: 1 process
Summary(pl):	Zestaw wielu monitor�w systemu(�w) w jednym procesie
Summary(pt_BR):	Monitora��o de atividades do sistema
Summary(ru):	GKrellM - ��� ���� ��������� ��������� � ������ ������ ��������
Summary(uk):	GKrellM - �� ���� ��������� ��Φ��Ҧ� � ������ ������ �������
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
GKrellM automatycznie wy�wietla wykresy aktywno�ci SMP CPU,
obci��enia, dysku oraz aktywnych interfejs�w sieciowych. Jest r�wnie�
przycisk wy��cznika, czasomierz dla interfejsu PPP, mierniki
wykorzystania pami�ci oraz partycji wymiany, wy�wietlacz czasy, kt�ry
up�yn�� od w��czenia maszyny, etykiet� nazwy hosta oraz zegar i
kalendarz. Inne funkcje:

 - Samoskaluj�ce si� linie siatki o konfigurowanej g�sto�ci
 - Wy�wietlacze imituj�ce diody LED dla interfejs�w sieciowych
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

%package gkrellmd
Summary:	gkrellmd - The GNU Krell Monitors Server
Summary(pl):	gkrellmd - Serwer monitor�w GKrellM
Group:		Daemons
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig

%description gkrellmd
gkrellmd listens for connections from gkrellm clients.  When a gkrellm
client connects to a gkrellmd server all builtin monitors collect their
data from the server.

%description gkrellmd -l pl
gkrellmd nas�uchuje po��cze� z klient�w gkrellm.  Gdy klient gkrellm
��czy si� z serwerem gkrellmd, wszystkie wbudowane monitory pobieraj�
dane z serwera.

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
