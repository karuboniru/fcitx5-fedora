%global forgeurl https://github.com/fcitx/fcitx5
%global commit 87fb655852092f3ed2f79a3aac86fc6d5d92069f
%forgemeta
%global dictver 20121020
%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/fcitx5.conf
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

Name:           fcitx5
Version:        0
Release:        0.2%{?dist}
Summary:        Next generation of fcitx
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}
Source1:        https://download.fcitx-im.org/data/en_dict-%{dictver}.tar.gz
Source2:        fcitx5-xinput


BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cldr-emoji-annotation)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-imdkit)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xkeyboard-config)
Requires:       dbus-x11
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       imsettings
Requires:       hicolor-icon-theme
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
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-configtool.desktop
 
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

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
%{_bindir}/%{name}
%{_bindir}/%{name}-configtool
%{_bindir}/%{name}-remote
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-configtool.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*
%{_xinputconf}

%files devel
%{_includedir}/Fcitx5/
%{_libdir}/cmake/Fcitx5*
%{_libdir}/libFcitx5*.so
%{_libdir}/pkgconfig/Fcitx5*.pc

%files libs
%license LICENSES/LGPL-2.1-or-later.txt
%{_libdir}/%{name}/
%{_libdir}/libFcitx5*.so.*


%changelog
* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2
- change according to review suggestions

* Thu Aug 13 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200813git87fb655
- new version

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gitc87ea48
- initial package
