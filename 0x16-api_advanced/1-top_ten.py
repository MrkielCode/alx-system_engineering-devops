import requests

def top_ten(subreddit):
    # Set a custom User-Agent to avoid issues
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    # Make a request to the Reddit API to get the hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Check if the 'data' key and 'children' key are present in the response
        if 'data' in data and 'children' in data['data']:
            # Extract information about each post
            for post in data['data']['children'][:10]:
                post_data = post['data']
                print(f'Title: {post_data["title"]}')
        else:
            print(f"Subreddit '{subreddit}' not found or has no hot posts.")
    else:
        print(f'Error: {response.status_code}')

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
