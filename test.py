import os
from gtts import gTTS
from moviepy.editor import TextClip, concatenate_videoclips

def generate_video_with_subtitles(lines, output_path):
    # Initialize an empty list to store the subtitle clips
    subtitle_clips = []

    # Set the desired speech speed (in words per minute)
    speech_speed = 120

    # Iterate over each line and generate subtitle clips
    for line in lines:
        # Generate TTS audio for the current line
        tts = gTTS(line)
        audio_path = "temp_audio.mp3"
        tts.save(audio_path)

        # Calculate the duration of the TTS audio based on text length and speech speed
        words_per_second = speech_speed / 60
        audio_duration = len(line.split()) / words_per_second

        # Create a TextClip object for the subtitle line
        subtitle_clip = TextClip(line, fontsize=30, color='white', bg_color='black').set_duration(audio_duration)

        # Append the subtitle clip to the list
        subtitle_clips.append(subtitle_clip)

        # Clean up the temporary audio file
        os.remove(audio_path)

    # Concatenate the subtitle clips into a single video clip
    video = concatenate_videoclips(subtitle_clips)

    # Set the video duration to a maximum of 5 seconds
    max_duration = 5
    if video.duration > max_duration:
        video = video.subclip(0, max_duration)

    # Set the audio file as the audio of the video
    video = video.set_audio(subtitle_clips[0].audio)

    # Save the final video with subtitles
    video.write_videofile(output_path, codec='libx265', fps=30)

# Example usage:
lines = ['Line 1', 'Line 2', 'Line 3']
output_path = 'output_video.mp4'
generate_video_with_subtitles(lines, output_path)
