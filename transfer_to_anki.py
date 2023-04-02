#!/Users/johan/fun/finnish_sentences/bin/python
from ankiwrite import addNote
from finnish_tts import save_finnish_audio
import uuid
# read file using lines
# for each line
# generate a sound file
# add the note
# append the contents of the file to a backup file
# delete the body
sentence_file = "/Users/johan/Library/Mobile Documents/com~apple~CloudDocs/finska/finska_meningar.txt"
backup_file = "/Users/johan/fun/finnish_sentences/sentences_backup.txt"
audio_path = "/Users/johan/fun/finnish_sentences/audio/"

def filepath(filename):
    return audio_path + filename

def unique_filename():
    return "f" + uuid.uuid4().hex + ".mp3"

with open(sentence_file, 'r+') as s:
    l = s.readlines()
    for line in l:
        if line.strip() != "":
            fname = unique_filename()
            fpath = filepath(fname)
            save_finnish_audio(line, fpath)
            addNote(line,fname,fpath)
    with open(backup_file, 'a') as bf:
        bf.writelines(l)
    s.truncate(0)
