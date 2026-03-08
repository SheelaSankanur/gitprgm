def reverse_str(s):
    rev=" "
    for i in s:
        rev=i+rev
    return rev

print(reverse_str("hello"))