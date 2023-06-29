# podcast-toolkit
This project is aimed at transcribing and summarizing podcasts using OpenAI Whisper, Pyannote, and ChatGPT models. This is an ongoing commerical development.

## Table of Contents

- [About](#about)
- [Updates](#Updates)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)

## About

This project utilizes OpenAI Whisper, Pyannote, and ChatGPT models to transcribe and summarize podcasts. The goal is to provide an accurate and efficient solution for podcast transcription and summarization tasks.
Development came out of the need for business applications in the Podcasting space to automate podcast episodes and document insights from speakers.*

*Depending on progress, application may expand to more audio forms other than podcasting.

## Updates

6/27/23 Log:
- Basic script running - outputs a table consisting of: Timestamp, Speaker #, Transcription
- Ways to download podcast audio files (.mp3)
- - Where to download podcast .mp3 https://podcastindex.org/podcast/551334
- ffmpeg and pydub needed
- Pyannote repo used for speaker diarization - creating feature labels
-   https://github.com/yinruiqing/pyannote-whisper -- really good documentation on using Whisper/pyannote/ChatGPT models
- pyannote takes in .wav only it seems
- Whisper repo - used for transcription, timestamp segments
- openai library used only for API key access so far
- Dissecting OpenAI Whisper Response https://analyzingalpha.com/openai-whisper-python-tutorial
- Python convert mp3 to wav with Pydub https://stackoverflow.com/questions/32073278/python-convert-mp3-to-wav-with-pydub

## Features
In Progress...

## Usage
In Progress...

## Contributing
If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## References
- Pyannote documentation https://github.com/yinruiqing/pyannote-whisper
- OpenAI API Speech-to-Text https://platform.openai.com/docs/guides/speech-to-text/speech-to-text-beta
- Whisper API - https://github.com/openai/whisper
