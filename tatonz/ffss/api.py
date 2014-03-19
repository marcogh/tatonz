# myapp/api.py
from tastypie import fields
from tastypie.resources import Resource
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle



class Scraper(object):
    """
    Train to shove data from.
    train numbers: 9704, 9708
    """
    def __init__(self, pk=None):
        from lxml.html import parse
        self._train = {} 
        self.__dict__['_train']['pk'] = pk 
        url = self.createurl()
        page = parse(url)


        # nome 
        self.__dict__['_train']['name'] = page.xpath('//h1/text()')[0]

        # partenza, arrivo 
        a = page.xpath('//h2/text()')
        #self.__dict__['_train']['departure'] = a[0]
        #self.__dict__['_train']['arrival'] = a[-1]

    def createurl(self):
        return 'http://mobile.viaggiatreno.it/vt_pax_internet/mobile/numero?numeroTreno=%s&tipoRicerca=numero&lang=EN' % self.pk

    def __getattr__(self, key):
        v = self.__dict__['_train'][key]
        if type(v) == type({}):
            return Scraper(v)
        return v

class TrainResource(Resource):
    name = fields.CharField(attribute='name')
    #departure = fields.CharField(attribute='departure')
    #arrival = fields.CharField(attribute='arrival') 

    #departure_time =
    #arrival_time = 
    #delay = 
    
    class Meta:
        resource_name = 'train'
        object_class = Scraper
        authorization = Authorization()

    def detail_uril_kwargs(self,bundle_or_obj):
        kwargs={}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.name
        else:
            kwargs['pk'] = bundle_or_obj.name

        return kwargs

    def get_object_list(self, request):
        results = []
        for train in [ '9704','9708' ]:
            new = Scraper(pk=train)
            results.append(new)
        return results

    def obj_get_list(self, bundle, **kwargs):
        # filtering disabled for brevity
        return self.get_object_list(bundle.request)

    def obj_get(self, bundle, **kwargs):
        pass
