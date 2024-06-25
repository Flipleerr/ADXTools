import subprocess

def adx_to_wav(adx_file, wav_file):
    vgmstream_path = 'vgmstream-cli.exe'  # Replace with the actual path to vgmstream-cli.exe
    result = subprocess.run([vgmstream_path, '-o', wav_file, adx_file], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Converted {adx_file} to {wav_file}")
    else:
        print(f"Unable to convert {adx_file}: {result.stderr}")

def main():
    adx_file = input("Enter the path to the ADX file: ")
    wav_file = input("Enter the path for the output WAV file: ")
    adx_to_wav(adx_file, wav_file)

if __name__ == '__main__':
    main()