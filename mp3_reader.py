### Created June 19th,2023
### Podcast AI Transcriber and Summarizer Development
### https://github.com/yinruiqing/pyannote-whisper -- really good git document on using Whisper/pyannote/ChatGPT model
### Another idea: transcribe foreign language podcasts or episodes and output script to learn German, translated in English
### Where to download podcast .mp3 https://podcastindex.org/podcast/551334
### Python convert mp3 to wav with Pydub https://stackoverflow.com/questions/32073278/python-convert-mp3-to-wav-with-pydub


# Libraries
import os, sys
import openai
import whisper
import json
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from pydub import AudioSegment
from huggingface_hub import login
from huggingface_hub import snapshot_download
from pyannote.audio import Pipeline
from pyannote_whisper.utils import diarize_text
load_dotenv()
# Load your API key from an environment variable or secret management service
api_key = os.getenv("OPENAI_API_KEY")
pyannote_token = os.getenv("PYANNOTE_TOKEN")
print(api_key)
print(pyannote_token)

# hfhub login
login(token=pyannote_token)
snapshot_download(repo_id="pyannote/speaker-diarization") # hfhub model

# Load audio file .mp3
audio_file = open('20230315_pmoney.mp3','rb')
src = "20230315_pmoney.mp3"
dst = "20230315_pmoney.wav"

### Function to convert mp3 to wav ###                                                     
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

### Purely based on Whisper ###
# Call the OpenAI - run Whisper
response = openai.Audio.transcribe('whisper-1', audio_file)

# Print transcription of podcast episode
print(response) # raw text ouput, without multiple speaker identification


### pyannote.audio + whisper ###
# Perform speaker diarization
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1", use_auth_token=pyannote_token) # IMPORTANT: VSCODE MUST RUN AS ADMIN

model = whisper.load_model("tiny.en")
asr_result = model.transcribe(audio_file) # .transcribe() from pyannote_whisper, not the whisper pkg
diarization_result = pipeline(audio_file) # only takes wav, need to convert .mp3
final_result = diarize_text(asr_result, diarization_result)

# Output transcription labeled by speakers
for seg, spk, sent in final_result:
    line = f'{seg.start:.2f} {seg.end:.2f} {spk} {sent}'
    print(line)


