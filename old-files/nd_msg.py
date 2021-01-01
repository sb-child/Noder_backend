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


class MsgExec:
    def __init__(self, skt_id: str):
        self.skt_id = skt_id
        self.dict_keys = ["type", "data", "msgID"]
        self.cmd_types = ["info", "login", "ops"]

    def executeCmd(self, data: dict, sid: str):
        # {"type": "xxx", "data": {...}, "msgID": "q2ww3e4r5t6y"}
        if not nd_utils.checkDict(self.dict_keys, data):
            return
        if data["type"] not in self.cmd_types:
            return
        _dt = data["type"]
        if _dt == "info":
            pass
        elif _dt == "login":
            pass
        elif _dt == "ops":
            pass

    def send(self, ):
        pass
