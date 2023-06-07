import os
import pyttsx3
from pydub import AudioSegment
from moviepy.editor import *
from moviepy.video.fx import resize
from convert import convert_text_to_list, filter_bad_words
from wordDuration import calculate_word_durations
from subreddit import get_top_posts
from redditScrap import getContent
from MakeVideo import merge_video_and_audio

# Example usage
video_file = "par.mp4"
audio_file = "temp2.wav"
title_image_path = "title.png"
ttsRate = 175

# Get the top 5 non-NSFW posts from the subreddit
top_posts = get_top_posts("tifu")

for i, post in enumerate(top_posts, start=1):
    print(f"Post #{i}:")
    print("Title:", post[0])
    print("URL:", post[1])
    content = getContent(post[1])

    title = post[0] #"TIFU by inviting a friend to the dead dad club"
    title = filter_bad_words(title)
    output_file = "{}.mp4".format(title)

    text_list = convert_text_to_list(title, content) 

    for i in range(len(text_list)):
      text_list[i] = filter_bad_words(text_list[i])

    text_list_subtitle = text_list

    merge_video_and_audio(video_file, text_list, text_list_subtitle, audio_file, output_file, ttsRate, title_image_path)