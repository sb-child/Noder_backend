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
from typing import Union

import nd_file_manager
import pymongo


class Workspace:
    def __init__(self):
        # self.ws_files = nd_file_manager.FileManager()
        pass


class WorkspaceManager:
    def __init__(self, db_host: str, db_port: int, db_name: str, files_dir: str):
        self.files_dir = files_dir
        self.db_name = db_name
        self.db_port = db_port
        self.db_host = db_host
        self.db = pymongo.MongoClient(host=db_host, port=db_port)
        self.wsDb = self.db[db_name]["workspaces"]

    def addWorkspace(self, name: str):
        pass

    def removeWorkspace(self, name: Union[str, None], wid: Union[str, None]):
        pass

    def getWorkspace(self, name: Union[str, None], wid: Union[str, None]):
        pass

    def getWorkspaceCount(self):
        pass

    def __getitem__(self, item):
        pass

    def __len__(self):
        pass
