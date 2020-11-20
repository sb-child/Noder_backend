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
# import websockets
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
        self.sio_mgr = socketio.AsyncRedisManager(redis_host)
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

        # self._front = {
        #     "op": f"noder_op:{self.id}",
        #     "user": f"noder_user:{self.id}",
        #     "send": f"noder_send:{self.id}",
        # }
        # self._re_sc = {
        #     "user_id": re.compile(self._front["user"] + ":([0-9a-zA-z]{8})").findall,
        #     "send_id": re.compile(self._front["send"] + ":([0-9a-zA-z]{8})").findall,
        # }
        self.mExec = nd_msg.MsgExec(self.id)
        # socket.io events
        self.skt.on("connect", self._conn)
        self.skt.on("disconnect", self._disConn)
        self.skt.on("message", self._message)

    """
        def _put_op(self, op_str: str, timeout=10):
            self.redis_cli.set(f"{self._front['op']}:{nd_utils.getTime()}", op_str, timeout)
    
        def send(self, uid: str, send: str, timeout=10):
            self.redis_cli.set(f"{self._front['send']}:{uid}", send, timeout)
    
        # @profile
        def _add_user(self, username: str, timeout=10):
            n = self.find_user_by_name(username)
            if len(n) >= 1:
                self.redis_cli.expire(f"{self._front['user']}:{n[0]}", timeout)
                return
            while True:
                uid = nd_utils.getRandomStr(8)
                if len(self.find_user_by_id(uid)) == 0:
                    break
            self.redis_cli.set(f"{self._front['user']}:{uid}", username, ex=timeout)
            return [uid, username]
    
        def get_users(self):
            ids = []
            ks = []
            keys: list = self.redis_cli.keys(f"{self._front['user']}:*")
            for i in keys:
                i = nd_utils.toStr(i)
                res = self._re_sc["user_id"](i)
                if len(res) == 0:
                    continue
                if len(res) != 1:
                    self.redis_cli.delete(i)
                    continue
                ids.append(res[0])
                ks.append(i)
            r = []
            names = self.redis_cli.mget(ks)
            for i in range(len(ids)):
                r.append([ids[i], nd_utils.toStr(names[i])])
            return r
    
        def find_user_by_name(self, name: str):
            u = self.get_users()
            for i in u:
                if i[1] == name:
                    return i
            return []
    
        def find_user_by_id(self, uid: str):
            nm = self.redis_cli.get(f"{self._front['user']}:{uid}")
            nm = nd_utils.toStr(nm)
            if nm == "":
                return []
            return [uid, nm]
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
        self.mExec.executeCmd(p, sid)

        # print(path)
        # websocket.close_timeout = 1
        # websocket.ping_timeout = 1
        # while True:
        #     try:
        #         data = await websocket.recv()
        #     except websockets.ConnectionClosed:
        #         print("closed")
        #         break
        #     if isinstance(data, str):
        #         print(path, data)
        #         r = self.mConv.conv(path, data)
        #         if r is None:
        #             continue
        #         if r["cli_type"] == "greeter":
        #             if r["op"] == "get_user":
        #                 result = self._add_user(f"user_{nd_utils.getRandomStr(10)}")
        #                 await websocket.send(nd_utils.jsonFromDict(
        #                     {"code": "ok",
        #                      "data": result,
        #                      "s_id": self.id}))
        #     else:
        #         await websocket.close()
        #         break

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
        # for i in range(1000):
        #     self._add_user(f"a{i}")


def main():
    s = SrvSocket(f'redis://127.0.0.1:6379/1', ("0.0.0.0", 37321))
    # s.debug()
    # r = s.get_users()
    # print(r)
    # print(len(r))
    s.run()


if __name__ == '__main__':
    main()
