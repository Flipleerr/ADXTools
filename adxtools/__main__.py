import argparse
from adxtools.adx_conversion import wav_to_adx, adx_to_wav
from adxtools.ahx_conversion import wav_to_ahx, ahx_to_wav
from adxtools.aix_conversion import adx_to_aix, aix_to_wav

def main():
    parser = argparse.ArgumentParser(description='ADXTools - A set of tools for converting, creating and modifying ADX, AHX, and AIX files in the command line.')
    subparsers = parser.add_subparsers(dest='command', help='Choose a command to run')

    parser_toadx = subparsers.add_parser('toadx', help='Convert WAV to ADX')
    parser_toadx.add_argument('wav_file', help='Path to the WAV file')
    parser_toadx.add_argument('adx_file', help='Path for the output ADX file')
    parser_toadx.add_argument('-key', help='Encryption key', default=None)

    parser_fromadx = subparsers.add_parser('fromadx', help='Convert ADX to WAV')
    parser_fromadx.add_argument('adx_file', help='Path to the ADX file')
    parser_fromadx.add_argument('wav_file', help='Path for the output WAV file')

    parser_toahx = subparsers.add_parser('toahx', help='Convert WAV to AHX')
    parser_toahx.add_argument('wav_file', help='Path to the WAV file')
    parser_toahx.add_argument('ahx_file', help='Path for the output AHX file')
    parser_toahx.add_argument('-bap', help='Bit Allocation Pattern', default=None)

    parser_fromahx = subparsers.add_parser('fromahx', help='Convert AHX to WAV')
    parser_fromahx.add_argument('ahx_file', help='Path to the AHX file')
    parser_fromahx.add_argument('wav_file', help='Path for the output WAV file')

    parser_toaix = subparsers.add_parser('toaix', help='Convert ADX to AIX')
    parser_toaix.add_argument('input_list_file', help='Path to the input list file')
    parser_toaix.add_argument('aix_file', help='Path for the output AIX file')
    parser_toaix.add_argument('-key', help='Encryption key', default=None)

    parser_fromaix = subparsers.add_parser('fromaix', help='Convert AIX to WAV')
    parser_fromaix.add_argument('aix_file', help='Path to the AIX file')
    parser_fromaix.add_argument('wav_file', help='Path for the output WAV file')

    args = parser.parse_args()

    if args.command == 'toadx':
        wav_to_adx(args.wav_file, args.adx_file, args.key)
    elif args.command == 'fromadx':
        adx_to_wav(args.adx_file, args.wav_file)
    elif args.command == 'toahx':
        wav_to_ahx(args.wav_file, args.ahx_file, args.bap)
    elif args.command == 'fromahx':
        ahx_to_wav(args.ahx_file, args.wav_file)
    elif args.command == 'toaix':
        adx_to_aix(args.input_list_file, args.aix_file, args.key)
    elif args.command == 'fromaix':
        aix_to_wav(args.aix_file, args.wav_file)
    else:
        parser.print_help()
    pass

if __name__ == '__main__':
    main()