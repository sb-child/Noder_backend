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

import pymongo
from pymongo.database import Database


class FileManager:
    def __init__(self, db: Database, file_id: str):
        self.db = db[f"ws_files:{file_id}"]
        # todo: a virtual directory tree


def main():
    # fm = FileManager("127.0.0.1", 27017, "test1")
    # fm.fileDb.insert_one({"name": "123"})
    # print(list(fm.fileDb.find({})))
    # fm.fileDb.drop()
    pass


if __name__ == '__main__':
    main()
