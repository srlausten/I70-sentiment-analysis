import requests
from transformers import pipeline

# Twitter API Bearer Token
bearer_token = 'YOUR_BEARER_TOKEN'

# Setup for sentiment analysis
sentiment_pipeline = pipeline("sentiment-analysis")

# Function to create the request headers with the Bearer Token
def create_headers(bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    return headers

# Function to get tweets
def get_tweets(query, max_results=10):
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    
    # Change to the query parameters as needed
    query_params = {'query': query, 'max_results': max_results}
    headers = create_headers(bearer_token)
    
    response = requests.get(search_url, headers=headers, params=query_params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    
    return response.json()

# Function to analyze sentiments of tweets
def analyze_tweets(tweets):
    texts = [tweet['text'] for tweet in tweets['data']]
    results = sentiment_pipeline(texts)
    return results

# Main function to fetch tweets, analyze them, and print results
def main():
    query = "I-70 -filter:retweets"
    tweets = get_tweets(query)
    if 'data' in tweets:
        analysis_results = analyze_tweets(tweets)
        for tweet, sentiment in zip(tweets['data'], analysis_results):
            print(f"Tweet: {tweet['text']}\nSentiment: {sentiment['label']}, Confidence: {sentiment['score']:.4f}\n")
    else:
        print("No tweets found.")

if __name__ == "__main__":
    main()
