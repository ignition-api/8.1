from typing import List

from com.inductiveautomation.ignition.common.user import User
from com.palantir.ptoss.cinch.core import DefaultBindableModel
from dev.thecesrom.helper.types import AnyStr


class RosterModel(DefaultBindableModel):
    def getName(self):
        # type: () -> AnyStr
        pass

    def getUsers(self):
        # type: () -> List[AnyStr]
        pass

    def set(self, that):
        # type: (RosterModel) -> None
        pass

    def setName(self, name):
        # type: (AnyStr) -> None
        pass

    def setUsers(self, users):
        # type: (List[User]) -> None
        pass
