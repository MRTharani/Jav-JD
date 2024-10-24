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


class Report(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``161``
        - ID: ``C95BE06A``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        id (List of ``int`` ``32-bit``):
            N/A

        reason (:obj:`ReportReason <pyrogram.raw.base.ReportReason>`):
            N/A

        message (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["user_id", "id", "reason", "message"]

    ID = 0xc95be06a
    QUALNAME = "functions.stories.Report"

    def __init__(self, *, user_id: "raw.base.InputUser", id: List[int], reason: "raw.base.ReportReason", message: str) -> None:
        self.user_id = user_id  # InputUser
        self.id = id  # Vector<int>
        self.reason = reason  # ReportReason
        self.message = message  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Report":
        # No flags
        
        user_id = TLObject.read(b)
        
        id = TLObject.read(b, Int)
        
        reason = TLObject.read(b)
        
        message = String.read(b)
        
        return Report(user_id=user_id, id=id, reason=reason, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(Vector(self.id, Int))
        
        b.write(self.reason.write())
        
        b.write(String(self.message))
        
        return b.getvalue()
