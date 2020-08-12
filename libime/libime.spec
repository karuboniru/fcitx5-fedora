%global forgeurl0 https://github.com/fcitx/libime
%global commit0   a108d15b06f0885f2fcc95d035614665392bc83b

%global forgeurl1 https://github.com/kpu/kenlm
%global commit1   96d303cfb1a0c21b8f060dbad640d7ab301c019a

%global _lm_sc_ver 20140820
%global _dict_ver  20200715

%forgemeta -a

Name:       libime  
Version:    0
License:    GPLv2
Release:    0.1%{?dist}
Summary:    This is a library to support generic input method implementation.
URL:        %{forgeurl0}
Source0:    %{forgesource0}
Source1:    %{forgesource1}
Source2:    https://download.fcitx-im.org/data/lm_sc.3gm.arpa-%{_lm_sc_ver}.tar.bz2
Source3:    https://download.fcitx-im.org/data/dict.utf8-%{_dict_ver}.tar.xz
Source4:    https://download.fcitx-im.org/data/table.tar.gz

BuildRequires: cmake, make, ninja-build, gcc-c++
BuildRequires: fcitx5-devel, boost-devel, extra-cmake-modules
BuildRequires: python3, doxygen, zlib-devel, bzip2-devel
BuildRequires: xz-devel, eigen3-devel

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
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/libime


%files devel
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_includedir}/LibIME



%changelog
* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1
- initial package
