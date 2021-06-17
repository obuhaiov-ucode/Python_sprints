import sys

def print_stderr(text: str):
    sys.stderr.write(f"ERROR| {text}.\n")

def print_stdout(text: str):
    sys.stdout.write(f"INFO| {text}.\n")
