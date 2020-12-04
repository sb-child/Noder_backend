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

from typing import Union
import redis
import asyncio
import socketio
import nd_utils
import re
import nd_msg
import aiohttp.web


class SrvSocket:
    def __init__(self, redis_host: str, host: Union[list, tuple]):
        # connect to redis
        # self.redis_cli = redis.StrictRedis(host=redis_host[0], port=redis_host[1])
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
        self.skt.on("connect", self._conn)
        self.skt.on("disconnect", self._disConn)
        self.skt.on("message", self._message)
        """
        todo :
        
        """

    async def _conn(self, sid, p):
        print("connect:")
        print(sid)
        print(p)
        print("")
        await self.skt.send("hello", sid)
        pass

    async def _disConn(self, sid):
        print("disconnect:")
        print(sid)
        print("")
        pass

    async def _message(self, sid, p: Union[str, bytes, list, dict]):
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
    s = SrvSocket(f'redis://127.0.0.1:6379/1', ("0.0.0.0", 37321))
    s.run()


if __name__ == '__main__':
    main()
