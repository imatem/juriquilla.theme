# -*- coding: utf-8 -*-
from Products.Five import BrowserView


class UsersView(BrowserView):
    """Solgema Fullcalendar Browser view for Fullcalendar rendering"""

    # implements(interfaces.ISolgemaFullcalendarView)

    # def __init__(self, context, request):
    #     self.context = context
    #     self.request = request

    def getFoo(self):
        return ''

    def test(self, condition, r1, r2):
        if condition:
            return r1
        return r2
