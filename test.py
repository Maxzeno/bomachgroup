import bleach

def strip_rich_text():
    rich_text = "<p>This is    <strong>rich     text&nbsp;</strong> with<p>&nbsp;</p> <em>tags</em>.</p>"
    rich_text = rich_text.replace('&nbsp;', '')

    text = bleach.clean(rich_text, tags=[], strip=True)
    cleaned_string = ' '.join(set(text.split()))
    return cleaned_string


print(strip_rich_text())

# help(bleach.clean)