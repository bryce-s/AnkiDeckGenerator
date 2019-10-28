# AnkiDeckGenerator
Given a CSV list of terms, we generate a deck of Anki flashcards with audio.


# Usage

Unfreeze requirements.txt into your venv.

`python3 AppendAndGenerateAudio.py kap1.csv mirror:true Kap1`

`mirror:true` or `mirro:false` is required. This argument duplicates and flips the cards, ie:
```
A (front) | B (back)
B (back) | A (front)
```

# Example
```
(env) ➜  AnkiDeckGenerator git:(master) ✗ python AppendAndGenerateAudio.py kap3.csv mirror:true Kap3
row 1: front: der Artikel, back:  -
row 2: front: das Beispiel, back:  -e
row 3: front: der Fall, back:  die Fälle
row 4: front: falls, back: in case
row 5: front: die Familie, back:  -n
row 6: front: der Film, back:  -e
row 7: front: das Foto, back:  -s
row 8: front: der Gast, back:  die Gäste
row 9: front: das Geld, back: money
row 10: front: die Gemeinde, back:  -n
row 11: front: die Geschichte, back:  -n
row 12: front: der Grund, back:  die Gründe
row 13: front: im Grunde genommen, back: basically
row 14: front: die Gruppe, back:  -n
row 15: front: die Kirche, back:  -n
row 16: front: das Mal, back:  -e / mal
row 17: front: die Mannschaft, back:  -en
row 18: front: der / das Meter, back:  -
row 19: front: das Mitglied, back:  -er
row 20: front: der Monat, back:  -e
row 21: front: der Name, back:  -n
row 22: front: der Ort, back:  -e
row 23: front: die Polizei (Sg.), back: police
row 24: front: der Präsident, back:  -en
row 25: front: das Problem, back:  -e
row 26: front: der Punkt, back:  -e
row 27: front: die Schule, back:  -n
row 28: front: die Straße, back:  -n
row 29: front: die Stunde, back:  -n
row 30: front: das Team, back:  -s
row 31: front: das Thema, back:  die Themen
row 32: front: das Unternehmen, back:  -
row 33: front: der Verein, back:  -e
row 34: front: der Weg, back:  -e
row 35: front: weg, back: gone
row 36: front: die Welt, back:  -en
row 37: front: das Ziel, back:  -e
row 38: front: arbeiten, back:  arbeitete
row 39: front: bekommen, back:  bekam
row 40: front: berichten, back:  berichtete
row 41: front: bestehen, back:  bestand
row 42: front: bieten, back:  bot
row 43: front: erklären, back:  erklärte
row 44: front: erreichen, back:  erreichte
row 45: front: folgen, back:  folgte
row 46: front: fordern, back:  forderte
row 47: front: gelten (gilt), back:  galt
row 48: front: gewinnen, back:  gewann
row 49: front: leben, back:  lebte
row 50: front: meinen, back:  meinte
row 51: front: mögen (mag), back:  mochte
row 52: front: nennen, back:  nannte
row 53: front: schaffen, back:  schaffte
row 54: front: schaffen, back:  schuf
row 55: front: schreiben, back:  schrieb
row 56: front: setzen, back:  setzte
row 57: front: sich setzen, back:  setzte sich
row 58: front: sprechen, back:  sprach
row 59: front: steigen, back:  stieg
row 60: front: treffen (trifft), back:  traf
row 61: front: tun, back:  tat
row 62: front: wissen (weiß), back:  wusste
row 63: front: ziehen, back:  zog
row 64: front: bekannt, back: familiar
row 65: front: deutlich, back: distinct
row 66: front: einfach, back: simple
row 67: front: frei, back: free
row 68: front: früh, back: early
row 69: front: gemeinsam, back: common
row 70: front: gleich, back: equal
row 71: front: international, back: international
row 72: front: jährig, back: years of age
row 73: front: klar, back: clear
row 74: front: möglich, back: possible
row 75: front: nah, back: near
row 76: front: politisch, back: political(ly)
row 77: front: richtig, back: right(ly)
row 78: front: rund, back: round
row 79: front: schnell, back: fast
row 80: front: schön, back: beautiful
row 81: front: schwer, back: heavy
row 82: front: spät, back:  später
row 83: front: vergangen, back: past
row 84: front: der Januar (Jänner), back: January (Austria: January)
row 85: front: der Februar, back: February
row 86: front: im Februar, back: in February
row 87: front: im (Monat), back: in (month)
row 88: front: der März, back: March
row 89: front: der April, back: April
row 90: front: der Mai, back: May
row 91: front: der Juni, back: June
row 92: front: der Juli, back: July
row 93: front: der August, back: August
row 94: front: der September, back: September
row 95: front: der Oktober, back: October
row 96: front: der November, back: November
row 97: front: der Dezember, back: December
row 98: front: mir, back: me
row 99: front: ihn, back: him
row 100: front: welch(e, back: er
row 101: front: neben, back: beside
row 102: front: während, back: during
row 103: front: also, back: therefore
row 104: front: besonders / besonder-, back: especially /special
row 105: front: bisher, back: so far
row 106: front: darauf, back: on it / on them
row 107: front: davon, back: of or from it / them
row 108: front: etwas, back: something
row 109: front: fast, back: almost
row 110: front: gar, back: at all
row 111: front: gerade, back: just now
row 112: front: sogar, back: even
row 113: front: wohl, back: probably
row 114: front: der Montag, back:  -e
row 115: front: der Dienstag, back:  -e
row 116: front: der Mittwoch, back:  -e
row 117: front: der Donnerstag, back:  -e
row 118: front: der Freitag, back:  -e
row 119: front: der Samstag, back:  -e
row 120: front: der Sonnabend, back:  -e
row 121: front: der Sonntag, back:  -e
row 122: front: das Wochenende, back:  -n
row 123: front: montags, back:  dienstags
(env) ➜  AnkiDeckGenerator git:(master) ✗ ls | grep output.apkg
output.apkg
```