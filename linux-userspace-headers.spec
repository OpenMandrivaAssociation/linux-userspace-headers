# kernel-headers are generated from mandriva kernel version %{kver}.%{ever}
%define kver 2.6.38.4
%define ever 1mnb2

Summary:	Linux kernel header files for userspace
Name:   	linux-userspace-headers
Version:	%{kver}
Release:	%manbo_mkrel 2
License:	GPL
Group:  	System/Kernel and hardware
URL:    	http://www.kernel.org/
# kernel-headers tarball generated from mandriva kernel in svn with:
# make INSTALL_HDR_PATH=<path> headers_install_all
# find <path> -name ..install.cmd -exec rm -f {} \;
# find <path> -name .install -exec rm -f {} \;
Source0: 	linux-userspace-headers-%{kver}.%{ever}.tar.xz
Source1:	make_versionh.sh
Source2:	create_asm_headers.sh
Conflicts:	glibc-devel <= 6:2.7-2mdv2008.1
Provides:	kernel-headers = 1:%{version}-%{release}
Obsoletes:	kernel-headers < 1:2.6.31-0.rc5.2
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
C header files from the Linux kernel. The header files define structures
and constants that are needed for building most standard programs.

This package is not suitable for building kernel modules.

%prep
%setup -q -n linux-userspace-headers-%{kver}.%{ever}
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

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{_includedir}/*


%changelog
* Sun Apr 24 2011 Thomas Backlund <tmb@mandriva.org> 2.6.38.4-1mnb2
+ Revision: 658359
- sync with kernel-2.6.38.4-1mnb2 (for ipset-6.4 support)

* Tue Mar 22 2011 Thomas Backlund <tmb@mandriva.org> 2.6.38.1-1
+ Revision: 647649
- sync with kernel-2.6.38.1-0.rc1.1

* Wed Jan 05 2011 Thomas Backlund <tmb@mandriva.org> 2.6.37-1mnb2
+ Revision: 628755
- sync headers with kernel-2.6.37-1mnb2

* Fri Oct 29 2010 Thomas Backlund <tmb@mandriva.org> 2.6.36-2mnb2
+ Revision: 590298
- drop P0 as make headers_install_all is now fixed in main kernel
- sync with main kernel-2.6.36-2mnb2

* Thu Oct 21 2010 Thomas Backlund <tmb@mandriva.org> 2.6.36-1mnb2
+ Revision: 587104
- sync with main kernel-2.6.36-1mnb2

* Thu Aug 05 2010 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 2.6.35-1mnb2
+ Revision: 566479
- Sync with latest mandriva kernel (2.6.35-1mnb).

* Thu Feb 25 2010 Thomas Backlund <tmb@mandriva.org> 2.6.33-1mnb2
+ Revision: 510967
- sync with main 2.6.33-1mnb

* Tue Feb 09 2010 Thomas Backlund <tmb@mandriva.org> 2.6.33-0.rc7.2mnb2
+ Revision: 503329
- remove kernel-only headers from patch0

* Tue Feb 09 2010 Thomas Backlund <tmb@mandriva.org> 2.6.33-0.rc7.1mnb2
+ Revision: 503247
- resync patch0 with kernel-2.6.33-0.rc7.1mnb
- sync with kernel-2.6.33-0.rc7.1mnb

* Thu Dec 17 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 2.6.32-1mnb2
+ Revision: 479753
- Sync with latest mandriva kernel (2.6.32.1-1mnb).
- Sync with latest mandriva kernel (2.6.31.2-0.rc1.1mnb).

* Fri Sep 11 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 2.6.31-1mnb2
+ Revision: 438461
- Sync with latest mandriva kernel (2.6.31-1mnb).

* Sat Aug 08 2009 Anssi Hannula <anssi@mandriva.org> 2.6.31-0.rc5.2mnb2
+ Revision: 411711
- rename from kernel-headers to linux-userspace-headers (previously some
  people were confused and thought this package had something to do with
  building kernel modules)
- clarify description
- rename from kernel-headers to linux-userspace-headers (previously some
  people were confused and thought this package had something to do with
  building kernel modules)

* Mon Aug 03 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.31-0.rc5.1mnb2
+ Revision: 408549
- Sync with latest mandriva kernel (2.6.31-0.rc5.2mnb).
- Don't ship /usr/include/scsi/scsi.h as glibc provides it for now.

* Wed Jul 29 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.31-0.rc4.1mnb2
+ Revision: 404093
- Sync with latest mandriva kernel (2.6.31-0.rc4.1mnb).

* Wed Jul 01 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.30-1mnb2
+ Revision: 391310
- Sync with latest mandriva kernel (2.6.30-2mnb).

* Tue May 26 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.30-0.rc7.1mnb2
+ Revision: 380022
- Sync with latest mandriva kernel (2.6.30-0.rc7.1mnb)
  * dropped kernel-headers-use-strict-types.patch (merged)
  * updated kernel-headers-kvm-a.out-missing-headers.patch

* Thu Mar 26 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.29-1mnb2
+ Revision: 361373
- Sync with latest mandriva kernel (2.6.29-1mnb).

* Tue Mar 24 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.29-0.rc7.4.2mnb2
+ Revision: 360904
- Remove hunk from kernel-headers-use-strict-types.patch which wrongly
  reverts upstream kernel header fix ("pkt_sched: type should be __u32
  in header").

* Thu Mar 12 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.29-0.rc7.4.1mnb2
+ Revision: 354093
- Sync with latest mandriva kernel (2.6.29-0.rc7.4.1mnb).
- Linux kernel has a bug which linux/{a.out.h,kvm.h} headers are not
  included when doing 'make headers_install_all'. While kernel isn't
  patched or we change the way we create kernel headers tarball/package,
  patch it to include the missing headers.

* Sat Feb 28 2009 Anssi Hannula <anssi@mandriva.org> 1:2.6.29-0.rc5.2mnb2
+ Revision: 346127
- fix headers brokenness by using strict types everywhere (fixes mixing
  of standard headers and many kernel headers that was broken recently,
  patchset from Jaswinder Singh Rajput's -tip core/header-fixes git
  tree, use-strict-types.patch)
- drop gnu-extensions.patch, the hunk is no longer visible to userspace

* Wed Feb 18 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.29-0.rc5.1mnb2
+ Revision: 342598
- Sync with latest mandriva kernel (2.6.29-0.rc5.1mnb).

* Thu Feb 05 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.28-3mnb2
+ Revision: 337687
- Sync with latest mandriva kernel (2.6.28.3-1mnb).

* Tue Jan 06 2009 Luiz Fernando Capitulino <lcapitulino@mandriva.com> 1:2.6.28-2mnb2
+ Revision: 326202
- Fix kernel and package version (they are 2mnb and not 1mnb)
- Sync with latest mandriva kernel (2.6.28-1mnb).

* Sun Nov 16 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.27.4-4mnb2
+ Revision: 303802
- No more need to conflict with libdrm-devel, when same files are being
  provided again by it.

* Thu Nov 13 2008 Colin Guthrie <cguthrie@mandriva.org> 1:2.6.27.4-3mnb2
+ Revision: 302921
- Do not include headers provided by libdrm as these are old versions
  that prevent the intel driver from building.

* Mon Nov 03 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.27.4-2mnb2
+ Revision: 299595
- Fix conflicts for libdrm-devel

* Mon Nov 03 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.27.4-1mnb2
+ Revision: 299579
- Sync with latest mandriva kernel (2.6.27.4-2mnb).
- Export drm headers that will not be exported anymore from libdrm.

* Thu Sep 25 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.27-4mnb2
+ Revision: 288031
- Sync with latest mandriva kernel (2.6.27-0.rc7.1.1mnb).

* Thu Sep 11 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.27-3mnb2
+ Revision: 283657
- Sync with latest Mandriva kernel (2.6.27-0.rc6.1mnb).

* Fri Sep 05 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.27-2mnb2
+ Revision: 281647
- Remove drm headers until libdrm stops to provide them.

* Fri Sep 05 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.27-1mnb2
+ Revision: 281382
- Sync with latest Mandriva kernel (2.6.27-0.rc5.7.1mnb).
- Cosmetics (spec file policy).

* Wed Jun 25 2008 Luiz Fernando Capitulino <lcapitulino@mandriva.com> 1:2.6.26-2mnb2
+ Revision: 229135
- Add ipt_psd.h and ipt_IFWLOG.h headers (needed by iptables)

* Wed Jun 25 2008 Luiz Fernando Capitulino <lcapitulino@mandriva.com> 1:2.6.26-1mnb2
+ Revision: 229043
- Update to 2.6.26-rc7 kernel headers

* Wed Mar 19 2008 Toshihiro Yamagishi <toshihiro@turbolinux.co.jp> 1:2.6.24-6mnb1
+ Revision: 188987
- replace %%mkrel with %%manbo_mkrel for ManboCore1

* Mon Feb 18 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.24-5mdv2008.1
+ Revision: 172125
- Revert last change, until I get an answer from linux-wireless about
  wireless.h being intentionally or not "broken" (may be software using
  it should manually include extra headers like told on comment because
  of glibc).

* Mon Feb 18 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.24-4mdv2008.1
+ Revision: 171663
- Don't ship wireless.h header, for userspace use the one from
  wireless-tools.

* Sat Feb 16 2008 Anssi Hannula <anssi@mandriva.org> 1:2.6.24-3mdv2008.1
+ Revision: 169304
- rebuild due to package loss

* Sun Feb 10 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.24-2mdv2008.1
+ Revision: 164741
- Fixed undefined LINUX_VERSION_CODE in /usr/include/linux/version.h

* Fri Feb 08 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:2.6.24-1mdv2008.1
+ Revision: 164135
- Use better versioning, and conflict with old glibc-devel releases that
  had kernel-headers included.
- import kernel-headers

