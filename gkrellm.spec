# RPM spec file for GKrellm

Summary:	Multiple stacked system monitors: 1 process.
Name:		gkrellm
Version:	0.6.8
Release:	1
License:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narz�dzia
Source0:	http://web.wt.net/~billw/gkrellm/%{name}-%{version}.tar.gz
Vendor:		Bill Wilson <billw@wt.net>
#BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q -n gkrellm-0.6.8

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALLDIR=%{_prefix}

%files
%defattr(644,root,root,755)
%doc COPYRIGHT Changelog README Themes
%doc examples gkrellm_theme.cfg gkrellmrc
%{_prefix}/bin/gkrellm
