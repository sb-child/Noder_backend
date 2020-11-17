# coding=utf-8
import random
import uuid
import string
import time
# import numba
import numpy
from typing import Union, List
import json


def getRandomUuid():
    return uuid.uuid4().__str__()


def getRandomStr(n: int):
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


def getTime():
    t = str(time.time()).split(".")
    return t[0] + "." + t[1][:6]


# @profile
def toStr(i: Union[str, bytes]):
    # if isinstance(i, str):
    #     return i
    if isinstance(i, bytes):
        return i.decode("utf-8")
    elif isinstance(i, str):
        return i
    else:
        return ""


def dirSpilt(d: str):
    r = d.split("/")
    for i in range(len(r)):
        r[i] = r[i].strip()
    while "" in r:
        r.remove("")
    return r


def toDir(ls: list):
    return "/".join(ls)


def dirCheck(d: str, dirs: dict):
    d1 = toDir(dirSpilt(d))
    if len(d1) == 0:
        return []
    d2 = {}
    for i in dirs.keys():
        d2[i] = toDir(dirSpilt(dirs[i]))
    d3 = []
    for i in d2.keys():
        a = d1.split(d2[i], maxsplit=2)
        if not (len(a) == 1 or a[0] != ""):
            d3.append([i, dirSpilt(a[1])])
    if len(d3) == 0:
        return []
    d4 = []
    for i in range(len(d3)):
        d4.append([i, len((d3[i][1]))])
    n1 = numpy.array(d4)
    mn = int(numpy.argmin(n1[..., 1]))
    return d3[mn]


def jsonFromStr(t: str):
    return dict(json.loads(t))


def jsonFromDict(t: dict):
    return json.dumps(t)


def checkDict(p: list, target: dict):
    for i in p:
        if i not in target:
            return False
    return True


def main():
    print(getRandomUuid())
    print(getRandomStr(32))
    for i in range(10):
        print(getTime())
    print(dirSpilt("/"))
    print(dirSpilt("/123"))
    print(dirSpilt("222"))
    print(dirSpilt("/555/555/55"))
    print(dirCheck("/5556/5/666/65/5/755", {"a": "/5556", "b": "/5556/5", "c": "/556/5", "d": "/5556/5/666"}))


if __name__ == '__main__':
    main()
