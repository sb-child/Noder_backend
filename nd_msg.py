# coding=utf-8

#  Noder - A node-based editor
#  Copyright (C) 2020 sbchild
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
