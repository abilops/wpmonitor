# What the Diff.py
# For analysing the diff
import difflib

def compareHTML(a,b):
	d = difflib.SequenceMatcher(a=a, b=b)
	return d.get_opcodes()
