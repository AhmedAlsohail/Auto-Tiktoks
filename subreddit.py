import requests
from bs4 import BeautifulSoup

def get_top_posts(subreddit):
    # Make a request to the subreddit using the Reddit API
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    url = f'https://www.reddit.com/r/{subreddit}/top/.json?sort=top&t=day&limit=10'
    response = requests.get(url, headers=headers)

    # Parse the JSON response
    data = response.json()

    # Extract the titles and URLs of the top 5 non-NSFW posts
    posts = data['data']['children']
    top_posts = []
    count = 0
    for post in posts:
        title = post['data']['title']
        post_url = post['data']['url']
        is_nsfw = post['data']['over_18']
        
        if not is_nsfw:
            top_posts.append((title, post_url))
            count += 1

        if count == 5:
            break

    return top_posts

# Enter the subreddit name
subreddit_name = "tifu"

# Get the top 5 non-NSFW posts from the subreddit
top_posts = get_top_posts(subreddit_name)

# Print the results
for i, post in enumerate(top_posts, start=1):
    print(f"Post #{i}:")
    print("Title:", post[0])
    print("URL:", post[1])
    print()
