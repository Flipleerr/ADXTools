import subprocess
import os

def wav_to_adx(wav_file, adx_file, key=None):
    # Requests adxencd (requires PATH)
    adxencd_path = 'adxencd.exe'

    # Checks whether the specified file exists
    if not os.path.exists(wav_file):
        print(f"Error: WAV file '{wav_file}' not found.")
        return

    # Appends .adx if not present
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

def main():
    wav_file = input("Enter the path to the WAV file: ").strip('"')
    adx_file = input("Enter the path for the output ADX file: ").strip('"')
    key = input("Enter the encryption key (or leave blank if none): ").strip()

    if key == "":
        key = None

    wav_to_adx(wav_file, adx_file, key)

if __name__ == '__main__':
    main()