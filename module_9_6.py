def all_variants(text):
    i = 0
    while i < len(text):
        yield text[i]
        i += 1



a = all_variants("abc")
for i in a:
    print(i)
