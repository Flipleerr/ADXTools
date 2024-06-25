import subprocess
import os

def wav_to_ahx(wav_file, ahx_file, bap=None):
    ahxencd_path = 'ahxencd.exe'
    if not os.path.exists(wav_file):
        print(f"Error: WAV file '{wav_file}' not found.")
        return
    if not ahx_file.lower().endswith('.ahx'):
        ahx_file += '.ahx'
    command = [ahxencd_path, wav_file, ahx_file]
    if bap:
        command.append(f'-bap={bap}')
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully converted {wav_file} to {ahx_file}")
        else:
            print(f"Error converting {wav_file} to {ahx_file}: {result.stderr}")
    except FileNotFoundError:
        print("Error: ahxencd executable not found. Ensure it is installed and in your system's PATH.")

def ahx_to_wav(ahx_file, wav_file):
    vgmstream_path = 'vgmstream_cli'
    if not os.path.exists(ahx_file):
        print(f"Error: AHX file '{ahx_file}' not found.")
        return
    if not wav_file.lower().endswith('.wav'):
        wav_file += '.wav'
    command = [vgmstream_path, '-o', wav_file, ahx_file]
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully converted {ahx_file} to {wav_file}")
        else:
            print(f"Error converting {ahx_file} to {wav_file}: {result.stderr}")
    except FileNotFoundError:
        print("Error: vgmstream executable not found. Ensure it is installed and in your system's PATH.")