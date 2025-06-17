import speech_recognition as sr
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from deep_translator import GoogleTranslator
from gtts import gTTS

class MovieManager:
     
     def get_audio(self, mp4_file, mp3_file):
          vc = VideoFileClip(mp4_file)
          ac = vc.audio
          ac.write_audiofile(mp3_file)
          ac.close()
          vc.close()

     def remove_audio(self, mp4_file, output_mp4):
         video = VideoFileClip(mp4_file)
         video_wa = video.without_audio()
         video_wa.write_videofile(output_mp4)
         video_wa.close()
         video.close

     def get_wav_audio(self, mp4_file, wav_file):
         vc = VideoFileClip(mp4_file)
         ac = vc.audio
         ac.write_audiofile(wav_file, codec="pcm_s16le")
         ac.close()
         vc.close()

     def audio_to_text(self, audio_file):
         r = sr.Recognizer()
         with sr.AudioFile(audio_file) as source:
             audio = r.record(source)
         try:
             text = r.recognize_google(audio)
             return text
         except:
             return "unknow"
         
     def text_to_speech(self, to_translate, to_lag):
         translated = GoogleTranslator(source = 'auto', taget = to_lang).translate(to_translate)
         print(translated)
         myobj = gTTS(text=translated, lang = top_lang, slow = False)
         myobj.save("welcome.mp3")

     def add_audio_to_video(self, mp4_file, mp3_file, out_file):
         videoclip = VideoFileClip(mp4_file)
         audioclip = AudioFileClip(mp3_file)

         new_audioclip = CompositeAudioClip([audioclip])
         videoclip.audio = new_audioclip
         videoclip.write_videofile(out_file)

mm = MovieManager()

speech = mm.audio_to_text("audio.wav")
mm.text_to_speech(speech, 'ru')
                    
        

         