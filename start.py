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
import nd_server_socket
from config import configManager


def main():
    sktSettings = configManager.ConfigReader("config/" + configManager.CONF_socket, configManager.BASIC_socket)
    conn_redis = sktSettings.read("socketIo", "redis_url", "str")
    conn_host = sktSettings.read("socketIo", "host", "str")
    conn_port: int = sktSettings.read("socketIo", "port", "int")
    db_name = sktSettings.read("fileManager", "file_db_name", "str")
    db_host = sktSettings.read("fileManager", "file_db_host", "str")
    db_port: int = sktSettings.read("fileManager", "file_db_port", "int")
    print(f"server starts at {conn_host}:{conn_port}")
    print(f"redis server: {conn_redis}")
    skt = nd_server_socket.SrvSocket(redis_host=conn_redis,
                                     host=[conn_host, conn_port],
                                     file_db={"host": db_host,
                                              "port": db_port,
                                              "name": db_name})
    skt.run()
    pass


if __name__ == "__main__":
    main()
