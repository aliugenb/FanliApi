# __author__ = Roger
# -*- coding: utf-8 -*-


class TraversalJson:
    def __init__(self):
        self.json_dict = {}

    def traversal_json(self, json_result):
        for key in json_result.keys():
            cmp_key = key.encode("utf-8")
            if isinstance(json_result[key], dict):
                self.json_dict[cmp_key] = json_result[key]
                self.traversal_json(json_result[key])

            elif isinstance(json_result[key], list):
                self.json_dict[cmp_key] = json_result[key]
                # 如果对象为list,继续遍历list中对象是否有dict
                for value in json_result[key]:
                    self.traversal_json(value)
            else:
                self.json_dict[cmp_key] = json_result[key]
        return self.json_dict
