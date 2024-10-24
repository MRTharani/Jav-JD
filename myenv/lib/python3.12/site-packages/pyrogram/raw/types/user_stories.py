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


class UserStories(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.UserStories`.

    Details:
        - Layer: ``161``
        - ID: ``8611A200``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        stories (List of :obj:`StoryItem <pyrogram.raw.base.StoryItem>`):
            N/A

        max_read_id (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["user_id", "stories", "max_read_id"]

    ID = 0x8611a200
    QUALNAME = "types.UserStories"

    def __init__(self, *, user_id: int, stories: List["raw.base.StoryItem"], max_read_id: Optional[int] = None) -> None:
        self.user_id = user_id  # long
        self.stories = stories  # Vector<StoryItem>
        self.max_read_id = max_read_id  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserStories":
        
        flags = Int.read(b)
        
        user_id = Long.read(b)
        
        max_read_id = Int.read(b) if flags & (1 << 0) else None
        stories = TLObject.read(b)
        
        return UserStories(user_id=user_id, stories=stories, max_read_id=max_read_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.max_read_id is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        if self.max_read_id is not None:
            b.write(Int(self.max_read_id))
        
        b.write(Vector(self.stories))
        
        return b.getvalue()
