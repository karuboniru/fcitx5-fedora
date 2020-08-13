%global forgeurl https://github.com/fcitx/fcitx5-lua
%global commit   d705404964d4842998be17cd53dd29d2f78a4144
%forgemeta

Name:           fcitx5-lua
Version:        0
Release:        0.1%{?dist}
Summary:        Lua support for fcitx
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}


BuildRequires:  cmake, extra-cmake-modules
BuildRequires:  gcc-c++, lua-devel
BuildRequires:  ninja-build, fcitx5-devel
BuildRequires:  gettext-devel
Requires:       fcitx5

%description
Lua support for fcitx.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Devel files for fcitx5-lua

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
%{_libdir}/fcitx5/luaaddonloader.so
%{_datadir}/fcitx5/*

%files devel
%{_includedir}/Fcitx5/*
%{_libdir}/cmake/*


%changelog
* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200812gitd705404
- initial package
