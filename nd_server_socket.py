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

from typing import Union, Dict
import socketio
import aiohttp.web
# import redis
# import asyncio
# import re
import nd_utils
import nd_msg
import nd_file_manager
import nd_task_pool


class SrvSocket:
    def __init__(self, redis_host: str, host: Union[list, tuple], file_db: Dict):
        # init socket.io
        # use default manager if redis_host is ""
        self.sio_mgr = socketio.AsyncRedisManager(redis_host) if redis_host != "" else None
        self.skt = socketio.AsyncServer(client_manager=self.sio_mgr,
                                        async_mode='aiohttp',
                                        ping_timeout=10,
                                        ping_interval=5)
        self.skt_AsgiApp = aiohttp.web.Application()
        self.skt.attach(self.skt_AsgiApp)
        # set hosts and id
        self.host = host
        self.r_host = redis_host
        self.id = nd_utils.getRandomStr(32)
        # command executer
        self.mExec = nd_msg.MsgExec(self.id)
        # socket.io events
        # greeter
        self.skt.on("connect", self._greeter_conn, namespace="/greeter")
        self.skt.on("disconnect", self._greeter_disConn, namespace="/greeter")
        self.skt.on("message", self._greeter_message, namespace="/greeter")
        # user
        self.skt.on("connect", self._user_conn, namespace="/user")
        self.skt.on("disconnect", self._user_disConn, namespace="/user")
        self.skt.on("message", self._user_message, namespace="/user")
        # worker
        self.skt.on("connect", self._worker_conn, namespace="/worker")
        self.skt.on("disconnect", self._worker_disConn, namespace="/worker")
        self.skt.on("message", self._worker_message, namespace="/worker")
        # fileManager
        self.fileDbSettings = file_db
        self.fMan = nd_file_manager.FileManager(db_host=file_db["host"],
                                                db_port=file_db["port"],
                                                db_name=file_db["name"])
        # taskPool
        self.taskPool = nd_task_pool.TaskPool()

    # -- todo: socket.io events
    # -- user
    async def _user_conn(self, sid, p):
        print("connect")
        await self.skt.send("hello", sid)
        pass

    async def _user_disConn(self, sid):
        print("disconnect")
        pass

    async def _user_message(self, sid, p: Union[str, bytes, list, dict]):
        pass

    # -- worker
    async def _worker_conn(self, sid, p):
        print("connect")
        await self.skt.send("hello", sid)
        pass

    async def _worker_disConn(self, sid):
        print("disconnect")
        pass

    async def _worker_message(self, sid, p: Union[str, bytes, list, dict]):
        pass

    # -- greeter
    async def _greeter_conn(self, sid, p):
        print("connect:")
        print(sid)
        print(p)
        print("")
        await self.skt.send("hello", sid)
        pass

    async def _greeter_disConn(self, sid):
        print("disconnect:")
        print(sid)
        print("")
        pass

    async def _greeter_message(self, sid, p: Union[str, bytes, list, dict]):
        print("message:")
        print(sid)
        print(p)
        print("")
        # non dict type is not allowed
        if not isinstance(p, dict):
            await self.skt.disconnect(sid)
            return
        self.skt.enter_room(sid, "users")
        self.mExec.executeCmd(p, sid)

    # -- end of socket.io events --
    def run(self):
        def my_print(_):
            pass

        print(f"socket.io is running at {self.host[0]}:{self.host[1]}")
        aiohttp.web.run_app(self.skt_AsgiApp,
                            host=self.host[0],
                            port=self.host[1],
                            print=my_print)

    def debug(self):
        pass


def main():
    # s = SrvSocket(f'redis://127.0.0.1:6379/1', ("0.0.0.0", 37321))
    # s.run()
    pass


if __name__ == '__main__':
    main()
