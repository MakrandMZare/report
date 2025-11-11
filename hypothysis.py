from hypothesis import given, strategies as st
import tqdm.cli
from tqdm.cli import TqdmTypeError

@given(st.sampled_from(['\\\\', '\\\\\\\\', '\\\\n', '\\\\t']))
def test_cast_chr_backslash_sequences(escape):
    """Test that backslash escape sequences are handled correctly"""
    if escape == '\\\\':
        # This should work but currently fails
        result = tqdm.cli.cast(escape, 'chr')
        assert result == b'\\'
    else:
        # These compound sequences also fail
        try:
            result = tqdm.cli.cast(escape, 'chr')
        except TqdmTypeError:
            pass