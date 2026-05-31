FIX_PROMPT = """
Return ONLY corrected C code.

Fix:
- array out of bounds
- gets()
- assignment inside if
- null pointer risk
- static linkage issue

CODE:
{code}

ERRORS:
{report}
"""