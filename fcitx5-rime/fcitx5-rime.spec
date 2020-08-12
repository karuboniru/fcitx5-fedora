%global forgeurl https://github.com/fcitx/fcitx5-rime
%global commit   e4fc60043e8c608d344b7f7b3e83116a81d89318
%forgemeta


Name:           fcitx5-rime
Version:        0
Release:        0.1%{?dist}
Summary:        fcitx5
License:        GPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}


BuildRequires:  cmake, extra-cmake-modules
BuildRequires:  gcc-c++, make, ninja-build, gettext-devel
BuildRequires:  fcitx5-devel, pkgconf, librime-devel
BuildRequires:  brise 
Requires:       fcitx5

%description
The fcitx5-rime package (still in testing!)

%prep
%forgesetup

%build
%cmake -GNinja
%cmake_build 

%install
%cmake_install

%find_lang %{name}

%check
%ctest

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/*
%{_datadir}/fcitx5/*
%{_datadir}/icons/hicolor/*/*/*


%changelog
