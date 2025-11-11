from hypothesis import given, strategies as st
from requests.sessions import merge_setting

@given(
    base_dict=st.one_of(st.none(), st.dictionaries(st.text(min_size=1), st.one_of(st.text(), st.none()))),
    override_dict=st.dictionaries(st.text(min_size=1), st.one_of(st.text(), st.none()))
)
def test_merge_setting_none_removal_consistency(base_dict, override_dict):
    """Test that merge_setting consistently removes None values from dicts"""
    result = merge_setting(override_dict, base_dict)

    if result is not None and isinstance(result, dict):
        # None values should always be removed from dictionary results
        assert None not in result.values()
Failing input: base_dict=None, override_dict={'0': None}

Reproducing the Bug
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