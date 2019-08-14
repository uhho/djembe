# Djembe rhythms

Collection of useful rhythms for learning playing Djembe.

## Legend

* **B** : bass (full hand)
* **T** : tone (half hand)
* **S** : slap (quarter hand)
* **-** : pause
* **|** : group separator

I'm using following symbols for additional sounds / combinaions

* **2** : Double tone (double tremolo)
* **3** : Triple tone (triple tremolo)
* **R** : "Broken" tone or slap played using both hands at the same time but with small lag


e.g.: **BBTT|-BT-** (8 ticks in 2 groups)

## Rhythms

### Intro

1. `T-T-|TT-T|-T-T|T-T-`
    1. `T-T-|TT-T|-T-T|T-TT`
1. `TT-T|-T-T|T-T-|T-TT`
1. `R-T-|T-2T|TTTT|TT--` (Lamban: break)

### 6 ticks

*3+3*

1. `BTB|TSS`
1. `BTT|BSS` :star:
1. `B-B|-TT` *Palo*
1. `S--|TS-`

### 8 ticks

*4+4*

1. `B--T|B-T-`
    1. `B--T|S-T-`
    1. `B--T|--T-` :star:
1. `T-BB|TTB-`
1. `BTTB|TTBT` :star:
    1. `BTTB|TBSS`
    1. `BTTB|BTSS`
1. `BTBT|TBTT` (same as previous, shifted 2 ticks to right)
1. `B-TT|-BT-`
    1. `BBTT|-BT-`
1. `B-TT|--S-`
1. `BT-T|-T-T`
1. `BBTT|BBT-`
1. `BBSB|BSTS`
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
1. `B--T|B-TT`
1. `T--S|T---` (raga)
1. `TT-T|T--T` (Burkina Faso)
    1. `TT-T|T-T-`
1. `T-TT|T-T-`
1. `B-B-|TTTT`
1. `TTTT|--SS` :star:

### 12 ticks

*3+3+3+3*

1. `T-B|-TT|B-T|T--`
1. `B-B|-SS|-BB|-SS`
1. `B-T|B-T|B-T|SSS`
1. `B-B|-BT|TB-|B--` :star:
1. `B-T|TB-|B-B|T--` *Abaqua*
1. `B---|T--T|T---`

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
1. `B--T|S--B|-T-T|S---` :star:
1. `BBTT|STTB|TTBS|STTB`
1. `BTTB|TTBT|TBTT|BTSS`
1. `TTBT|STTT|SBTT|BTTT`
1. `B-TT|BTTB|-BTT|B-TT` :star:
1. `BTTB|TTB-|TTTT|TTT-`
1. `T---|B-TT|--B-|--TT`
1. `T--T|--T-|-T--|--TT`
    1. `B--B|--B-|-T--|SSSS` :star:
1. `B-TT|B-TT|B-TT|BT-T`
1. `B---|T---|B--T|--T-` :star:
1. `B--T|S---|S-S-|S---` :star:
1. `B---|T---|T--T|--TT`
1. `T-T-|TTTT|T-T-|B-T-`
1. `B---|TT--|B-TT|TT--` (Lamban)
1. `T-T-|T-T-|BB-B|B-B-` :star:
1. `TTTT|B-S-|B-SS|B-S-`
1. `B-T-|TTTS|-S-T|T-BB` :star:
1. `B--T|----|B--T|--SS`
1. `BTTS|TTTT|BTTS|TTSS` :star:
1. `S---|B--T|T-T-|--S-`
1. `B-B-|S--T|-T--|S-SS` (Baba Yetu) :star:

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

## Sample solos

```
TT-T|-T-T|T-T-|T-TT

B--T|S--B|-T-T|S---
TT-T|S---|TT-T|S---
--SS|--SS|--SS|--SS
S-22|S-22|S-22|S-22
-TTT|-TTT|-TTT|-TTT
B-TT|B-TT|B-TT|B-TT
22-T|T--T|22-T|T--T

TT-T|-T-T|T-T-|T---
```
