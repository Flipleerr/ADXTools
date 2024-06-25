import subprocess
import os

def aud_to_aix(input_list, aix_file, key=None):
    aixmakec_path = 'aixmakec.exe'

    if not os.path.exists(input_list):
        print(f"Error: Could not find '{input_list}'")

    if not aix_file.lower().endswith('.aix'):
        aix_file += '.aix'

    command = [input_list, aix_file, key]
    if key:
        command.extend(['-key', key])

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully created {aix_file} from {input_list}")
        else:
            print(f"Error creating {aix_file}: {result.stderr}")
    except FileNotFoundError:
        print("Error: aixmakec executable not found. Ensure it is installed and in your system's PATH.")

def main():
    input_list = input("Enter the path to the input list file: ").strip('"')

    aix_file = input("Enter the path for the output AIX file: ").strip('"')

    key = input("Enter the encryption key (or leave blank if none): ").strip()

    if key == "":
        key = None

    aud_to_aix(input_list, aix_file, key)
