from plone.app.theming.utils import isThemeEnabled
from zope.interface import alsoProvides
from zope.interface import Interface


class IJuriquillaMarkerLayer(Interface):
    """Layer Marker Interface applied if Diazo is active
    """

def apply_juriquilla_layer(obj, event):
    if IJuriquillaMarkerLayer.providedBy(event.request) or not isThemeEnabled(event.request):
        return
    alsoProvides(event.request, IJuriquillaMarkerLayer)
