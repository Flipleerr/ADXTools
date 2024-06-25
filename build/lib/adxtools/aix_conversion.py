import subprocess
import os

def adx_to_aix(input_list_file, aix_file, key=None):
    aixmakec_path = 'aixmakec.exe'
    if not os.path.exists(input_list_file):
        print(f"Error: Input list file '{input_list_file}' not found.")
        return
    if not aix_file.lower().endswith('.aix'):
        aix_file += '.aix'
    command = [aixmakec_path, input_list_file, aix_file]
    if key:
        command.extend(['-key', key])
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully created {aix_file} from {input_list_file}")
        else:
            print(f"Error creating {aix_file}: {result.stderr}")
    except FileNotFoundError:
        print("Error: aixmakec executable not found. Ensure it is installed and in your system's PATH.")

def aix_to_wav(aix_file, wav_file):
    vgmstream_path = 'vgmstream_cli'
    if not os.path.exists(aix_file):
        print(f"Error: AIX file '{aix_file}' not found.")
        return
    if not wav_file.lower().endswith('.wav'):
        wav_file += '.wav'
    command = [vgmstream_path, '-o', wav_file, aix_file]
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully converted {aix_file} to {wav_file}")
        else:
            print(f"Error converting {aix_file} to {wav_file}: {result.stderr}")
    except FileNotFoundError:
        print("Error: vgmstream executable not found. Ensure it is installed and in your system's PATH.")
