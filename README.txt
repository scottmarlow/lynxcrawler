# https://codingforseo.com/blog/extract-links-with-lynx

# on Fedora, install lynx command via dnf install lynx


extract_links () {
    lynx --listonly \
    --nonumbers \
    --display_charset=utf-8 \
    --dump "$1" \
    | grep "^http" \
    | sort \
    | uniq
}


extract_links https://jakarta.ee/specifications > jakartaeespecs.txt
