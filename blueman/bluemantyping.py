from typing import NewType, Protocol, Union
from gi.repository import GObject


class _HasGType(Protocol):
    __gtype__: GObject.GType


# Actually supported types are int, bool, str, float, and object but no subclasses, see
# https://github.com/GNOME/pygobject/blob/ac576400ecd554879c906791e6638d64bb8bcc2a/gi/pygi-type.c#L498
# (We shield the possibility to provide a str to avoid errors)
GSignals = dict[str, tuple[GObject.SignalFlags, None, tuple[Union[None, type, GObject.GType, _HasGType], ...]]]

ObjectPath = NewType("ObjectPath", str)
BtAddress = NewType("BtAddress", str)
