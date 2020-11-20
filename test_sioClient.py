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

import socketio
import asyncio

sio = socketio.Client()


def connect():
    print('connection established')


def my_message(data):
    print('message received with ', data)
    sio.sleep(0.5)
    sio.send({})


def disconnect():
    print('disconnected from server')


if __name__ == '__main__':
    sio.on("connect", connect)
    sio.on("message", my_message)
    sio.on("disconnect", disconnect)
    sio.connect('http://0.0.0.0:37321')
