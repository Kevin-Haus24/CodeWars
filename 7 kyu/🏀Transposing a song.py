def transpose(songs, interval):
    notes_1 = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    notes_2 = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    notes = dict.fromkeys(notes_1 + notes_2)
    ans = []
    for index, song in enumerate(notes): notes[song] = index

    return notes

print(transpose(['Ab', 'Gb'], 2))