import os
import sys

# streamcables/*.py import each other by flat unqualified name (e.g. "import
# settings"), relying on that directory itself being on sys.path.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "streamcables"))
