import json

from flask import Flask
from flask import Response
from flask_cors import CORS

from google_helper import GoogleHelper
from rake_keyword_extract import RakeExtract
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)


@app.route('/api/keywords/<place_id>', methods=['GET'])
def get_keywords(place_id):
    google = GoogleHelper()
    # get the reviews
    reviews_list = google.get_reviews_from_id(place_id)
    # if none returned then it's a bad request
    if reviews_list is None:
        return "No reviews found for the link", 400
    # extract the data to return in proper json format
    keywords_list = []
    sid_obj = SentimentIntensityAnalyzer()
    for review in reviews_list:
        # extract keywords from each review
        extracted_keywords = RakeExtract(review)
        for keyword in extracted_keywords:
            # get the sentiment of the keyword
            sentiment_dict = sid_obj.polarity_scores(keyword[0])
            predicted_sentiment = "Neutral"
            if sentiment_dict['compound'] >= 0.10:
                predicted_sentiment = 'Positive'
            elif sentiment_dict['compound'] <= -0.10:
                predicted_sentiment = 'Negative'
            # add the keyword and sentiment to the final list to be returned
            keywords_list.append({"keyword": keyword[0], "importance": keyword[1], "sentiment": predicted_sentiment})

    js = {'keywords': keywords_list}
    # return response
    return Response(json.dumps(js), mimetype='application/json')
