# Twitter Sentiment Analysis for I-70

This Python script fetches recent tweets related to Interstate 70 (I-70) and performs sentiment analysis on them, providing insights into the public sentiment regarding this highway.

## Prerequisites

- Python 3.x
- `requests` library
- `transformers` library

## Installation

1. Ensure Python 3.x is installed on your system.

2. Install the required Python packages:

```bash
pip install requests transformers
```

3. Obtain a Bearer Token from Twitter's Developer Portal and replace `'YOUR_BEARER_TOKEN'` in the script with your actual Bearer Token.

## Usage

Run the script using Python:

```bash
python analyze_tweets.py
```

The script will fetch recent tweets mentioning "I-70", perform sentiment analysis, and print the results, including the sentiment label (POSITIVE/NEGATIVE) and confidence score.

## Customization

You can customize the query and the number of tweets to analyze by modifying the `query` and `max_results` parameters in the `main` function.

## Note

This script is for educational purposes and should be used in accordance with Twitter's Developer Agreement and Policy.

### Instructions for Use

1. **Replace the placeholder `'YOUR_BEARER_TOKEN'`** in the Python script with your actual Twitter API Bearer Token.
2. **Run the Python script:** Navigate to the directory containing `analyze_tweets.py` and execute it using your Python environment.
3. **Read the `README.md`** for installation instructions, usage, and customization options.

### Example Output 

```
Tweet: Loving the clear roads on I-70 today! Smooth driving and great views.
Sentiment: POSITIVE, Confidence: 0.9874

Tweet: Avoid I-70 at all costs! Traffic is a nightmare.
Sentiment: NEGATIVE, Confidence: 0.9652

Tweet: I-70 is surprisingly empty this morning. Is everyone okay?
Sentiment: NEUTRAL, Confidence: 0.7603

Tweet: The construction on I-70 is taking forever. It's been months now!
Sentiment: NEGATIVE, Confidence: 0.9485

Tweet: Just took a trip along I-70. The new scenery is beautiful!
Sentiment: POSITIVE, Confidence: 0.9821
```

This setup gives you a straightforward way to analyze sentiment toward I-70 using Twitter data, combining API data fetching with powerful sentiment analysis capabilities.
