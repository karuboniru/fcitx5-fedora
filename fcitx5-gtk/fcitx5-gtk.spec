%global forgeurl https://github.com/fcitx/fcitx5-gtk
%global commit fc335f1d6be8820d021db282cf90b746dc7d9b7c
%forgemeta

Name:           fcitx5-gtk
Version:        0
Release:        0.1%{?dist}
Summary:        Gtk im module and glib based dbus client library
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}


BuildRequires:  cmake, extra-cmake-modules
BuildRequires:  gcc-c++, gobject-introspection-devel
BuildRequires:  ninja-build, fcitx5-devel, gtk2-devel, gtk3-devel
Requires:       fcitx5

%description
Gtk im module and glib based dbus client library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Devel files for fcitx5-gtk.

%prep
%forgesetup

%build
%cmake -GNinja
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
* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200812gitfc335f1
- initial package
