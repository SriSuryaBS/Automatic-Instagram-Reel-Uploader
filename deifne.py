import requests
import json




def getCreds():

    creds = dict()
    creds['access_token'] = ''
    creds['client_id'] = ''
    creds['client_secret'] = ''
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v16.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = ''
    creds['page_id'] = ''
    creds['instagram_account_id'] = ''
    return creds


def makeAPIcalls(url,endpointParams,debug = 'no'):

    '''if type == 'POST':
        data = requests.post(url, endpointParams)
    else:'''
    data = requests.get(url,endpointParams)

    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent = 4)
    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)

    '''if( "yes" == debug):
        displayApicalldata(response)'''

    return response

def displayApicalldata(response):
    print("Url:")
    print(response['url'])
    print('Endpoint Params')
    print(response['endpoint_params_pretty'])
    print('Response')
    print(response['json_data_pretty'])