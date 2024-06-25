import subprocess
import os

def wav_to_adx(wav_file, adx_file, key=None):
    adxencd_path = 'adxencd.exe'
    if not os.path.exists(wav_file):
        print(f"Error: WAV file '{wav_file}' not found.")
        return
    if not adx_file.lower().endswith('.adx'):
        adx_file += '.adx'
    command = [adxencd_path, wav_file, adx_file]
    if key:
        command.extend(['-key', key])
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully converted {wav_file} to {adx_file}")
        else:
            print(f"Error converting {wav_file} to {adx_file}: {result.stderr}")
    except FileNotFoundError:
        print("Error: adxencd executable not found. Ensure it is installed and in your system's PATH.")

def adx_to_wav(adx_file, wav_file):
    vgmstream_path = 'vgmstream_cli'
    if not os.path.exists(adx_file):
        print(f"Error: ADX file '{adx_file}' not found.")
        return
    if not wav_file.lower().endswith('.wav'):
        wav_file += '.wav'
    command = [vgmstream_path, '-o', wav_file, adx_file]
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully converted {adx_file} to {wav_file}")
        else:
            print(f"Error converting {adx_file} to {wav_file}: {result.stderr}")
    except FileNotFoundError:
        print("Error: vgmstream executable not found. Ensure it is installed and in your system's PATH.")
