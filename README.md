Simple Python library to extract tracker module information using the `xmp` program.

Depends on `xmp` being installed.

# Install

```
pip install git+https://github.com/chr15m/py-xmp-mod-render.git@main
```

# Use

```python
from modrender import modrender
modrender("myfile.it")
```

Can also be run from the command line:

`mod-render MODFILE`

Tested on `.xm`, `.it`, and `.mptm` files.

# API

## `get_info(modfile)`

Returns a struct like this:

```
{'channelcount': 8,
 'channelnames': {0: 'arpeg', 1: 'melody', 2: 'amen', 3: 'beats', 4: 'blippy'},
 'comments': 'GOOD NOTES\n\n [x][ ]  [x][ ][ ]\n[ ][x][x][ ][x][x][ ].',
 'info': {'Channels': '8 [ f - - - - 8 8 8 ]',
          'Duration': '0min30s',
          'Instruments': '15',
          'Module length': '6 patterns',
          'Module name': 'bambulance',
          'Module type': 'OpenMPT 1.30 IT 2.14',
          'Patterns': '10',
          'Samples': '13'},
 'raw': 'Extended Module Player 4.0.10\n'
        'Copyright (C) 1996-2014 Claudio Matsuoka and Hipolito Carraro Jr\n'
        'Using null output\n'
        'Mixer set to 44100 Hz, 16bit, cubic spline interpolated stereo\n'
        "Press 'h' for help\n"
        '\n'
        'Loading test-mods/bambulance.it (1 of 1)\n'
        'Module name  : bambulance\n'
        'Module type  : OpenMPT 1.30 IT 2.14\n'
        'Module length: 6 patterns\n'
        'Patterns     : 10\n'
        'Instruments  : 15\n'
        'Samples      : 13\n'
        'Channels     : 8 [ f - - - - 8 8 8 ]\n'
        'Duration     : 0min30s\n'
        '\n'
        '> GOOD NOTES\n'
        '> \n'
        '>  [x][ ]  [x][ ][ ]\n'
        '> [ ][x][x][ ][x][x][ ].\n'
        '\n'}
```
