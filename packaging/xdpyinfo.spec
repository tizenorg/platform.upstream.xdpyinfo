%bcond_with x

Name:           xdpyinfo
Version:        1.3.1
Release:        1
License:        MIT
Summary:        Utility to display information about an X server
Url:            http://xorg.freedesktop.org/
Group:          Graphics/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1001: 	xdpyinfo.manifest
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(dmx)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xxf86dga)
BuildRequires:  pkgconfig(xxf86misc)
BuildRequires:  pkgconfig(xxf86vm)

%if !%{with x}
ExclusiveArch:
%endif

%description
xdpyinfo is a utility for displaying information about an X server.

It is used to examine the capabilities of a server, the predefined
values for various parameters used in communicating between clients
and the server, and the different types of screens, visuals, and X11
protocol extensions that are available.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%reconfigure
make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_bindir}/xdpyinfo
%{_mandir}/man1/xdpyinfo.1%{?ext_man}

%changelog
