# RPM spec file for GKrellm

Summary:	Multiple stacked system monitors: 1 process.
Name:		gkrellm
Version:	0.6.8
Release:	1
Copyright:	GPL
Group:		X11/Utilities
Source:		http://web.wt.net/~billw/gkrellm/gkrellm-0.6.8.tar.gz
Vendor:		Bill Wilson <billw@wt.net>
Packager:	Bill Wilson <billw@wt.net>
#BuildRoot:	<Where to stage it>

%description
GKrellM charts SMP CPU, load, Disk, and all active net interfaces
automatically. An on/off button and online timer for the PPP interface
is provided. Includes meters for memory and swap usage, an uptime
monitor, a hostname label, and a clock/calendar.
are provided.  Additional features are:

  * Autoscaling grid lines with configurable grid line resolution.
  * LED indicators for the net interfaces.
  * A gui popup for configuration of chart sizes and resolutions.

%prep
%setup -q -n gkrellm-0.6.8

%build
make

%install
make install INSTALLDIR=/usr/X11R6

%files
%doc COPYRIGHT Changelog README Themes
%doc examples gkrellm_theme.cfg gkrellmrc
/usr/X11R6/bin/gkrellm
