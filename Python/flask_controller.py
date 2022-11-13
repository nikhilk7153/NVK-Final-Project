import json

from flask import Flask
from flask import Response

from google_helper import GoogleHelper
from rake_keyword_extract import RakeExtract

app = Flask(__name__)


@app.route('/api/keywords/<place_id>', methods=['GET'])
def get_keywords(place_id):
    google = GoogleHelper()
    # get the reviews
    reviews_list = google.get_reviews_from_id(place_id)
    # if none returned then it's a bad request
    if reviews_list is None:
        return "No reviews found for the link", 400
    # extract only the keywords, and not their bias
    keywords_list = []
    for review in reviews_list:
        extracted_keywords = RakeExtract(review)
        for keyword in extracted_keywords:
            keywords_list.append(keyword[0])
    # return the keywords as a json list
    js = keywords_list
    return Response(json.dumps(js),  mimetype='application/json')
