--- a/tokenizers/tools/visualizer.py
+++ b/tokenizers/tools/visualizer.py
@@ -175,7 +175,7 @@ class EncodingVisualizer:
         colors = {}

         for label in sorted(labels):  # sort so we always get the same colors for a given set of labels
-            colors[label] = f"hsl({h},{s}%,{l}%"
+            colors[label] = f"hsl({h},{s}%,{l}%)"
             h += h_step
         return colors