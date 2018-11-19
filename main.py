# conding: utf-8
import json
import sys

import pretty_midi
import clipboard

TEMPLATE_BODY = {
    "_version": "1.5.0",
    "_beatsPerMinute": 120,
    "_beatsPerBar": 8,
    "_noteJumpSpeed": 10,
    "_shuffle": 0,
    "_shufflePeriod": 0.5,
    "_events": [],
    "_notes":[]
}

TEMPLATE_NOTE = {
    "_time": 0,
    "_lineIndex": 1,
    "_lineLayer": 1,
    "_type": 0,
    "_cutDirection": 8
}

# Note Octave to "_lineIndex" value
def to_line_index( note ):
    #========================================================
    # Line mapping
    #========================================================
    # Octave4: *---     : 0
    # Octave5: -*--     : 1
    # Octave6: --*-     : 2
    # Octave7: ---*     : 3
    octave = int( note.pitch / 12 ) - 2
    if( octave == 4 ):
        return 0
    elif( octave == 5 ):
        return 1
    elif( octave == 6 ):
        return 2
    elif( octave == 7 ):
        return 3
    else:
        # invalid octave
        return 0

# Velocity to "_lineLayer" value
def to_line_layer( note ):
    #========================================================
    # Layer mapping
    #========================================================
    # [Velocity]
    # 1-42      43-83      84-127
    #   |         |          *
    #   |         *          |
    #   *         |          |
    vel = note.velocity
    if( vel < 42 ):
        return 0
    elif( vel < 83 ):
        return 1
    else:
        return 2

# Note (C, C#, D, ... B) to "_cutDirection" value
def to_line_cut_direction( note ):
    n = note.pitch % 12
    #========================================================
    # Key mapping
    #========================================================
    # 0: (C)  Bottom to Top (direction:0)
    # 2: (D)  Top to Bottom (direction:1)
    # 4: (E)  Right to Left (direction:2)
    # 5: (F)  Left to Right (direction:3)
    # 6: (F#) Right-Bottom to Left-Top (direction:4)
    # 7: (G)  Left-Bottom to Right-Top (direction:5)
    # 8: (G#) Right-Top to Left-Bottom (direction:6)
    # 9: (A)  Left-Top to Right-Bottom (direction:7)
    # 11:(B)  Any (direction:8)
    if( n == 0 ):
        return 0
    elif( n == 2 ):
        return 1
    elif( n == 4 ):
        return 2
    elif( n == 5 ):
        return 3
    elif( n == 6 ):
        return 4
    elif( n == 7 ):
        return 5
    elif( n == 8 ):
        return 6
    elif( n == 9 ):
        return 7
    elif( n == 11 ):
        return 8
    else:
        # invalid
        return 0


# main
def main():
    midi = pretty_midi.PrettyMIDI( sys.argv[1] )
    midi_tracks = midi.instruments
    bpm =  midi.estimate_tempo()
    score = TEMPLATE_BODY.copy()
    score[ "_beatsPerMinute" ] = bpm

    for i, t in enumerate( midi_tracks ):
        for note in t.notes:
            # note.start: Note On time (sec)
            # note.pitch: Note No
            # note.velocity: Velocity
            n = TEMPLATE_NOTE.copy()

            # MIDI track 1: Red
            # MIDI track 2: Blue
            n[ "_type" ]            = i

            n[ "_time" ]            = (bpm/60)*note.start
            n[ "_lineIndex" ]       = to_line_index( note )
            n[ "_lineLayer" ]       = to_line_layer( note )
            n[ "_cutDirection" ]    = to_line_cut_direction( note )

            score[ "_notes" ].append( n )

    clipboard.copy( json.dumps( score, indent=4 ) )

if __name__ == "__main__":
    main()
