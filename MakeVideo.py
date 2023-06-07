import pyttsx3
from pydub import AudioSegment
from moviepy.editor import *
from moviepy.video.fx import resize

def get_speech_duration(text, rate):
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.setProperty("volume", 0.0)  # Mute the audio
    audio_file = "temp.wav"  # Temporary audio file path
    engine.save_to_file(text, audio_file)  # Save the speech to a temporary audio file
    engine.runAndWait()

    audio_segment = AudioSegment.from_wav(audio_file)
    duration = audio_segment.duration_seconds

    # Clean up temporary files
    # os.remove("temp.wav")

    return duration

def merge_video_and_audio(video_file, text_list, text_list_subtitle, audio_file, output_file, ttsRate, title_image_path):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty("rate", ttsRate)

    single_string = "\n".join(text_list)
    #engine.say(single_string)
    engine.save_to_file(single_string, 'temp2.wav')


    engine.runAndWait()

    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)
    
    audioDuration = audio.duration

    ##======================================
    # Create a text clip with the specified text
    # Set the duration of the text clip to match the duration of the video
    currentTime = 0.0
    currentItem = 0

    text_clips = []
    for i, text in enumerate(text_list_subtitle):
      duration = get_speech_duration(text, ttsRate)

      if(currentItem == 0): 
        photo = ImageClip(title_image_path, duration=duration)
        photo = photo.resize(width=490)  # Adjust the width as needed
        photo = photo.set_position('center')
        photo = photo.set_start(0)
        text_clips.append(photo)
        print("first")
        txt_clip = TextClip(text, fontsize=25 , color='black', font='Dubai-Bold', size=video.size, method='caption')
        txt_clip = txt_clip.set_position(('center', 'top'))
      else:
        txt_clip = TextClip(text, fontsize=56 , color='orange', font='Dubai-Bold', size=video.size,stroke_color = 'black', stroke_width = 2.6, method='caption')
        txt_clip = txt_clip.resize(width=400)  # Adjust the width as needed


      txt_clip = txt_clip.set_position(('center', 'top'))

      txt_clip = txt_clip.set_start(currentTime)
      txt_clip = txt_clip.set_duration(duration)

      currentTime += duration

      text_clips.append(txt_clip)

      currentItem = currentItem + 1

    # Adjust the video duration to match the audio duration
    video = video.set_duration(audioDuration)

    # Set audio to the video
    video = video.set_audio(audio)

    final_clip = CompositeVideoClip([video] + text_clips)

    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")