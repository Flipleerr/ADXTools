import subprocess
import os

def wav_to_ahx(wav_file, ahx_file, bap=None):
    # Requests ahxencd (requires PATH)
    ahxencd_path = 'ahxencd.exe'

    # Checks whether the specified file exists
    if not os.path.exists(wav_file):
        print(f"Error: WAV file '{wav_file}' not found.")
        return

    # Appends .ahx if not present
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

def main():
    wav_file = input("Enter the path to the WAV file: ").strip('"')
    ahx_file = input("Enter the path for the output AHX file: ").strip('"')
    bap = input("Enter the desired Bit Allocation Pattern: ").strip()

    if bap == "":
        bap = None

    wav_to_ahx(wav_file, ahx_file, bap)

if __name__ == '__main__':
    main()