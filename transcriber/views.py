from dotenv import load_dotenv
import os
from django.http import HttpResponse, JsonResponse
from .models import Transcriber_Model_Template
from .serializers import Transcriber_Serializer_Template
from rest_framework.decorators import api_view
from pytube import YouTube
import openai
import pydub
import eyed3


load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

_audio_max_length = 10 * 60 * 1000 # 10 minutes
_audio_base_dir = './transcriber/downloads/'
    
@api_view(['POST'])
def upload(request):
    youtube_url = request.data['yturl']
    youtubeObject = YouTube(youtube_url)
    
    video_length = youtubeObject.length
    chunks = (video_length // _audio_max_length) + 1
    
    youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
    
    data = youtubeObject.download(filename= _audio_base_dir + 'audio.mp3')
    
    
    print(transcribe(chunks, data))
    
    
    return HttpResponse('worked')


def transcribe(chunks, audio_file_dir):
    # try:
    #     audio = pydub.AudioSegment.from_mp3(audio_file_dir)
    #     print("Audio loaded successfully.")
    # except pydub.exceptions.CouldntDecodeError as e:
    #     print("Failed to load audio:", e)
    #     return "Audio loading error"


    # transcription = ""
    # for current_chunk in range(chunks):
    #     audio_chunk = audio[current_chunk * _audio_max_length:(current_chunk + 1) * _audio_max_length]
    #     audio_chunk.export(_audio_base_dir + "audio_temp", format="mp3")
    file = open(audio_file_dir, 'rb')
    transcription = whisper_transcription(file)['text']
    
    return transcription 
        
        
def whisper_transcription(file):
    transcript = openai.Audio.transcribe("whisper-1", file)
    
    # return "AAAAAAAAAAAAAAAAAA"
    return transcript
        
