import requests


class YelpHelper:
    def __init__(self,
                 api_key="F6vsTDv2v2j-VjULctcSCUEmRRFs6bQ9tYQdHheyD0li2QNT-W7_BJcKa9zC7q626CFBv78g0iQ2GXFND9L3ZR"
                         "-NAY0tTEZGUZ9nIYqb2GUB96m6XrgATcP_UOztYXYx"):
        self.api_key = api_key
        self.name = ""
        self.id = ""
        self.reviews = []

    def yelp_reviews_from_link(self, link):
        business_id = self.yelp_business_id(link)
        return self.yelp_reviews_by_id(business_id)

    def yelp_business_id(self, link):
        self.name = link.split("/")[-1]
        return self.__make_business_request(self.name)

    def yelp_reviews_by_id(self, business_id):
        json_response = self.__make_reviews_request(business_id)
        return self.__extract_reviews(json_response)

    def yelp_search(self, location, limit=50, offset=0):
        url = "https://api.yelp.com/v3/businesses/search"
        headers = {'Authorization': 'Bearer ' + self.api_key}
        url_params = {'location': location.replace(' ', '+'),
                      'limit': limit, 'offset': offset}
        search_response = requests.request("GET", url,
                                           headers=headers, params=url_params)
        return search_response.json()["businesses"]

    def __make_business_request(self, name):
        url = "https://api.yelp.com/v3/businesses/" + name
        headers = {'Authorization': 'Bearer ' + self.api_key}
        search_response = requests.request("GET", url,
                                           headers=headers)
        self.id = search_response.json()['id']
        return self.id

    def __make_reviews_request(self, business_id):
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
    reviews_list = yelp.yelp_reviews_from_link("https://www.yelp.com/biz/la-fitness-chicago-5?osq=La+Fitness")
    print(reviews_list)
    reviews_list = yelp.yelp_reviews_from_link("https://www.yelp.com/biz/healthy-substance-chicago")
    print(reviews_list)
