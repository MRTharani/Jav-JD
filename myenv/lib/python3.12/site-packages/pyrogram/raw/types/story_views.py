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


class StoryViews(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StoryViews`.

    Details:
        - Layer: ``161``
        - ID: ``C64C0B97``

    Parameters:
        views_count (``int`` ``32-bit``):
            N/A

        reactions_count (``int`` ``32-bit``):
            N/A

        recent_viewers (List of ``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["views_count", "reactions_count", "recent_viewers"]

    ID = 0xc64c0b97
    QUALNAME = "types.StoryViews"

    def __init__(self, *, views_count: int, reactions_count: int, recent_viewers: Optional[List[int]] = None) -> None:
        self.views_count = views_count  # int
        self.reactions_count = reactions_count  # int
        self.recent_viewers = recent_viewers  # flags.0?Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViews":
        
        flags = Int.read(b)
        
        views_count = Int.read(b)
        
        reactions_count = Int.read(b)
        
        recent_viewers = TLObject.read(b, Long) if flags & (1 << 0) else []
        
        return StoryViews(views_count=views_count, reactions_count=reactions_count, recent_viewers=recent_viewers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.recent_viewers else 0
        b.write(Int(flags))
        
        b.write(Int(self.views_count))
        
        b.write(Int(self.reactions_count))
        
        if self.recent_viewers is not None:
            b.write(Vector(self.recent_viewers, Long))
        
        return b.getvalue()
