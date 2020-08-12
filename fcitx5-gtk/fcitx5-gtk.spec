%global forgeurl https://github.com/fcitx/fcitx5-gtk
%global commit fc335f1d6be8820d021db282cf90b746dc7d9b7c
%forgemeta

Name:           fcitx5-gtk
Version:        0
Release:        1%{?dist}
Summary:        fcitx5
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}


BuildRequires:  cmake, extra-cmake-modules
BuildRequires:  gcc-c++, make, gobject-introspection-devel
BuildRequires:  ninja-build, fcitx5-devel, gtk2-devel, gtk3-devel
Requires:       dbus-x11, fcitx5

%description
The fcitx5-gtk package (still in testing!)

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
devel files for fcitx5-gtk

%prep
%forgesetup

%build
%cmake -GNinja -DENABLE_QT4=False
%cmake_build 

%install
%cmake_install

%files
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_datadir}/gir-1.0/FcitxG-1.0.gir
%{_libdir}/*.so.*
%{_libdir}/gtk-*/*/immodules/im-fcitx5.so
%{_libdir}/girepository-1.0/FcitxG-1.0.typelib

%files devel
%{_includedir}/Fcitx5/*
%{_libdir}/cmake/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog

