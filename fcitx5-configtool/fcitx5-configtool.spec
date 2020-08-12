%global forgeurl https://github.com/fcitx/fcitx5-configtool
%global commit ecd16e5f5bfeaded9bb59b88f484871d14e016e5
%forgemeta
%global translation_domain org.fcitx.fcitx5.kcm

Name:           fcitx5-configtool
Version:        0
Release:        0.1%{?dist}
Summary:        Configuration tools used by fcitx5
License:        GPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}
Patch0:         0001-use-usr-libexec-instead.patch


BuildRequires:  cmake, extra-cmake-modules
BuildRequires:  gcc-c++, make, libxkbcommon-x11-devel
BuildRequires:  ninja-build, fcitx5-devel, fcitx5-qt-devel
BuildRequires:  xkeyboard-config-devel, libX11-devel
BuildRequires:  gettext-devel, pkgconf, iso-codes-devel
BuildRequires:  libxkbcommon-x11-devel, qt5-qtx11extras-devel
BuildRequires:  kf5-kwidgetsaddons-devel, kf5-kirigami2-devel
BuildRequires:  kf5-kdeclarative-devel, kf5-kpackage-devel
BuildRequires:  kf5-ki18n-devel, kf5-kcoreaddons-devel
BuildRequires:  kf5-kitemviews-devel, libxkbfile-devel
Requires:       fcitx5

%description
Configuration tools used by fcitx5.

%prep
%forgeautosetup -p1

%build
%cmake -GNinja -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%cmake_build 

%install
%cmake_install

%find_lang %{name}
%find_lang %{translation_domain}


%files -f %{name}.lang -f %{translation_domain}.lang 
%license LICENSES/GPL-2.0-or-later.txt
%doc README
%{_bindir}/*
%{_libdir}/qt5/plugins/kcms/kcm_fcitx5.so
%{_datadir}/applications/kbd-layout-viewer5.desktop
%{_datadir}/kpackage/kcms/org.fcitx.fcitx5.kcm
%{_datadir}/kservices5/kcm_fcitx5.desktop
%{_datadir}/metainfo/org.fcitx.fcitx5.kcm.appdata.xml

%changelog
* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1
- initial package
