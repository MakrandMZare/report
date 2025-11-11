from requests.sessions import merge_setting

# Case 1: Both arguments are dicts - None values ARE removed
result1 = merge_setting({'a': 1, 'b': None}, {'c': 2})
print(f"Both dicts: {result1}")
print(f"Has None values: {None in result1.values()}")

# Case 2: Session setting is None - None values are NOT removed
result2 = merge_setting({'a': 1, 'b': None}, None)
print(f"\nSession None: {result2}")
print(f"Has None values: {None in result2.values()}")

# Case 3: Request setting is None - None values are NOT removed
result3 = merge_setting(None, {'a': 1, 'b': None})
print(f"\nRequest None: {result3}")
print(f"Has None values: {None in result3.values()}")