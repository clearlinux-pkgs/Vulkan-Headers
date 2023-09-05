#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : Vulkan-Headers
Version  : 1.3.263
Release  : 165
URL      : https://github.com/KhronosGroup/Vulkan-Headers/archive/v1.3.263/Vulkan-Headers-1.3.263.tar.gz
Source0  : https://github.com/KhronosGroup/Vulkan-Headers/archive/v1.3.263/Vulkan-Headers-1.3.263.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: Vulkan-Headers-data = %{version}-%{release}
Requires: Vulkan-Headers-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!--
SPDX-License-Identifier: Apache-2.0
-->
# Vulkan-Headers
Vulkan header files and API registry

%package data
Summary: data components for the Vulkan-Headers package.
Group: Data

%description data
data components for the Vulkan-Headers package.


%package dev
Summary: dev components for the Vulkan-Headers package.
Group: Development
Requires: Vulkan-Headers-data = %{version}-%{release}
Provides: Vulkan-Headers-devel = %{version}-%{release}
Requires: Vulkan-Headers = %{version}-%{release}

%description dev
dev components for the Vulkan-Headers package.


%package license
Summary: license components for the Vulkan-Headers package.
Group: Default

%description license
license components for the Vulkan-Headers package.


%prep
%setup -q -n Vulkan-Headers-1.3.263
cd %{_builddir}/Vulkan-Headers-1.3.263

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693952800
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build32
pushd clr-build32
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%cmake -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_INSTALL_LIBDIR=/usr/lib32 -DLIB_SUFFIX=32 ..
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
popd

%install
export SOURCE_DATE_EPOCH=1693952800
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Vulkan-Headers
cp %{_builddir}/Vulkan-Headers-%{version}/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/Vulkan-Headers/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/Vulkan-Headers-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/Vulkan-Headers/0e865724e451e18b1bdf69664f3df551cf9c3c73 || :
pushd clr-build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*
/usr/share/vulkan/registry/apiconventions.py
/usr/share/vulkan/registry/cgenerator.py
/usr/share/vulkan/registry/generator.py
/usr/share/vulkan/registry/genvk.py
/usr/share/vulkan/registry/parse_dependency.py
/usr/share/vulkan/registry/profiles/VP_KHR_roadmap_2022.json
/usr/share/vulkan/registry/reg.py
/usr/share/vulkan/registry/spec_tools/conventions.py
/usr/share/vulkan/registry/spec_tools/util.py
/usr/share/vulkan/registry/stripAPI.py
/usr/share/vulkan/registry/validusage.json
/usr/share/vulkan/registry/video.xml
/usr/share/vulkan/registry/vk.xml
/usr/share/vulkan/registry/vkconventions.py

%files dev
%defattr(-,root,root,-)
/usr/include/vk_video/vulkan_video_codec_h264std.h
/usr/include/vk_video/vulkan_video_codec_h264std_decode.h
/usr/include/vk_video/vulkan_video_codec_h264std_encode.h
/usr/include/vk_video/vulkan_video_codec_h265std.h
/usr/include/vk_video/vulkan_video_codec_h265std_decode.h
/usr/include/vk_video/vulkan_video_codec_h265std_encode.h
/usr/include/vk_video/vulkan_video_codecs_common.h
/usr/include/vulkan/vk_icd.h
/usr/include/vulkan/vk_layer.h
/usr/include/vulkan/vk_platform.h
/usr/include/vulkan/vulkan.cppm
/usr/include/vulkan/vulkan.h
/usr/include/vulkan/vulkan.hpp
/usr/include/vulkan/vulkan_android.h
/usr/include/vulkan/vulkan_beta.h
/usr/include/vulkan/vulkan_core.h
/usr/include/vulkan/vulkan_directfb.h
/usr/include/vulkan/vulkan_enums.hpp
/usr/include/vulkan/vulkan_extension_inspection.hpp
/usr/include/vulkan/vulkan_format_traits.hpp
/usr/include/vulkan/vulkan_fuchsia.h
/usr/include/vulkan/vulkan_funcs.hpp
/usr/include/vulkan/vulkan_ggp.h
/usr/include/vulkan/vulkan_handles.hpp
/usr/include/vulkan/vulkan_hash.hpp
/usr/include/vulkan/vulkan_ios.h
/usr/include/vulkan/vulkan_macos.h
/usr/include/vulkan/vulkan_metal.h
/usr/include/vulkan/vulkan_raii.hpp
/usr/include/vulkan/vulkan_screen.h
/usr/include/vulkan/vulkan_static_assertions.hpp
/usr/include/vulkan/vulkan_structs.hpp
/usr/include/vulkan/vulkan_to_string.hpp
/usr/include/vulkan/vulkan_vi.h
/usr/include/vulkan/vulkan_video.hpp
/usr/include/vulkan/vulkan_wayland.h
/usr/include/vulkan/vulkan_win32.h
/usr/include/vulkan/vulkan_xcb.h
/usr/include/vulkan/vulkan_xlib.h
/usr/include/vulkan/vulkan_xlib_xrandr.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Vulkan-Headers/0e865724e451e18b1bdf69664f3df551cf9c3c73
/usr/share/package-licenses/Vulkan-Headers/2b8b815229aa8a61e483fb4ba0588b8b6c491890
