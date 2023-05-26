from deifne import getCreds,makeAPIcalls
from getpages import pageID

def getInstagramAccount(params,accesstoken):
    endpointParams = dict()
    endpointParams['access_token'] = accesstoken
    endpointParams['fields'] = 'instagram_business_account'

    url = params['endpoint_base'] + pageID(accesstoken)

    return makeAPIcalls(url, endpointParams, debug='yes')

def instabID(accesstoken):

    params = getCreds()
    params['debug'] = 'yes'
    response = getInstagramAccount(params,accesstoken)
    aid = response['json_data']['instagram_business_account']['id']
    '''print("Account ID = ")
    print(aid)'''
    return aid