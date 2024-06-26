# ADXTools
**A set of lightweight command-line tools written in Python for modifying ADX files**
![ADXTools](/docs/images/ADX_logo.png)

## What is ADX?
ADX is a file format developed by CRI Middleware used mainly in video games, notably the Sonic the Hedgehog series. It's also used mostly by Sega in their games, with ADX first being used on the Saturn. It also presents a barrier to entry for modding, as many encoding and decoding tools are not widely available. This repo sees to change that.


## Installation
First off, you'll need to download the following dependencies:

- [vgmstream](https://github.com/vgmstream/vgmstream)
- [adxencd.exe](https://github.com/Flipleerr/my-stuff/raw/master/adxencd.exe)

Next step would be to add these to your system's PATH. This allows the programs to be called from any location on your computer, also allowing ADXTools to work it's magic.

Install ADXTools with pip using `pip install adxtools`, then make sure it's installed by running the following command: `adxtools -h`.

## Usage
Using ADXTools is relatively simple: most of the syntax involves this syntax: `adxtools [action-type] [input-file] [output-file]`, but it can fluctuate from command to command. For example, conversion to AHX requires you to provide a `.bap` file, which provides the bit allocation pattern that ahxencd.exe uses to compress audio data (more info can be found in the docs - which are to be added soon).

## Contributing
This project as of now does not have a Code of Conduct, nor do I expect people will contribute, but if you do, simply create a fork and send over a pull request. Make sure to follow the factoring style of the existing code.