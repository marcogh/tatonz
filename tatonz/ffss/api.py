# myapp/api.py
from tastypie import fields
from tastypie.resources import Resource
from tastypie.authorization import Authorization


class ViaggiaTreno(object):
    """
    Train to shove data from.
    """
    def __init__(self, initial=None):
        from lxml.html import parse
        url = 'http://mobile.viaggiatreno.it/vt_pax_internet/mobile/numero?numeroTreno=9704&tipoRicerca=numero&lang=EN'
        page = parse(url)

        self.__dict__['_train'] = {} 

        # nome 
        self.__dict__['_train']['name'] = page.xpath('//h1/text()')

        # partenza, arrivo 
        a = page.xpath('//h2/text()')
        self.__dict__['_train']['departure'] = a[0]
        self.__dict__['_train']['arrival'] = a[-1]

    def __getattr__(self, name):
        return self._data.get(name, None)

    def to_dict(self):
        return self._data


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
