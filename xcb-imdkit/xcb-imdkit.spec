%global forgeurl https://github.com/fcitx/xcb-imdkit
%global commit d6609a72465cf7e0479aea075a4d2e5d7ca018eb
%forgemeta

Name:       xcb-imdkit
Version:    0
Release:    0.1%{?dist}
Summary:    Input method development support for xcb
License:    LGPLv2
URL:        %{forgeurl}
Source:     %{forgesource}

BuildRequires:  cmake, extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libxcb-devel, xcb-util-devel, xcb-util-keysyms-devel

%description
xcb-imdkit is an implementation of xim protocol in xcb, 
comparing with the implementation of IMDkit with Xlib, 
and xim inside Xlib, it has less memory foot print, 
better performance, and safer on malformed client.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Devel files for xcb-imdkit

%prep
%forgesetup


%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSES/LGPL-2.1-only.txt
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/xcb-imdkit
%{_libdir}/cmake/XCBImdkit
%{_libdir}/*.so
%{_libdir}/pkgconfig/xcb-imdkit.pc

%changelog
* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200812gitd6609a7
- initial package

