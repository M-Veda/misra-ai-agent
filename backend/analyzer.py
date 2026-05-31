import subprocess

def run_cppcheck(file_path):

    command = [
        "cppcheck",
        "--enable=all",
        "--std=c99",
        file_path
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    errors = []

    for line in result.stderr.splitlines():

        if (
            "error:" in line or
            "warning:" in line or
            "style:" in line
        ):
            errors.append(line)

    return "\n".join(errors)