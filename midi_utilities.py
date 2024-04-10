from mido import Message, MidiFile, MidiTrack

def read_from_midi(file = './miditest.mid'):
    mid = MidiFile(file)
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            print(msg)




def write_to_midi(newFile = './new_song.mid'):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    
    # GENERATE THE MIDI MESSAGE INFORMATION THAT WILL BE WRITTEN IN THE FILE

    mid.save('new_song.mid')