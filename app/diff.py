import difflib
import os

def compare_html(url, new_html):
    filename = f".cache_{url.replace('/', '_')}"
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            old_html = f.read()
    else:
        old_html = ""

    with open(filename, 'w') as f:
        f.write(new_html)

    diff = difflib.unified_diff(old_html.splitlines(), new_html.splitlines())
    return '\n'.join(diff)
