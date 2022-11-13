import requests

"""
You can use this link to find the ids of places for now.
https://developers.google.com/maps/documentation/places/web-service/place-id
"""


class GoogleHelper:
    def __init__(self,
                 api_key="AIzaSyDBlcm5umGwbO8xPO96CGUp-dQ8-Md1isg"):
        self.api_key = api_key

    # find get the reviews by google place id and return their text as a list
    def get_reviews_from_id(self, place_id):
        url = "https://maps.googleapis.com/maps/api/place/details/json"
        headers = {}
        url_params = {'place_id': place_id,
                      'fields': 'reviews', 'reviews_no_translations': 'false',
                      'key': self.api_key}
        search_response = requests.request("GET", url,
                                           headers=headers, params=url_params)
        # if we didn't get the expected response then something went wrong
        if search_response.status_code != 200:
            return None
        # extract the text from reviews and return it as list
        text_reviews = []
        for review in search_response.json()['result']['reviews']:
            text_reviews.append(review['text'])
        return text_reviews


if __name__ == "__main__":
    google = GoogleHelper()
    reviews_list = google.get_reviews_from_id("ChIJ4Vrk3Bo3DogRpHfXxy0yu98")
    print(reviews_list)
