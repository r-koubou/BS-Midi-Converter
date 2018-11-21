# Usage

## NOTE
This tool make a powerful converting to you.
You need to read a program code or understand following to use.

## Usage

1: Run from python

**When 1st time run only: Call setup-venv.bat, setup-libs.bat to install dependency programs.**

`python main.py <midifile>`

2: Run from exe (Attached : 64bit OS Only)

`BSMConverter.exe <midifile>`

or

Drag & Drop a midi file to BSMConverter.exe

**If no problem, json data will copy to clipboard.**

## MIDI file Spec

### BPM

This tool search BPM from MIDI file.
You have to insert Tempo data.


### Beat Direction

Use MIDI Note

| Note |             Beat Direction             |
|:----:|:--------------------------------------:|
| C    | Bottom to Top (direction:0)            |
| D    | Top to Bottom (direction:1)            |
| E    | Right to Left (direction:2)            |
| F    | Left to Right (direction:3)            |
| F#   | Right-Bottom to Left-Top (direction:4) |
| G    | Left-Bottom to Right-Top (direction:5) |
| G#   | Right-Top to Left-Bottom (direction:6) |
| A    | Left-Top to Right-Bottom (direction:7) |
| B    | Any (direction:8)                      |

### Layer mapping

Use MIDI Note Velocity

~~~
1-42      43-83      84-127
  |         |          *
  |         *          |
  *         |          |
~~~

### Line mapping

Use MIDI Note (Octave)

~~~
Octave4: *---
Octave5: -*--
Octave6: --*-
Octave7: ---*
~~~

### Beat type

Use MIDI CC2 value

| CC2 Value | Beat Type |
|:---------:|:---------:|
| 0-31      | Red       |
| 32-63     | Blue      |
| 64-96     | Bomb      |

## Basic example

On DAW (Cubase, Studio One, Logic, etc.)

1. Create a song's audio file and insert to an audio track
2. Create 2 MIDI tracks
3. Track1: insert MIDI CC2( value:0 ) to Beginning of the score -\> **Red Beat**
4. Track2: insert MIDI CC2( value:32 ) to Beginning of the score -\> **Blue Beat**
5. MIDI programing with MIDI Note, Velocity
6. Export SMF (Recomend Time Resolution:480)
7. Convert!
8. Check on external Beat Saber Editor (e.g.: EditSaber)
