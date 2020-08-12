%global forgeurl https://github.com/fcitx/fcitx5
%global commit c87ea4885fca7b3f906f21e3b4bb5210dd37adc8
%forgemeta
%global dictver 20121020

Name:           fcitx5
Version:        0
Release:        0.1%{?dist}
Summary:        fcitx5
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}
Source1:        https://download.fcitx-im.org/data/en_dict-%{dictver}.tar.gz


BuildRequires:  cmake, extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  cairo-devel, enchant-devel, iso-codes-devel
BuildRequires:  mesa-libGL-devel, libxkbcommon-x11-devel
BuildRequires:  pango-devel, systemd-devel, systemd-rpm-macros
BuildRequires:  wayland-devel, wayland-protocols-devel, libxcb-devel
BuildRequires:  xcb-util-wm-devel, xcb-imdkit-devel, xcb-util-wm-devel
BuildRequires:  libxkbfile-devel, fmt-devel, gdk-pixbuf2-devel
BuildRequires:  cldr-emoji-annotation-devel, libuuid-devel
BuildRequires:  expat-devel, json-c-devel, xkeyboard-config-devel
BuildRequires:  xcb-util-keysyms-devel
Requires:       dbus-x11

%description
The fcitx5 package (still in testing!)

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
devel files for fcitx5

%prep
%forgesetup
cp %{S:1} src/modules/spell/dict/

%build
%cmake
%cmake_build 

%install
%cmake_install

%find_lang %{name}

%check
%ctest

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/*.so.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-configtool.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*

%files devel
%{_includedir}/*
%{_libdir}/cmake/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*



%changelog

