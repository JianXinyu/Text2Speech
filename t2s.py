#!/usr/bin/python
# -*- coding: utf-8 -*-

from google.cloud import texttospeech
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\key.json"

import re
from langdetect import detect

def t2s(lang, text, filename):
        # Instantiates a client
        client = texttospeech.TextToSpeechClient()

        # Set the text input to be synthesized
        synthesis_input = texttospeech.types.SynthesisInput(text=text)

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.types.VoiceSelectionParams(
            language_code=lang,
            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

        # Select the type of audio file you want returned
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(synthesis_input, voice, audio_config)

        # The response's audio_content is binary.
        with open(filename+'.mp3', 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "'+filename+'.mp3"') 

# 读取文本
# 分割段落
# 识别中英文
# 每段转为语音
# 合并语音文件
# 删除多余文件
if __name__ == "__main__":
    
    p=re.compile('\n',re.S)
    fileContent=open('test2.txt','r',encoding='utf8').read()#读文件内容
    paraList=p.split(fileContent) #根据换行符对文本进行切片


    for paraIndex in range(len(paraList)):#遍历切片后的文本列表
        lang = detect(paraList[paraIndex])
        t2s(lang, paraList[paraIndex], str(paraIndex))

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
