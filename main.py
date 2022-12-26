import json


test_list = [{"key1": "value1"},
             {"k1": "v1", "k2": "v2",
             "k3": "v3"},
             {},
             {},
             {"key1": "value1"},
             {"key1": "value1"},
             {"key2": "value2"}]


def delete_doubles(lis: list) -> set:
    my_set = set()
    for dict_ in lis:
        my_set.add(json.dumps(dict_))
    return my_set

print(delete_doubles(test_list))