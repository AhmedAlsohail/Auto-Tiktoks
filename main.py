import os
import pyttsx3
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Example usage
video_file = "par.mp4"
text_list = ["TIFU by inviting a friend to the dead dad club", "Not today, this was a few years ago, etc.", "My dad died when I was a year old, so I've had plenty of time to come to terms with it. "]
audio_file = "temp2.wav"
output_file = "merged_video.mp4"

single_string = " ".join(text_list)
engine.say(single_string)
engine.save_to_file(single_string, 'temp2.wav')


engine.runAndWait()

def get_speech_duration(text, rate=150):
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

def merge_video_and_audio(video_file, text_list, audio_file, output_file):
    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)
    
    audioDuration = audio.duration

    ##======================================
    # Create a text clip with the specified text
    # Set the duration of the text clip to match the duration of the video
    currentTime = 0.0
    text_clips = []
    for i, text in enumerate(text_list):
      duration = get_speech_duration(text, engine.getProperty("rate"))

      txt_clip = TextClip(text, fontsize=25, color='white', font='Arial', size=video.size)
      txt_clip = txt_clip.set_position(('center', 'top'))
      txt_clip = txt_clip.set_duration(duration)
      txt_clip = txt_clip.set_start(currentTime)

      text_clips.append(txt_clip)

      currentTime += duration

    '''
      #=========================
      start_time = currentTime
      txt_clip = txt_clip.set_duration(duration)
      
      currentTime = currentTime + duration

      # Set the start time of the text clip
      txt_clip = txt_clip.set_start(start_time)
      
      # Set the position of the text clip on the video
      txt_clip = txt_clip.set_position(('center', 'top'))
    ##============================================
    '''

    # Adjust the video duration to match the audio duration
    video = video.set_duration(audioDuration)

    # Set audio to the video
    video = video.set_audio(audio)

    final_clip = CompositeVideoClip([video] + text_clips)

    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

    



merge_video_and_audio(video_file, text_list, audio_file, output_file)