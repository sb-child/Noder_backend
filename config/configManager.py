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
import configparser
import warnings
import re

CONF_login = "login.ini"
CONF_socket = "socket.ini"

BASIC_login = {
    "login": {
        "password": "",
        "max_user": 0
    },
}
BASIC_socket = {
    "socketIo": {
        "redis_url": "redis://127.0.0.1:6379/1",
        "host": "127.0.0.1",
        "port": 37321
    },
    "fileManager": {
        "file_dir": "files",
        "file_db_name": "noder_file_db",
        "file_db_host": "localhost",
        "file_db_port": 27017,
    },
}

FILTER_conf = re.compile(r"CONF_*")
FILTER_basic = re.compile(r"BASIC_*")


# _FILTER_filter = re.compile(r"FILTER_*")

def createDefaultFiles():
    # print(globals())
    #
    # def getVarsByRe(rec: re.Pattern):
    #     r = []
    #     for _i in globals():
    #         if rec.match(_i[0]) is not None:
    #             r.append(_i[1])
    #     return r

    _conf_vars = [CONF_login, CONF_socket]  # getVarsByRe(FILTER_conf)
    _basic_vars = [BASIC_login, BASIC_socket]  # getVarsByRe(FILTER_basic)

    for a in zip(_conf_vars, _basic_vars):
        cw = configparser.ConfigParser()
        print(a)
        d = dict(a[1])
        for i in d.keys():
            cw.add_section(i)
            for j in d[i].keys():
                cw.set(i, j, str(d[i][j]))
        cw.write(open(str(a[0]), "w"))
        print(f"write: {a[0]}")


class ConfigReader:
    def __init__(self, filename: str, basic_struct: dict):
        self._cf = configparser.ConfigParser()
        self._cf.read(filename)
        self._basic = basic_struct

    def read(self, section: str, option: str, op_type: str):
        option = option.lower()
        op_type = op_type.lower()
        if op_type not in ["int", "str", "float"]:
            raise TypeError("op_type must be 'int', 'str', 'float'.")
        # r = None
        if self._cf.has_option(section, option):
            r = self._cf.get(section, option)
        else:
            try:
                r = self._basic[section][option]
            except KeyError:
                raise KeyError(f"Cannot find option [{section} -> {option}].")
            warnings.warn(f"Cannot find option [{section} -> {option}] in file.\n"
                          f"Using the default value [{r}].")
        return r


def main():
    createDefaultFiles()
    cr = ConfigReader(CONF_login, BASIC_login)
    a = cr.read("login", "password", "str")
    print(a)


if __name__ == "__main__":
    main()
