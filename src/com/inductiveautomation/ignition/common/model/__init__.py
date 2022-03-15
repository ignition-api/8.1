__all__ = ["Version"]

import re

from java.lang import Object


class Version(Object):
    dev = True
    snapshot = False

    def __init__(self, major=0, minor=0, rev=0, build=0, beta=0, rc=0):
        self.major = major
        self.minor = minor
        self.rev = rev
        self.build = build
        self.beta = beta
        self.rc = rc

    def __eq__(self, other, strict=False):
        ret = 0
        version_1 = [self.major, self.minor, self.rev]
        version_2 = [other.major, other.minor, other.rev]

        if strict:
            version_1.extend((self.build, self.beta, self.rc))
            version_2.extend((other.build, other.beta, other.rc))
        for i in range(max(len(version_1), len(version_2))):
            v_1 = version_1[i] if i < len(version_1) else 0
            v_2 = version_2[i] if i < len(version_2) else 0
            if v_1 > v_2:
                ret = 1
            elif v_1 < v_2:
                ret = -1
        return ret

    def __str__(self):
        return self.toString()

    def compareTo(self, that):
        return self.__eq__(that, True)

    def exists(self):
        pass

    @staticmethod
    def fromXML(inputStream):
        pass

    def getBasicString(self):
        return (
            f"{self.major}.{self.minor}.{self.rev}-rc{self.rc}"
            if self.rc > 0
            else f"{self.major}.{self.minor}.{self.rev}"
        )

    def getBeta(self):
        return self.beta

    def getBuildNumber(self):
        return self.build

    def getMajor(self):
        return self.major

    def getMinor(self):
        return self.minor

    def getRc(self):
        return self.rc

    def getRevision(self):
        return self.rev

    def getXML(self):
        pass

    def isDev(self):
        return self.dev

    def isFutureVersion(self, arg):
        other = self.parse(arg)
        return self.__eq__(other) == -1

    def isSnapshot(self):
        return self.snapshot

    @staticmethod
    def parse(s):
        sem_ver = [int(i) for i in re.findall(r"-?\d+", s)]
        return Version(sem_ver[0], sem_ver[1], sem_ver[2])

    def toParseableString(self):
        return f"{self.major}.{self.minor}.{self.rev}.{self.build}"

    def toString(self):
        if self.rc > 0:
            return f"{self.major}.{self.minor}.{self.rev}-rc{self.rc} (b{self.build})"
        elif self.isSnapshot():
            return f"{self.major}.{self.minor}.{self.rev}-SNAPSHOT (b{self.build})"
        elif self.build is not None:
            return f"{self.major}.{self.minor}.{self.rev} (b{self.build})"
        else:
            return f"{self.major}.{self.minor}.{self.rev}"
