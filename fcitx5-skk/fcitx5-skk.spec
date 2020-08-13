%global forgeurl https://github.com/fcitx/fcitx5-skk
%global commit   02fb41d84d27969116ca878428978df2275c597a
%forgemeta

Name:       fcitx5-skk
Version:    0
Release:    0.1%{?dist}
Summary:    Japanese SKK (Simple Kana Kanji) Engine for Fcitx5
License:    GPLv3+
URL:        %{forgeurl}
Source:     %{forgesource}

BuildRequires:  fcitx5-devel, libskk-devel, gcc-c++
BuildRequires:  cmake, gettext, intltool, ninja-build
BuildRequires:  extra-cmake-modules, fcitx5-qt-devel
BuildRequires:  qt5-qtbase-devel, pkgconfig, glib2-devel
Requires:       fcitx5
Requires:       skkdic

%description
Fcitx5-skk is an SKK (Simple Kana Kanji) engine for Fcitx.  It provides
Japanese input method using libskk.

%prep
%forgesetup

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README.md 
%{_libdir}/fcitx5/qt5/libfcitx5-skk-config.so
%{_libdir}/fcitx5/skk.so
%{_datadir}/fcitx5/addon/skk.conf
%{_datadir}/fcitx5/inputmethod/skk.conf
%{_datadir}/fcitx5/skk/dictionary_list
%{_datadir}/icons/hicolor/64x64/apps/fcitx-skk.png

%changelog
* Thu Aug 13 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1
- Initial Package