Summary:	Multiple stacked system monitors: 1 process.
Name:		gkrellm
Version:	0.6.1
Release:	1
Copyright:	GPL
Group:		X11/Utilities
Vendor:		Bill Wilson <billw@wt.net>
Source:		Fhttp://web.wt.net/~billw/gkrellm/%{name}-%{version}.tgz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GKrellM charts CPU, Disk, and all active net interfaces automatically.
An on/off button and online timer for the PPP interface is provided.
Meters for memory and swap usage as well as a system uptime monitor
are provided.  Additional features are:

  * Clicking on left or right frame slides GKrellM shut to gain screen space.
  * Autoscaling grid lines with configurable grid line resolution.
  * LED indicators for the net interfaces.
  * Configurable chart sizes.
  * 2 example alternate themes provided in /usr/doc/gkrellm/examples.

%prep
%setup -q

%build
make

%install
make install INSTALLDIR=/usr/X11R6

%files
%doc COPYRIGHT Changelog README TODO Themes
%doc examples gkrellm_theme.cfg gkrellmrc install-examples
/usr/X11R6/bin/gkrellm
