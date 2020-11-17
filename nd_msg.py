# coding=utf-8
import nd_utils
import json


class MsgConverter:
    def __init__(self, skt_id: str):
        self.skt_id = skt_id
        self.dirs = {
            "greeter": "greeter",
            "users": f"users/{skt_id}",
        }
        self.basic_struct = {
            "greeter": ["cmd"],
            "users": ["cmd"],
        }
        self.commands = {
            "greeter": ["get_user"],
            "users": ["-"],
        }

    def conv(self, path: str, text: str):
        # greeter: /greeter
        # user: /users/(id)/(uid)
        d = nd_utils.dirCheck(path, self.dirs)
        if len(d) == 0:
            return None
        if d[0] not in self.dirs.keys():
            return None
        dt = nd_utils.jsonFromStr(text)
        if not nd_utils.checkDict(self.basic_struct[d[0]], dt):
            return None
        if not nd_utils.checkDict(self.commands[d[0]], dt["cmd"]):
            return None
        # if d[0] == "greeter":
        # if dt["cmd"] == "get_user":
        return {"cli_type": d[0], "op": dt["cmd"]}
        # elif d[0] == "users":
        #     pass

    def send(self, ):
        pass
