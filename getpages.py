from deifne import getCreds,makeAPIcalls

def getUserID(params,accesstoken):
    endpointParams = dict()
    endpointParams['access_token'] = accesstoken

    url = params['endpoint_base'] + 'me/accounts'


    return makeAPIcalls(url,endpointParams,params['debug'])

def pageID(accesstoken):
    params = getCreds()
    params['debug'] = 'yes'

    response = getUserID(params,accesstoken)

    id = response['json_data']['data'][0]['id']
    '''print(id)'''

    return id