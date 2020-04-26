import json
from serpwow.google_search_results import GoogleSearchResults
import search_res_found as srf
import choice_vote_aggr as cva

MY_SERPWOW_API_KEY = "3E571B595491441CA1326446856073E5"


def object_decoder(list_json, voter_engine):
    return [srf.SearchResultFound(json_obj, voter_engine) for json_obj in list_json]


def intr(com_res):
    # links_2d = [[el.link for el in sublist] for sublist in com_res]
    # print(links_2d)
    # link_set = set(links_2d[0]).intersection(*links_2d[1:])

    intr_res = []
    for sub in com_res:
        for el in sub:
            flag = False
            for _sub in com_res:
                if el.link not in [item.link for item in _sub]:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                intr_res.append(el)
    return intr_res


def group_by_search_engine(inter_list):
    res_map = {}
    for item in inter_list:
        res_map[item.voter_engine] = []
    for item in inter_list:
        res_map[item.voter_engine].append(item)
    return res_map


def make_preferences_by_search_engines(input_map):
    """
    визначення відносної вагомості
    sort by positions
    """
    for k, v in input_map.items():
        # To return a new list, use the sorted() built-in function...
        input_map[k] = sorted(input_map[k], key=lambda x: x.position, reverse=False)
    return input_map


def populate_candidates(input_map):
    """
    :param input_map:  string=>list
    :return:
    """
    candidates = set()
    for k, lst in input_map.items():
        for el in lst:
            candidates.add(el.link)
    return candidates


def populate_preferences(input_map):
    """
    :param input_map:  string=>list
    :return:
    """
    preferences = []
    for k, lst in input_map.items():
        sublist = []
        for el in lst:
            # eliminate duplicates with preserving order
            if el.link not in sublist:
                sublist.append(el.link)
        preferences.append(sublist)
    return preferences


def populate_search_results():
    query = input("WRITE YOUR SEARCH QUERY:")
    search_params = {"q": query, "location": "Austin, Texas"}
    # search_engines = ["yandex", "google"]
    search_engines = ["yandex", "google", "bing", "naver"]
    searcher = GoogleSearchResults(MY_SERPWOW_API_KEY)

    common_result = []  # 2d
    for engine in search_engines:
        print("*" * 300)
        print("" + engine + " RESULT")
        print("*" * 300)

        data = searcher.get_json({**search_params,
                                  **{"engine": engine}})
        result = data["organic_results"]

        # json_formatted_str = json.dumps(result, indent=2)
        # print(json_formatted_str)

        mapped_entities = object_decoder(result, engine)
        [obj.pretty_print() for obj in mapped_entities]

        common_result.append(mapped_entities)

    return common_result


if __name__ == '__main__':
    common_result = populate_search_results()

    print("=" * 100)
    intr_res = intr(common_result)
    print([obj.pretty_print() for obj in intr_res])

    res_map = group_by_search_engine(intr_res)
    prefs_groups = make_preferences_by_search_engines(res_map)

    candidates = populate_candidates(prefs_groups)
    preferences = populate_preferences(prefs_groups)

    aggr = cva.Aggregator(candidates, preferences)

    print("\n\nBORDA METHOD: ")
    aggr.borda()
    print("\n\nCONDORCET METHOD: ")
    aggr.condorcet_pairwise_comparison()

















