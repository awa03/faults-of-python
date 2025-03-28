def my_strip(text, chars=None):
    if not text: return ""
    if chars is None: chars = " \t\n\r"
    start = 0
    while start < len(text) and text[start] in chars: start += 1
    end = len(text)
    while end > start and text[end - 1] in chars: end -= 1
    return text[start:end]

def my_replace(text, old, new, count=-1):
    if not text or not old: return text
    result = []
    start = 0
    replacements = 0
    while True:
        pos = text.find(old, start)
        if pos == -1 or (count != -1 and replacements >= count):
            result.append(text[start:])
            break
        result.append(text[start:pos])
        result.append(new)
        start = pos + len(old)
        replacements += 1
    return ''.join(result)

def my_in(substring, text):
    if not substring: return True
    if not text: return False
    for i in range(len(text) - len(substring) + 1):
        found = True
        for j in range(len(substring)):
            if text[i + j] != substring[j]:
                found = False
                break
        if found: return True
    return False
