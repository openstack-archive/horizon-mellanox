from django.views import generic
from openstack_dashboard.api.rest import utils as rest_utils
from openstack_dashboard.api.rest import urls
import requests
import httplib, urllib, urllib2

@urls.register
class NEOLoginService(generic.View):
    """API for Murano packages.
    """
    url_regex = r'mlnx/neo_login/$'

    @rest_utils.ajax()
    def get(self, request):
        #postdata = {"username" : "admin", "password" : "123456"}
        #headers = {'content-type': 'application/x-www-form-urlencoded'}
        #r = requests.post("http://10.224.15.50/neo/login", data=postdata)


       params = urllib.urlencode({'username' : "admin", "password" : "123456"})
       headers = {"Content-type": "application/x-www-form-urlencoded"}
       conn = httplib.HTTPConnection("10.224.15.50")
       conn.request("POST", "/neo/login", params, headers)
       response = conn.getresponse()
       data = response.read()
       conn.close()
       return {
            'status': response.status,
            'text' : data
       }
