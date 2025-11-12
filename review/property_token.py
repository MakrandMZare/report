from hypothesis import given, strategies as st
import re
from tokenizers.tools import Annotation, EncodingVisualizer

@given(st.lists(st.text(min_size=1, max_size=20), min_size=1, max_size=10))
def test_calculate_label_colors_valid_hsl_format(labels):
    annotations = [Annotation(i*10, i*10+5, label) for i, label in enumerate(labels)]
    colors = EncodingVisualizer.calculate_label_colors(annotations)

    hsl_pattern = re.compile(r'^hsl\(\d+,\d+%,\d+%\)$')  # Correct HSL format with closing paren
    for label, color in colors.items():
        assert hsl_pattern.match(color), f"Invalid HSL format: '{color}'"