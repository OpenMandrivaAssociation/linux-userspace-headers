#
# Deprecated: the new package providing kernel header files is named
# "kernel-headers" (surprise surprise).
#
%define kver 2.6.38.4

Summary:	Linux kernel header files for userspace
Name:   	linux-userspace-headers
Version:	%{kver}
Release:	%manbo_mkrel 2
License:	GPL
Group:  	System/Kernel and hardware
URL:    	http://www.kernel.org/
Requires:	kernel-headers >= %{kver}
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
C header files from the Linux kernel. The header files define structures
and constants that are needed for building most standard programs.

This package is not suitable for building kernel modules.

%files
%defattr(0644,root,root,0755)
