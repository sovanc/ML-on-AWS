import boto3
from pygame import mixer
import os

polly = boto3.client('polly')
spoken_text = polly.synthesize_speech(Text='Hi, my name is Larry.  I am the presenter for today.',
    OutputFormat='mp3',
    VoiceId='Matthew')
    
with open('output.mp3', 'wb') as f:
    f.write(spoken_text['AudioStream'].read())
    f.close()
    
mixer.init()
mixer.music.load('output.mp3')
mixer.music.play()

while mixer.music.get_busy() == True:
    pass
    
mixer.quit()
#os.remove('output.mp3')