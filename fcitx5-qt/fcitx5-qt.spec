%global forgeurl https://github.com/fcitx/fcitx5-qt
%global commit 3ddd34aa720cb4efd451a686c389d579b1914425
%forgemeta
%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$


Name:           fcitx5-qt
Version:        0
Release:        0.2%{?dist}
Summary:        Qt library and IM module for fcitx5
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}
# upstream don't use /usr/libexec, patch to fix
Patch0:         0001-use-usr-libexec-instead.patch


BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(Fcitx5Utils)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui) 
BuildRequires:  gettext-devel
BuildRequires:  qt5-qtbase-private-devel

%description
Qt library and IM module for fcitx5.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fcitx5-devel

%description devel
Devel files for fcitx5-qt

%prep
%forgeautosetup -p1

%build
%cmake -GNinja -DENABLE_QT4=False
%cmake_build 

%install
%cmake_install

%find_lang %{name}


%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/libFcitx5Qt5DBusAddons.so.1
%{_libdir}/libFcitx5Qt5WidgetsAddons.so.2
%{_libdir}/libFcitx5Qt5DBusAddons.so.*.*
%{_libdir}/libFcitx5Qt5WidgetsAddons.so.*.*
%{_libdir}/fcitx5/qt5/libfcitx-quickphrase-editor5.so
%{_qt5_plugindir}/platforminputcontexts/libfcitx5platforminputcontextplugin.so
%{_libexecdir}/fcitx5/

%files devel
%{_includedir}/Fcitx5Qt5/
%{_libdir}/cmake/Fcitx5Qt5*
%{_libdir}/libFcitx5Qt5DBusAddons.so
%{_libdir}/libFcitx5Qt5WidgetsAddons.so

%changelog
* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811git3ddd34a
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811git3ddd34a
- initial package
