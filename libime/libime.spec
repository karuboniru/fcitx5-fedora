%global forgeurl0 https://github.com/fcitx/libime
%global commit0   a108d15b06f0885f2fcc95d035614665392bc83b

# KenLM is used as submodule in upstream
%global forgeurl1 https://github.com/kpu/kenlm
%global commit1   96d303cfb1a0c21b8f060dbad640d7ab301c019a

%global _lm_sc_ver 20140820
%global _dict_ver  20200715

%forgemeta -a

Name:       libime  
Version:    0
# both kenlm and libime are released under LGPL2+
License:    LGPLv2+
Release:    0.2%{?dist}
Summary:    This is a library to support generic input method implementation
URL:        %{forgeurl0}
Source0:    %{forgesource0}
Source1:    %{forgesource1}
Source2:    https://download.fcitx-im.org/data/lm_sc.3gm.arpa-%{_lm_sc_ver}.tar.bz2
Source3:    https://download.fcitx-im.org/data/dict.utf8-%{_dict_ver}.tar.xz
Source4:    https://download.fcitx-im.org/data/table.tar.gz

BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: fcitx5-devel
BuildRequires: boost-devel
BuildRequires: extra-cmake-modules
BuildRequires: python3
BuildRequires: doxygen
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(eigen3)


%description
This is a library to support generic input method implementation.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}

%prep
%forgeautosetup
rmdir %{_builddir}/%{name}-%{commit0}/src/libime/core/kenlm
tar xf %{S:1} --directory=%{_builddir}/%{name}-%{commit0}/src/libime/core/
ln -s %{_builddir}/%{name}-%{commit0}/src/libime/core/kenlm-%{commit1} \
    %{_builddir}/%{name}-%{commit0}/src/libime/core/kenlm
ln -s %{S:2} %{_builddir}/%{name}-%{commit0}/data
ln -s %{S:3} %{_builddir}/%{name}-%{commit0}/data
ln -s %{S:4} %{_builddir}/%{name}-%{commit0}/data

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_bindir}/libime_history
%{_bindir}/libime_pinyindict
%{_bindir}/libime_prediction
%{_bindir}/libime_slm_build_binary
%{_bindir}/libime_tabledict
%{_libdir}/libIMECore.so.0.*
%{_libdir}/libIMEPinyin.so.0.*
%{_libdir}/libIMETable.so.0.*
%{_datadir}/libime


%files devel
%{_libdir}/libIMECore.so
%{_libdir}/libIMEPinyin.so
%{_libdir}/libIMETable.so
%{_libdir}/cmake/LibIME*
%{_includedir}/LibIME/



%changelog
* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811gita108d15.s20200811git96d303c
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gita108d15.s20200811git96d303c
- initial package
