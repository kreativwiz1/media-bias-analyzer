import streamlit as st
import re
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
from textblob import TextBlob
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Getting the API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Initialize the OpenAI client
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize the YouTube API client
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# ... rest of your code



# Initialize the OpenAI client
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize the YouTube API client
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def get_video_id(url):
    video_id_match = re.match(r'.*v=([^&]+).*', url)
    if video_id_match:
        return video_id_match.group(1)
    else:
        raise ValueError('Invalid YouTube URL')

def fetch_transcript(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id)

def transcript_to_text(transcript):
    return "\n".join([entry['text'] for entry in transcript])

def get_video_details(video_id):
    request = youtube.videos().list(part="snippet,contentDetails,statistics", id=video_id)
    response = request.execute()
    if 'items' in response and len(response['items']) > 0:
        video = response['items'][0]
        details = {
            "title": video['snippet']['title'],
            "description": video['snippet']['description'],
            "published_at": video['snippet']['publishedAt'],
            "view_count": video['statistics']['viewCount'],
            "like_count": video['statistics']['likeCount'],
            "dislike_count": video['statistics'].get('dislikeCount', 'N/A'),
            "comment_count": video['statistics']['commentCount']
        }
        return details
    else:
        return None

def get_top_comments(video_id, max_results=10):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results,
        order="relevance"
    )
    response = request.execute()
    comments = []
    for item in response['items']:
        top_comment = item['snippet']['topLevelComment']['snippet']
        comments.append({
            "author": top_comment['authorDisplayName'],
            "text": top_comment['textDisplay'],
            "like_count": top_comment['likeCount']
        })
    return comments

# Streamlit UI
st.title("AI Media Bias Analyzer")

youtube_url = st.text_input("Enter YouTube URL:")
if st.button("Analyze"):
    try:
        video_id = get_video_id(youtube_url)
        video_details = get_video_details(video_id)
        transcript = fetch_transcript(video_id)
        transcript_text = transcript_to_text(transcript)
        comments = get_top_comments(video_id)

        # Generate the response from OpenAI
        with st.chat_message("assistant"):
            response = openai_client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": "Given a video transcript and viewer comments, analyze the media's polarization and bias. Utilize the provided transcript to identify language patterns and framing techniques that may indicate bias. Additionally, consider viewer comments to gauge audience perceptions and reactions. Use meter to communicate the level of polarization and bias present in the media content."},
                    {"role": "user", "content": f"Video Details: {video_details}\n\nTranscript: {transcript_text}\n\nComments: {comments}\n\nGiven a video transcript and viewer comments, analyze the media's polarization and bias. Utilize the provided transcript to identify language patterns and framing techniques that may indicate bias. Additionally, consider viewer comments to gauge audience perceptions and reactions. Using a scale from 1 to 10, where 1 represents extreme bias and polarization and 10 represents complete objectivity and neutrality, rate the media content in the following categories: Objectivity: How impartial and unbiased is the content,Balance: Does the content present diverse perspectives or viewpoints?,Neutrality: To what extent does the content refrain from promoting a particular agenda or ideology?,Engagement: How effectively does the content engage with viewer comments and feedback? Please provide a summary of your analysis along with the scores for each category. Also, include the sample size of viewers, including the number of comments analyzed, to contextualize the analysis."}
                ]
            )
            report_text = response.choices[0].message.content
            st.write(report_text)

    except Exception as e:
        st.error(f"Error: {e}")
