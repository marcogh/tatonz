# myapp/api.py
from tastypie.resources import Resource


# Train object to shove data in/get data from.
class RiakObject(object):
"""
url = 'http://mobile.viaggiatreno.it/vt_pax_internet/mobile/numero?numeroTreno=9704&tipoRicerca=numero&lang=EN'
page = parse(url)

# nome 
page.xpath('//h1/text()')

# partenza, prossima fermata, arrivo 
page.xpath('//h2/text()')
"""
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}

        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def to_dict(self):
        return self._data


class Train(Resource):
    name = fields.CharField(attribute='name')
    departure =
    arrival = 

    departure_time =
    arrival_time = 
    delay = 

    def detail_uri_kwargs(self, bundle_or_obj):
        pass

    def get_object_list(self, request):
        pass

    def obj_get_list(self, bundle, **kwargs):
        pass

    def obj_get(self, bundle, **kwargs):
        pass
