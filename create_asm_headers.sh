[[ -n "$TARGET" ]] || TARGET="%_target_cpu"

unset ASM_BI

case "$TARGET" in
  sparc64)
    ASM64="asm-sparc64"
    ASM="asm-sparc"
    ASM_BI="asm-bi-sparc64"
    ;;
  x86_64|amd64)
    ASM="asm-x86"
    ;;
  s390x)
    ASM="asm-s390"
    ;;
  i*86|athlon)
    ASM="asm-x86"
    ;;
  ppc|ppc64)
    ASM="asm-powerpc"
    ;;
  *)
    ASM="asm-$TARGET"
esac

# Setup bi-arch headers
if [ -z "$ASM_BI" ]; then
	mv $ASM asm
else
	mv $ASM_BI asm
fi

# Clean-ups 
find . -maxdepth 1 -type d -name "asm-*" ! -name "$ASM" ! -name "$ASM64" ! -name "asm-generic" | xargs rm -rf

