# Djembe rhythms

Collection of useful rhythms for learning playing Djembe.

## Legend

* `B` : bass (full hand)
* `T` : tone (half hand)
* `S` : slap (quarter hand)
* `-` : pause
* `|` : group separator

e.g.: `BBTT|-BT-` (8 ticks in 2 groups)

## Rhythms

### 6 ticks

*3+3*

1. `BTB|TSS`
1. `BTT|BSS` :star:

### 8 ticks

*4+4*

1. `B--T|B-T-`
1. `T-BB|TTB-`
1. `BTTB|TTBT` :star:
    1. `BTTB|TBSS`
1. `BTBT|TBTT` (same as previous, shifted 2 ticks to right)
1. `B-TT|-BT-`
    1. `BBTT|-BT-`
1. `B-TT|--S-`
1. `BT-T|-T-T`
1. `BBTT|BBT-`
1. `BBSB|BSTS`
1. `B--T|S-T-` :star:
1. `TT-B|B--T`
1. `B-TT|T-B-`
1. `TT-B|B-T-`
1. `-TT-|BB-T` (same as previous, shifted 1 tick to right)
1. `B---|--TT`
    1. `B-TT|B-SS` (dense, 2 slaps at the end)
1. `TT--|TT--`
    1. `--TT|--TT` (same as previous, shifted 2 ticks to right)
    1. `--TT|--S-`
1. `BB-S|S-TT`

### 12 ticks

*3+3+3+3*

1. `T-B|-TT|B-T|T--`
1. `B-B|-SS|-BB|-SS`

## 14 ticks

*(4+4+3+3)*

1. `B-TT|T-T-|B-T|-T-`

### 16 ticks

*4+4+4+4*

1. `B---|TTTT|--B-|-B--`
1. `BTTB|S-TT|BTTB|S---`
1. `BBTT|BTB-|TB-T|BBT-`
1. `BB-T|-TTT|BB-T|-TT-`
1. `B-T-|T-T-|BT-T|-T-T`
1. `B--T|B-TT|B--T|B-TT`
1. `B--T|S--B|-T-T|S---`
1. `BBTT|STTB|TTBS|STTB`
1. `BTTB|TTTT|BTTB|TTSS`
1. `BTTB|TTBT|TBTT|BTSS`
1. `TTBT|STTT|SBTT|BTTT`
1. `B-TT|BTTB|-BTT|B-TT` :star:
1. `BTTB|TTB-|TTTT|TTT-`
1. `T---|B-TT|--B-|--TT`
1. `T--T|--T-|-T--|--TT`
1. `B-TT|B-TT|B-TT|BT-T`
1. `B--T|S---|S-S-|S---` :star:

### 32 ticks

*4+4+4+4 4+4+4+4*

1. `B---|S---|B--S|T---|B---|TTTT|T--T|T---` :star:

## Rhythm generator

I've created a simple rhythm generator based on Markov Model.
To use it, go to `generator` directory, open python and run:
```py
from generator import train, generate
model = train(['BB--', 'BBAA', 'AACC'])
model.generate(4)
```
