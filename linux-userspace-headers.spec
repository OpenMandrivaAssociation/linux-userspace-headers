# kernel-headers are generated from mandriva kernel version %{kver}.%{ever}
%define kver 2.6.31
%define ever 0.rc5.2mnb

Summary:	Linux kernel header files for userspace
Name:   	linux-userspace-headers
Version:	%{kver}
Release:	%manbo_mkrel 0.rc5.2
License:	GPL
Group:  	System/Kernel and hardware
URL:    	http://www.kernel.org/
# kernel-headers tarball generated from mandriva kernel in svn with:
# make INSTALL_HDR_PATH=<path> headers_install_all
# find <path> -name ..install.cmd -exec rm -f {} \;
# find <path> -name .install -exec rm -f {} \;
Source0: 	kernel-headers-%{kver}.%{ever}.tar.lzma
Source1:	make_versionh.sh
Source2:	create_asm_headers.sh
# make headers_install_all has a bug which linux/{a.out.h,kvm.h} headers are not
# included. While kernel isn't patched or we change the way we create kernel
# headers tarball, patch it to include the missing headers
Patch0:		kernel-headers-kvm-a.out-missing-headers.patch
Conflicts:	glibc-devel <= 6:2.7-2mdv2008.1
Provides:	kernel-headers = 1:%{version}-%{release}
Obsoletes:	kernel-headers < 1:2.6.31-0.rc5.2
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
C header files from the Linux kernel. The header files define structures
and constants that are needed for building most standard programs.

This package is not suitable for building kernel modules.

%prep
%setup -q -n kernel-headers-%{kver}.%{ever}
%patch0 -p1
%{expand:%(%__cat %{_sourcedir}/make_versionh.sh 2>/dev/null)}
TARGET=%_target_cpu
%{expand:%(%__cat %{_sourcedir}/create_asm_headers.sh 2>/dev/null)}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_includedir}
cp -avf * %{buildroot}/%{_includedir}

# (cg) Remove files provided by libdrm
for hdr in drm.h drm_mode.h drm_sarea.h i915_drm.h mga_drm.h nouveau_drm.h \
           r128_drm.h radeon_drm.h savage_drm.h sis_drm.h via_drm.h;
do
	rm -f %{buildroot}%{_includedir}/drm/$hdr
done

# don't ship scsi.h while glibc provides it
rm -f %{buildroot}%{_includedir}/scsi/scsi.h

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{_includedir}/*
