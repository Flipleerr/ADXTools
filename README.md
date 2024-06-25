# ADXTools
**A set of lightweight command-line tools written in Python for modifying ADX files**
![ADXTools](/docs/images/ADX_logo.png)

## What is ADX?
ADX is a file format developed by CRI Middleware used mainly in video games, notably the Sonic the Hedgehog series. It's also used mostly by Sega in their games, with ADX first being used on the Saturn. It also presents a barrier to entry for modding, as many encoding and decoding tools are not widely available. This repo sees to change that.

## Tools
As of now, ADXConvert is the only available tool. More tools are to be added soon.

### ADXConvert
This tool converts to and from the ADX format, accepting WAV, AIFF and (obviously) ADX files.

## Installation
First off, you'll need to download the following dependencies:

- [vgmstream](https://github.com/vgmstream/vgmstream)
- [adxencd.exe](https://github.com/Flipleerr/my-stuff/raw/master/adxencd.exe)

Then, you'll need to add these to your system's PATH. This allows the execs to be called from any location on your PC.

Finally, run the scripts with this syntax: `python script_path.py`