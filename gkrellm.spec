# RPM spec file for GKrellm

Summary:	Multiple stacked system monitors: 1 process.
Name:		gkrellm
Version:	0.6.0
Release:	2a
Copyright:	GPL
Group:		X11/Utilities
Source:		Fhttp://web.wt.net/~billw/gkrellm/gkrellm-0.6.0-2.tgz
Vendor:		Bill Wilson <billw@wt.net>
Packager:	Gary Thomas <gdt@linuxppc.org>
#BuildRoot:	<Where to stage it>

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
%setup -q -n gkrellm-0.6.0-2

%build
make

%install
make install INSTALLDIR=/usr/X11R6

%files
%doc COPYRIGHT Changelog README TODO Themes
%doc examples gkrellm_theme.cfg gkrellmrc install-examples
/usr/X11R6/bin/gkrellm
