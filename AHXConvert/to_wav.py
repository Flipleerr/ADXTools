import subprocess

def ahx_to_wav(ahx_file, wav_file):
    vgmstream_path = 'vgmstream-cli.exe'  # Replace with the actual path to vgmstream-cli.exe
    result = subprocess.run([vgmstream_path, '-o', wav_file, ahx_file], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Converted {ahx_file} to {wav_file}")
    else:
        print(f"Unable to convert {ahx_file}: {result.stderr}")

def main():
    ahx_file = input("Enter the path to the AHX file: ")
    wav_file = input("Enter the path for the output WAV file: ")
    ahx_to_wav(ahx_file, wav_file)

if __name__ == '__main__':
    main()