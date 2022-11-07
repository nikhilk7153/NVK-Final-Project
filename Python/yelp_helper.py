import requests


class YelpHelper:
    def __init__(self,
                 api_key="F6vsTDv2v2j-VjULctcSCUEmRRFs6bQ9tYQdHheyD0li2QNT-W7_BJcKa9zC7q626CFBv78g0iQ2GXFND9L3ZR"
                         "-NAY0tTEZGUZ9nIYqb2GUB96m6XrgATcP_UOztYXYx"):
        self.api_key = api_key
        self.reviews = []

    def yelp_reviews_by_id(self, business_id):
        json_response = self.__make_request(business_id)
        return self.__extract_reviews(json_response)

    def yelp_search(self, location, limit=50, offset=0):
        url = "https://api.yelp.com/v3/businesses/search"
        headers = {'Authorization': 'Bearer ' + self.api_key}
        url_params = {'location': location.replace(' ', '+'),
                      'limit': limit, 'offset': offset}
        search_response = requests.request("GET", url,
                                           headers=headers, params=url_params)
        return search_response.json()["businesses"]

    def __make_request(self, business_id):
        url = 'https://api.yelp.com/v3/businesses/' + business_id + '/reviews'
        headers = {'Authorization': 'Bearer ' + self.api_key}
        url_params = {}
        response = requests.request("GET", url, headers=headers, params=url_params)
        return response.json()

    def __extract_reviews(self, response_json):
        result = []
        reviews = list(response_json["reviews"])
        for review in reviews:
            result.append(review["text"])
        self.reviews = result
        return result


if __name__ == "__main__":
    yelp = YelpHelper()
    reviews_list = yelp.yelp_reviews_by_id("qjnpkS8yZO8xcyEIy5OU9A")
    print(reviews_list)
