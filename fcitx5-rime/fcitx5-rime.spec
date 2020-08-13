%global forgeurl https://github.com/fcitx/fcitx5-rime
%global commit   e4fc60043e8c608d344b7f7b3e83116a81d89318
%forgemeta


Name:           fcitx5-rime
Version:        0
Release:        0.1%{?dist}
Summary:        RIME support for Fcitx
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}


BuildRequires:  cmake, extra-cmake-modules
BuildRequires:  gcc-c++, make, ninja-build, gettext-devel
BuildRequires:  fcitx5-devel, pkgconf, librime-devel
BuildRequires:  brise 
Requires:       fcitx5

%description
RIME(中州韻輸入法引擎) is mainly a Traditional Chinese 
input method engine.

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
* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200812gite4fc600
- initial package
