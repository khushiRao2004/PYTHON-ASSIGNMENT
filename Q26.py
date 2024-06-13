def check_prefix_suffix(string, prefix, suffix):
    return string.startswith(prefix), string.endswith(suffix)

string = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")

starts_with_prefix, ends_with_suffix = check_prefix_suffix(string, prefix, suffix)
print(f"String starts with '{prefix}': {starts_with_prefix}")
print(f"String ends with '{suffix}': {ends_with_suffix}")
