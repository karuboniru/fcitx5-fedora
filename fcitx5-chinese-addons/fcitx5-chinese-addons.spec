%global forgeurl https://github.com/fcitx/fcitx5-chinese-addons
%global commit   ef9beb76e563cae1da7eb9cdea4ce0d916e2e700
%forgemeta
%global dictver 20121124

Name:           fcitx5-chinese-addons
Version:        0
Release:        0.1%{?dist}
Summary:        Chinese related addon for fcitx5
License:        GPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}
Source1:        https://download.fcitx-im.org/data/py_table-%{dictver}.tar.gz
Source2:        https://download.fcitx-im.org/data/py_stroke-%{dictver}.tar.gz


BuildRequires:  cmake, extra-cmake-modules
BuildRequires:  gcc-c++, make
BuildRequires:  ninja-build, boost-devel, fcitx5-devel
BuildRequires:  curl-devel, fmt-devel, gettext-devel
BuildRequires:  fcitx5-qt-devel, qt5-qtwebkit-devel
BuildRequires:  qt5-qtwebengine-devel, libime-devel
BuildRequires:  opencc-devel, fcitx5-lua-devel
Requires:       fcitx5

%description
This provides pinyin and table input method
support for fcitx5. Released under LGPL-2.1+.

im/pinyin/emoji.txt is derived from Unicode 
CLDR with modification.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
devel files for fcitx5-chinese-addons

%prep
%forgesetup
ln -s %{S:1} modules/pinyinhelper
ln -s %{S:2} modules/pinyinhelper

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
%{_bindir}/scel2org5
%{_libdir}/fcitx5/*
%{_datadir}/fcitx5/*
%{_datadir}/icons/hicolor/*/apps/*


%files devel
%{_includedir}/Fcitx5/*
%{_libdir}/cmake/*

%changelog
* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200812gitef9beb7
- initial package

