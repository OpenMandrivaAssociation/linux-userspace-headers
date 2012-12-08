echo $PWD
read VERSION PATCHLEVEL SUBLEVEL <<EOF
$(echo %{kver} |awk -F. '{print $1, " ", $2, " ", $3}')
EOF
LINUX_VERSION_CODE=$(expr $VERSION \* 65536 + $PATCHLEVEL \* 256 + $SUBLEVEL)

cat <<EOF > linux/version.h
#ifdef __KERNEL__
#error "======================================================="
#error "You should not include /usr/include/{linux,asm}/ header"
#error "files directly for the compilation of kernel modules."
#error ""
#error "To build kernel modules please do the following:"
#error ""
#error " o Have the kernel devel installed which matches the"
#error "   kernel you want to build for"
#error ""
#error " o Make sure that the symbolic link"
#error "   /lib/modules/\`uname -r\`/build exists and points to"
#error "   the matching kernel directory"
#error ""
#error " o When compiling, make sure to use the following"
#error "   compiler option to use the correct include files:"
#error ""
#error "   -I/lib/modules/\`uname -r\`/build/include"
#error ""
#error "   instead of"
#error ""
#error "   -I/usr/include/linux"
#error ""
#error "   Please adjust the Makefile accordingly."
#error "======================================================="
#else
#define LINUX_VERSION_CODE ${LINUX_VERSION_CODE}
#define KERNEL_VERSION(a,b,c) (((a) << 16) + ((b) << 8) + (c))
#endif
EOF
