%global forgeurl https://github.com/fcitx/fcitx5-qt
%global commit 91a4b144c06487f54e05a70cea02d5b84f84563c
%forgemeta

Name:           fcitx5-qt
Version:        0
Release:        1%{?dist}
Summary:        fcitx5
License:        GPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}


BuildRequires:  cmake, extra-cmake-modules
BuildRequires:  gcc-c++, make, libxkbcommon-x11-devel
BuildRequires:  ninja-build, fcitx5-devel, qt5-qtbase-devel
BuildRequires:  gettext-devel
Requires:       dbus-x11, fcitx5

%description
The fcitx5-qt package (still in testing!)

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
devel files for fcitx5-qt

%prep
%forgesetup

%build
%cmake -GNinja -DENABLE_QT4=False
%cmake_build 

%install
%cmake_install

%find_lang %{name}


%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/*.so.*
%{_libdir}/fcitx5/*
%{_libdir}/qt5/plugins/platforminputcontexts/libfcitx5platforminputcontextplugin.so

%files devel
%{_includedir}/Fcitx5Qt5/*
%{_libdir}/cmake/*
%{_libdir}/*.so

%changelog

