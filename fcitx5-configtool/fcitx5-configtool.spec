%global forgeurl https://github.com/fcitx/fcitx5-configtool
%global commit ecd16e5f5bfeaded9bb59b88f484871d14e016e5
%forgemeta
%global translation_domain org.fcitx.fcitx5.kcm

Name:           fcitx5-configtool
Version:        0
Release:        0.2%{?dist}
Summary:        Configuration tools used by fcitx5
License:        GPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}
# upstream don't use /usr/libexec, patch to fix
Patch0:         0001-use-usr-libexec-instead.patch


BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  fcitx5-qt-devel
BuildRequires:  gettext-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kirigami2-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kpackage-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kitemviews-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5Utils)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
Requires:       fcitx5
Requires:       kf5-filesystem


%description
Configuration tools used by fcitx5.

%prep
%forgeautosetup -p1

%build
%cmake_kf5 -GNinja
%cmake_build 

%install
%cmake_install
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/kservices5 \
  %{buildroot}%{_datadir}/kservices5/kcm_fcitx5.desktop
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/kbd-layout-viewer5.desktop

%find_lang %{name}
%find_lang %{translation_domain}


%files -f %{name}.lang -f %{translation_domain}.lang 
%license LICENSES/GPL-2.0-or-later.txt
%doc README
%{_bindir}/fcitx5-config-qt
%{_bindir}/kbd-layout-viewer5
%{_kf5_qtplugindir}/kcms/kcm_fcitx5.so
%{_datadir}/applications/kbd-layout-viewer5.desktop
%{_datadir}/kpackage/kcms/org.fcitx.fcitx5.kcm
%{_datadir}/kservices5/kcm_fcitx5.desktop
%{_metainfodir}/org.fcitx.fcitx5.kcm.appdata.xml

%changelog
* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811gitecd16e5
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gitecd16e5
- initial package
