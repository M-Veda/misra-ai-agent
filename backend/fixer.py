import re

def fix_common_issues(code):

    # Fix assignment inside if
    code = re.sub(
        r'if\s*\((\w+)\s*=\s*(\d+)\)',
        r'if (\1 == \2)',
        code
    )

    # Fix array bounds
    code = code.replace("i <= 5", "i < 5")

    # Replace gets safely
    code = code.replace(
        "gets(ptr);",
        """
    if(ptr != NULL)
    {
        fgets(ptr, 10, stdin);
    }
"""
    )

    # Fix unsafe printf
    code = code.replace(
        "printf(ptr);",
        'printf("%s", ptr);'
    )

    # Fix return statement
    code = code.replace(
        "return;",
        "return 0;"
    )

    # Add static linkage
    code = code.replace(
        "void func(int a)",
        "static void func(int a)"
    )

    # Replace unused array assignment
    code = code.replace(
        "arr[i] = i * 10;",
        'printf("%d\\n", i * 10);'
    )

    # Remove unused array declaration
    code = code.replace(
        "int arr[5];",
        ""
    )

    return code