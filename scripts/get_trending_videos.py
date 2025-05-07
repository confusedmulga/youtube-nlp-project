from googleapiclient.discovery import build
import pandas as pd

# Replace with your actual API key
API_KEY = "AIzaSyC0C_nQJVSjKE3wznBIa-KQz1eGFGX7Bd0"

youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_trending_videos(region='IN', max_results=10):
    request = youtube.videos().list(
        part='snippet',
        chart='mostPopular',
        regionCode=region,
        maxResults=max_results
    )
    response = request.execute()
    
    videos = []
    for item in response['items']:
        video_id = item['id']
        title = item['snippet']['title']
        videos.append({'video_id': video_id, 'title': title})
    
    return pd.DataFrame(videos)

if __name__ == '__main__':
    df = get_trending_videos()
    df.to_csv('../data/trending_videos.csv', index=False)
    print("Trending videos saved!")
