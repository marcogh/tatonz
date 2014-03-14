# myapp/api.py
from tastypie import fields
from tastypie.resources import Resource
from tastypie.authorization import Authorization


class Scraper(object):
    """
    Train to shove data from.
    """
    def __init__(self, name=None):
        from lxml.html import parse
        self.name = name 
        url = self.createurl()
        page = parse(url)

        self._train = {} 

        # nome 
        self.name = page.xpath('//h1/text()')

        # partenza, arrivo 
        a = page.xpath('//h2/text()')
        self.departure = a[0]
        self.arrival = a[-1]

    def createurl(self):
        return 'http://mobile.viaggiatreno.it/vt_pax_internet/mobile/numero?numeroTreno=%s&tipoRicerca=numero&lang=EN' % self.name 

    def __getattr__(self, name):
        return self.get(name, None)

class Train(Resource):
    name = fields.CharField(attribute='name')
    departure = fields.CharField(attribute='departure')
    arrival = fields.CharField(attribute='arrival') 

    #departure_time =
    #arrival_time = 
    #delay = 

    class Meta:
        resource_name = 'train'
        object_class = ViaggiaTreno
        authorization = Authorization()
    

    def detail_uri_kwargs(self, bundle_or_obj):
        pass

    def get_object_list(self, request):
        pass

    def obj_get_list(self, bundle, **kwargs):
        pass

    def obj_get(self, bundle, **kwargs):
        pass
