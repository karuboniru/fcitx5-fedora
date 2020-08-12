%global forgeurl https://github.com/fcitx/fcitx5-qt
%global commit 3ddd34aa720cb4efd451a686c389d579b1914425
%forgemeta

Name:           fcitx5-qt
Version:        0
Release:        0.1%{?dist}
Summary:        fcitx5
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}
Patch0:         0001-use-usr-libexec-instead.patch


BuildRequires:  cmake, extra-cmake-modules
BuildRequires:  gcc-c++, make, libxkbcommon-x11-devel
BuildRequires:  ninja-build, fcitx5-devel, qt5-qtbase-devel
BuildRequires:  gettext-devel, qt5-qtbase-private-devel
Requires:       dbus-x11, fcitx5

%description
The fcitx5-qt package (still in testing!)

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
devel files for fcitx5-qt

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
%{_libdir}/*.so.*
%{_libdir}/fcitx5/*
%{_libdir}/qt5/plugins/platforminputcontexts/libfcitx5platforminputcontextplugin.so
%{_libexecdir}/fcitx5

%files devel
%{_includedir}/Fcitx5Qt5/*
%{_libdir}/cmake/*
%{_libdir}/*.so

%changelog

