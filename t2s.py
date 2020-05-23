#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""

from google.cloud import texttospeech
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\key.json"
# # Instantiates a client
# client = texttospeech.TextToSpeechClient()

# # Set the text input to be synthesized
# synthesis_input = texttospeech.types.SynthesisInput(text="This quickstart introduces you to Text-to-Speech. In this quickstart, you set up your Google Cloud Platform project and authorization and then make a request for Text-to-Speech to create audio from text. To learn more about the fundamental concepts in Text-to-Speech, read Text-to-Speech Basics.")

# # Build the voice request, select the language code ("en-US") and the ssml
# # voice gender ("neutral")
# voice = texttospeech.types.VoiceSelectionParams(
#     language_code='en-US',
#     ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

# # Select the type of audio file you want returned
# audio_config = texttospeech.types.AudioConfig(
#     audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# # Perform the text-to-speech request on the text input with the selected
# # voice parameters and audio file type
# response = client.synthesize_speech(synthesis_input, voice, audio_config)

# # The response's audio_content is binary.
# with open('output.mp3', 'wb') as out:
#     # Write the response to the output file.
#     out.write(response.audio_content)
#     print('Audio content written to file "output.mp3"')

def synthesize_ssml(ssml):
    """Synthesizes speech from the input string of ssml.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/

    Example: <speak>Hello there.</speak>
    """
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(ssml=ssml)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        name='en-US-Standard-C',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


# 读取文本
# 分割段落
# 识别中英文
# 每段转为语音
# 合并语音文件
# 删除多余文件

import re
from langdetect import detect
p=re.compile('\n',re.S)
fileContent=open('test.txt','r',encoding='utf8').read()#读文件内容
paraList=p.split(fileContent) #根据换行符对文本进行切片


for paraIndex in range(len(paraList)):#遍历切片后的文本列表
    lang = detect(paraList[paraIndex])
    if(lang == "zh-cn"):
        # Instantiates a client
        client = texttospeech.TextToSpeechClient()

        # Set the text input to be synthesized
        synthesis_input = texttospeech.types.SynthesisInput(text=paraList[paraIndex])

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='zh-CN',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

        # Select the type of audio file you want returned
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(synthesis_input, voice, audio_config)

        # The response's audio_content is binary.
        with open(str(paraIndex)+'.mp3', 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "'+str(paraIndex)+'.mp3"')     
    elif(lang == "en"):
        # Instantiates a client
        client = texttospeech.TextToSpeechClient()

        # Set the text input to be synthesized
        synthesis_input = texttospeech.types.SynthesisInput(text=paraList[paraIndex])

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

        # Select the type of audio file you want returned
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(synthesis_input, voice, audio_config)

        # The response's audio_content is binary.
        with open(str(paraIndex)+'.mp3', 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "'+str(paraIndex)+'.mp3"')

    # fileWriter=open(str(paraIndex)+'.txt','a',encoding='utf8')#创建一个写文件的句柄
    # fileWriter.write(paraList[paraIndex])#先将列表中元素写入文件中
    # fileWriter.close() #关闭当前句柄
mp3_write = open('all.mp3', 'wb')
for paraIndex in range(len(paraList)):
    f_read = open(str(paraIndex)+'.mp3', 'rb')
    mp3_write.write(f_read.read())
    f_read.close()
    os.remove(str(paraIndex)+'.mp3')
mp3_write.flush()
mp3_write.close()
print('finished')
