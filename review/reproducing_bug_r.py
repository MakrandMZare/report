import sys
sys.path.insert(0, '/root/hypothesis-llm/envs/tokenizers_env/lib/python3.13/site-packages')
from tokenizers.tools import Annotation, EncodingVisualizer

annotations = [Annotation(0, 5, "test_label")]
colors = EncodingVisualizer.calculate_label_colors(annotations)
color = colors["test_label"]

print(f"Generated color: '{color}'")
assert color.endswith(')'), f"Missing closing parenthesis in HSL: {color}"