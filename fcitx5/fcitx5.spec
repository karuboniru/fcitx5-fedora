%global forgeurl https://github.com/fcitx/fcitx5
%global commit 87fb655852092f3ed2f79a3aac86fc6d5d92069f
%forgemeta
%global dictver 20121020
%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/fcitx5.conf

Name:           fcitx5
Version:        0
Release:        0.1%{?dist}
Summary:        Next generation of fcitx
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}
Source1:        https://download.fcitx-im.org/data/en_dict-%{dictver}.tar.gz
Source2:        fcitx5-xinput


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
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       imsettings
Requires(post):     %{_sbindir}/alternatives
Requires(postun):   %{_sbindir}/alternatives

%description
Fcitx 5 is a generic input method framework released under LGPL-2.1+.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Devel files for fcitx5

%package libs
Summary:        Shared libraries for Fcitx

%description libs
The %{name}-libs package provides shared libraries for Fcitx

%prep
%forgesetup
cp %{S:1} src/modules/spell/dict/

%build
%cmake
%cmake_build 

%install
%cmake_install
install -pm 644 -D %{S:2} %{buildroot}%{_xinputconf}

%find_lang %{name}

%check
%ctest

%post
%{_sbindir}/alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_xinputconf} 55 || :

%postun
if [ "$1" = "0" ]; then
  %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
  # if alternative was set to manual, reset to auto
  [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :
fi

%ldconfig_scriptlets libs

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-configtool.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*
%{_xinputconf}

%files devel
%{_includedir}/*
%{_libdir}/cmake/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files libs
%{_libdir}/%{name}
%{_libdir}/*.so.*


%changelog
* Thu Aug 13 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200813git87fb655
- new version

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200812gitc87ea48
- initial package
