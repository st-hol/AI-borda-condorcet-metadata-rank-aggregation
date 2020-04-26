# from googlesearch import search
#
# query = "apple iphone news 2019"
#
# my_results_list = []
# for i in search(query,  # The query you want to run
#                 tld='com',  # The top level domain
#                 lang='en',  # The language
#                 num=10,  # Number of results per page
#                 start=0,  # First result to retrieve
#                 stop=None,  # Last result to retrieve
#                 pause=2.0,  # Lapse between HTTP requests
#                 ):
#     my_results_list.append(i)
#     print(i)
#
# import json
#
# from serpwow.baidu_search_results import BaiduSearchResults
# from serpwow.bing_search_results import BingSearchResults
# from serpwow.google_scholar_search_results import GoogleScholarSearchResults
# from serpwow.google_search_results import GoogleSearchResults
# from serpwow.yahoo_search_results import YahooSearchResults
# from serpwow.yandex_search_results import YandexSearchResults
#
# search_params = {"q": "wow", "location": "Austin,Texas"}
# search_clients = [GoogleSearchResults(search_params), BingSearchResults(search_params), BaiduSearchResults(search_params), GoogleScholarSearchResults(search_params)]
#
# for client in search_clients:
#     data = client.get_json()
#     # result = data["organic_results"]
#     json_formatted_str = json.dumps(data, indent=2)
#     print(json_formatted_str)
#     print("*"*100)
#
# # client = GoogleSearchResults()
# # result = client.get_dict()
# #
# # client = BingSearchResults({"q": "Coffee", "location": "Austin,Texas"})
# # data = client.get_json()
# #
# # client = BaiduSearchResults({"q": "Coffee"})
# # data = client.get_json()
# #
# # client = GoogleScholarSearchResults({"q": "Coffee"})
# # data = client.get_json()
#
# # client = YandexSearchResults({"text": "Coffee"})
# # data = client.get_json()
#
# # client = YahooSearchResults({"p": "Coffee"})
# # data = client.get_json()
# #
# # json_formatted_str = json.dumps(data, indent=2)
# # print(json_formatted_str)


import json
from serpwow.google_search_results import GoogleSearchResults

search_params = {"q": "wow", "location": "Austin, Texas"}
search_engines = ["yandex", "google"]
# search_engines = ["yandex", "google", "bing", "naver", "amazon"]
searcher = GoogleSearchResults("53B07FA3EE984B17AFE7300A43EA4FB6")

for engine in search_engines:
    print("*" * 300)
    print("" + engine + " RESULT")
    print("*" * 300)
    data = searcher.get_json({**search_params, **{"engine": engine}})
    result = data["organic_results"]
    json_formatted_str = json.dumps(result, indent=2)
    print(json_formatted_str)






