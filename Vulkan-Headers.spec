#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Vulkan-Headers
Version  : 1.3.236
Release  : 138
URL      : https://github.com/KhronosGroup/Vulkan-Headers/archive/v1.3.236/Vulkan-Headers-1.3.236.tar.gz
Source0  : https://github.com/KhronosGroup/Vulkan-Headers/archive/v1.3.236/Vulkan-Headers-1.3.236.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: Vulkan-Headers-data = %{version}-%{release}
Requires: Vulkan-Headers-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

%description
# Vulkan-Headers
Vulkan header files and API registry
The contents of this repository are largely obtained from other repositories
and are collected, coordinated, and curated here.

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


%package dev32
Summary: dev32 components for the Vulkan-Headers package.
Group: Default
Requires: Vulkan-Headers-data = %{version}-%{release}
Requires: Vulkan-Headers-dev = %{version}-%{release}

%description dev32
dev32 components for the Vulkan-Headers package.


%package license
Summary: license components for the Vulkan-Headers package.
Group: Default

%description license
license components for the Vulkan-Headers package.


%prep
%setup -q -n Vulkan-Headers-1.3.236
cd %{_builddir}/Vulkan-Headers-1.3.236

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670264392
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build32
pushd clr-build32
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
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
export SOURCE_DATE_EPOCH=1670264392
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Vulkan-Headers
cp %{_builddir}/Vulkan-Headers-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/Vulkan-Headers/2b8b815229aa8a61e483fb4ba0588b8b6c491890
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
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/vulkan/registry/apiconventions.py
/usr/share/vulkan/registry/cgenerator.py
/usr/share/vulkan/registry/generator.py
/usr/share/vulkan/registry/genvk.py
/usr/share/vulkan/registry/profiles/VP_KHR_roadmap_2022.json
/usr/share/vulkan/registry/reg.py
/usr/share/vulkan/registry/spec_tools/conventions.py
/usr/share/vulkan/registry/spec_tools/util.py
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
/usr/include/vulkan/vk_sdk_platform.h
/usr/include/vulkan/vulkan.h
/usr/include/vulkan/vulkan.hpp
/usr/include/vulkan/vulkan_android.h
/usr/include/vulkan/vulkan_beta.h
/usr/include/vulkan/vulkan_core.h
/usr/include/vulkan/vulkan_directfb.h
/usr/include/vulkan/vulkan_enums.hpp
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
/usr/include/vulkan/vulkan_wayland.h
/usr/include/vulkan/vulkan_win32.h
/usr/include/vulkan/vulkan_xcb.h
/usr/include/vulkan/vulkan_xlib.h
/usr/include/vulkan/vulkan_xlib_xrandr.h
/usr/lib64/cmake/VulkanHeaders/VulkanHeadersConfig.cmake
/usr/lib64/cmake/VulkanHeaders/VulkanHeadersConfigVersion.cmake

%files dev32
%defattr(-,root,root,-)
/usr/lib32/cmake/VulkanHeaders/VulkanHeadersConfig.cmake
/usr/lib32/cmake/VulkanHeaders/VulkanHeadersConfigVersion.cmake

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Vulkan-Headers/2b8b815229aa8a61e483fb4ba0588b8b6c491890
