from os import path
from pydub import AudioSegment
import os

src_path = '/home/pranav/Desktop/Cross_Model_Project/speech-accent-archive/recordings'
dest_path = '/home/pranav/Desktop/Cross_Model_Project/speech-accent-archive/wav_recordings'

for file in os.listdir(src_path):
	basename = file.split('.')
	basename = basename[0]+'.wav'
	sound = AudioSegment.from_mp3(os.path.join(src_path,file))
	sound.export(os.path.join(dest_path,basename), format='wav')


