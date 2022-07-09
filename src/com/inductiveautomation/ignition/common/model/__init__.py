__all__ = ["Version"]

import re

from typing import Any, Optional, Tuple, Union

from java.io import InputStream
from java.lang import IllegalArgumentException, Object, String


class Version(Object):
    build = 0  # type: int
    dev = True  # type: bool
    major = 0  # type: int
    minor = 0  # type: int
    rev = 0  # type: int
    beta = 0  # type: int
    rc = 0  # type: int
    snapshot = False  # type: bool

    def __init__(self, major=0, minor=0, rev=0, build=0, beta=0, rc=0):
        # type: (int, int, int, int, int, int) -> None
        self.major = major
        self.minor = minor
        self.rev = rev
        self.build = build
        self.beta = beta
        self.rc = rc

    def __eq__(self, other):
        # type: (Any) -> bool
        return self._compare(other, True) == 0

    def __str__(self):
        # type: () -> str
        return self.toString()

    def _compare(self, that, strict=False):
        this = self.toTuple(strict)
        that = that.toTuple(strict)
        return (this > that) - (this < that)

    def compareTo(self, that):
        # type: (Version) -> Optional[int]
        return self._compare(that, True) if isinstance(that, type(self)) else None

    def exists(self):
        # type: () -> bool
        pass

    @staticmethod
    def fromXML(inputStream):
        # type: (InputStream) -> Version
        pass

    def getBasicString(self):
        # type: () -> str
        return (
            "{}.{}.{}-rc{}".format(self.major, self.minor, self.rev, self.rc)
            if self.rc > 0
            else "{}.{}.{}".format(self.major, self.minor, self.rev)
        )

    def getBeta(self):
        # type: () -> int
        return self.beta

    def getBuildNumber(self):
        # type: () -> int
        return self.build

    def getMajor(self):
        # type: () -> int
        return self.major

    def getMinor(self):
        # type: () -> int
        return self.minor

    def getRc(self):
        # type: () -> int
        return self.rc

    def getRevision(self):
        # type: () -> int
        return self.rev

    def getXML(self):
        # type: () -> str
        pass

    def isDev(self):
        # type: () -> bool
        return self.dev

    def isFutureVersion(self, arg):
        # type: (Union[Version, String]) -> bool
        cls = type(self)
        if isinstance(arg, basestring):
            that = self.parse(arg)
        elif isinstance(arg, cls):
            that = arg
        else:
            raise TypeError("isFutureVersion(): 1st arg can't be coerced to String.")

        return self._compare(that) == -1

    def isSnapshot(self):
        # type: () -> bool
        return self.snapshot

    @staticmethod
    def parse(s):
        # type: (String) -> Version
        sem_ver = [int(i) for i in re.findall(r"-?\d+", s)]
        if len(sem_ver) < 3:
            raise IllegalArgumentException('Invalid version: "{}"'.format(s))
        build_number = sem_ver[3] if len(sem_ver) == 4 else 0
        return Version(sem_ver[0], sem_ver[1], sem_ver[2], build_number)

    def toParseableString(self):
        # type: () -> str
        return "{}.{}.{}.{}".format(self.major, self.minor, self.rev, self.build)

    def toString(self):
        # type: () -> str
        if self.rc > 0:
            return "{}.{}.{}-rc{} (b{})".format(
                self.major, self.minor, self.rev, self.rc, self.build
            )
        if self.isSnapshot():
            return "{}.{}.{}-SNAPSHOT (b{})".format(
                self.major, self.minor, self.rev, self.build
            )
        if self.build is not None:
            return "{}.{}.{} (b{})".format(self.major, self.minor, self.rev, self.build)

        return "{}.{}.{}".format(self.major, self.minor, self.rev)

    def toTuple(self, strict=False):
        # type: (bool) -> Tuple[int, ...]
        return (
            (self.major, self.minor, self.rev, self.build, self.beta, self.rc)
            if strict
            else (self.major, self.minor, self.rev)
        )
