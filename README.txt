# https://codingforseo.com/blog/extract-links-with-lynx

# on Fedora, install lynx command via dnf install lynx

We built the initial jakartaspecs.txt with the following two commands to define and use extract_links
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

Then we downloaded a few specs via:

python ./process.py

A bit of coding to automatically go through the specification links from jakartaeespecs.txt would be actually crawling through the specs instead of hard coding the downloads.  That is the next step if we use lynx.
