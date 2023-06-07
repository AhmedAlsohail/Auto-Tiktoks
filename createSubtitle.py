import pyttsx3
from moviepy.editor import *

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the output file name and path
output_file = 'output.mp4'

# Set the path to your input video file
video_file = 'v.mp4'

# Set the path to your input text file
text_file = 'a.txt'

# Read the text file
with open(text_file, 'r') as file:
    text = file.read()

# Create a list of words with their start and end times
spoken_words = []

def on_word(name, location, length):
    # name: The word being spoken
    # location: The character index where the word starts in the text
    # length: The length of the word in characters
    start_time = len(spoken_words) * 0.5  # Assuming 0.5 seconds per word
    end_time = (len(spoken_words) + 1) * 0.5
    spoken_words.append((name, start_time, end_time))

engine.connect('started-word', on_word)
engine.save_to_file(text, 'output_audio.mp3')
engine.runAndWait()

# Load the generated audio file
audio = AudioFileClip('output_audio.mp3')

# Load the video file
video = VideoFileClip(video_file)

# Create empty subtitles clip
subtitles = VideoClip(make_frame=lambda t: [[[0, 0, 0]]])

# Create the subtitle clips for each word
for word, start, end in spoken_words:
    subtitle = TextClip(word, fontsize=30, color='white', bg_color='black')
    subtitle = subtitle.set_start(start).set_end(end).set_duration(end - start)
    subtitles = concatenate_videoclips([subtitles, subtitle])

# Set the final video duration to match the audio duration
final_video = video.set_duration(audio.duration)

# Set the audio of the final video
final_video = final_video.set_audio(audio)

# Overlay the subtitles on the final video
final_video = CompositeVideoClip([final_video, subtitles.set_position(('center', 'bottom'))])

# Write the final video with subtitles to a file
final_video.write_videofile(output_file, codec='libx264', audio_codec='aac')
