from deifne import getCreds,makeAPIcalls

def longLivedAccessToken(params,client_id,client_secret,acc):
    endpointParams = dict()
    endpointParams['grant_type'] = 'fb_exchange_token'
    endpointParams['client_id'] = client_id
    endpointParams['client_secret'] = client_secret
    endpointParams['fb_exchange_token'] = acc

    url = params['endpoint_base'] + 'oauth/access_token'

    return makeAPIcalls(url,endpointParams,params['debug'])

def get_long_lived_access_token(client_id,client_secret,at):
    params = getCreds()
    params['debug'] = 'yes'

    response = longLivedAccessToken(params,client_id,client_secret,at)
    print(response)

    '''print("------\AccessTokenInfo\---------")
    print("AccessToken= ")'''
    actoken = response['json_data']['access_token']
    '''print(actoken)'''
    return actoken
