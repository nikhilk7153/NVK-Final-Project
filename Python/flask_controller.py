from flask import Flask
from yelp_helper import YelpHelper
from rake_keyword_extract import RakeExtract

app = Flask(__name__)


@app.route('/api/keywords/<link>', methods=['GET'])
def get_keywords(link):
    yelp = YelpHelper()
    reviews_list = yelp.yelp_reviews_from_link(link)
    if reviews_list is None:
        return "No reviews found for the link", 400
    keywords_list = []
    for review in reviews_list:
        extracted_keywords = RakeExtract(review)
        for keyword in extracted_keywords:
            keywords_list.append(keyword)[0]
    return {keywords_list}
