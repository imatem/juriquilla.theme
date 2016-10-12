# -*- coding: utf-8 -*-
from Products.CMFPlone.utils import getToolByName
from Products.Five import BrowserView
from zope.component.hooks import getSite
from Products.Collage.browser.views import BaseTopicView
from Products.Collage.browser.views import BaseView

from DateTime import DateTime
from DateTime.interfaces import DateTimeError
from plone.app.portlets.portlets.rss import RSSFeed


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

    def officePhone(self, obj):
        return getattr(obj, 'officePhone', None)

    def specialtiesUser(self, obj):
        specialties = []
        catalog = getToolByName(getSite(), 'portal_catalog')

        person_specialties = catalog(UID=obj.getRawSpecialties())
        for sp in person_specialties:
            specialty_brain = sp
            specialties.append({'url': specialty_brain.getURL(), 'value': specialty_brain.Title})

        return specialties


class IMSiteTopicView(BaseTopicView):

    def cstyle(self, ptitle):
        if 'Juriquilla' == ptitle:
            return 'jurheader-color'
        return 'cuheader-color'

    def topicstyle(self, ptitle):
        if 'Juriquilla' == ptitle:
            return 'jurborder-color'
        return 'cuborder-color'


class RSSTopicsView(BaseView):
    title = u'RSSlink_topics'

    def __init__(self, context, request):
        self.context = context
        self.request = request
        # self.feed = IMRSSFeed('http://paginas.matem.unam.mx/oaxaca/RSS/index.xml', 100)
        self.feed = IMRSSFeed(self.context.remote_url(), 100)
        self.feed.update()

    @property
    def feedAvailable(self):
        """checks if the feed data is available"""
        return self.feed

    def hasFeed(self):
        if self.items():
            return True
        return False

    def items(self):

        ritems = []
        date = DateTime()
        for item in self.feed.items:
            if item.get('updated', ''):
                if item['updated'] < date:
                    continue
                if item['updated'] >= date and item['updated'] <= date + 14:
                    ritems.append(item)
                elif item['updated']._hour + 1 >= date._hour and item['updated'] <= date + 14:
                    ritems.append(item)
        return ritems

    def getFancyDate(self, date):
        month_name = {
            'Jan.': 'Enero',
            'Feb.': 'Febrero',
            'Mar.': 'Marzo',
            'Apr.': 'Abril',
            'May': 'Mayo',
            'June': 'Junio',
            'July': 'Julio',
            'Aug.': 'Agosto',
            'Sep.': 'Septiembre',
            'Oct.': 'Octubre',
            'Nov.': 'Noviembre',
            'Dec.': 'Diciembre'
        }

        datetime = date and date.pCommon() or ''
        if datetime:
            date_s = datetime.split(' ')
            return date_s[1].replace(',', '') + ' de ' + month_name[date_s[0]] + ', ' + date_s[3] + ' ' + date_s[4] + '.' or ''

        return datetime

    def cstyle(self):
        if 'oaxaca' in self.context.remote_url():
            return 'oaxheader-color'

        return 'cuerheader-color'

    def topicstyle(self):
        if 'oaxaca' in self.context.remote_url():
            return 'oaxborder-color'
        return 'cuerborder-color'


class IMRSSFeed(RSSFeed):
    """an RSS feed"""

    def _buildItemDict(self, item):
        link = item.links[0]['href']
        itemdict = {
            'title': item.title,
            'url': link,
            'summary': item.get('description', ''),
            'speaker': item.get('dc_speaker', ''),
            'institution': item.get('dc_institution', ''),
            'seminarytitle': item.get('dc_seminarytitle', ''),
            'location': item.get('dc_location', ''),
        }
        if hasattr(item, "updated"):
            try:
                itemdict['updated'] = DateTime(item.updated)
            except DateTimeError:
                # It's okay to drop it because in the
                # template, this is checked with
                # ``exists:``
                pass

        return itemdict
