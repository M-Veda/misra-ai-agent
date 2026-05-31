from analyzer import run_cppcheck

def validate_code(file_path):

    report = run_cppcheck(file_path)

    if report.strip() == "":
        return True, "No issues found."

    return False, report