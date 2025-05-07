from googleapiclient.discovery import build
import pandas as pd
import time

API_KEY = "AIzaSyC0C_nQJVSjKE3wznBIa-KQz1eGFGX7Bd0"

youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_comments(video_id, max_results=100):
    comments = []
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100,
        textFormat='plainText'
    )
    response = request.execute()
    
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
    
    return comments

if __name__ == '__main__':
    video_df = pd.read_csv('../data/trending_videos.csv')
    all_comments = []

    for _, row in video_df.iterrows():
        print(f"Fetching comments for: {row['title']}")
        try:
            comments = get_comments(row['video_id'])
            for c in comments:
                all_comments.append({'video_id': row['video_id'], 'title': row['title'], 'comment': c})
            time.sleep(1)  # gotta avoid hitting API quota
        except Exception as e:
            print("Error:", e)
            continue

    comment_df = pd.DataFrame(all_comments)
    comment_df.to_csv('../data/comments.csv', index=False)
    print("Comments saved!")
