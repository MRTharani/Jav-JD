#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class AllStories(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.stories.AllStories`.

    Details:
        - Layer: ``161``
        - ID: ``519D899E``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        state (``str``):
            N/A

        user_stories (List of :obj:`UserStories <pyrogram.raw.base.UserStories>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        stealth_mode (:obj:`StoriesStealthMode <pyrogram.raw.base.StoriesStealthMode>`):
            N/A

        has_more (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetAllStories
    """

    __slots__: List[str] = ["count", "state", "user_stories", "users", "stealth_mode", "has_more"]

    ID = 0x519d899e
    QUALNAME = "types.stories.AllStories"

    def __init__(self, *, count: int, state: str, user_stories: List["raw.base.UserStories"], users: List["raw.base.User"], stealth_mode: "raw.base.StoriesStealthMode", has_more: Optional[bool] = None) -> None:
        self.count = count  # int
        self.state = state  # string
        self.user_stories = user_stories  # Vector<UserStories>
        self.users = users  # Vector<User>
        self.stealth_mode = stealth_mode  # StoriesStealthMode
        self.has_more = has_more  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AllStories":
        
        flags = Int.read(b)
        
        has_more = True if flags & (1 << 0) else False
        count = Int.read(b)
        
        state = String.read(b)
        
        user_stories = TLObject.read(b)
        
        users = TLObject.read(b)
        
        stealth_mode = TLObject.read(b)
        
        return AllStories(count=count, state=state, user_stories=user_stories, users=users, stealth_mode=stealth_mode, has_more=has_more)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.has_more else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(String(self.state))
        
        b.write(Vector(self.user_stories))
        
        b.write(Vector(self.users))
        
        b.write(self.stealth_mode.write())
        
        return b.getvalue()
