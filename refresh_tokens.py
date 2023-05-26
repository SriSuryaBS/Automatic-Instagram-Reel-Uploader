from deifne import getCreds,makeAPIcalls
import sqlite3
def longLivedAccessToken(params,client_id,client_secret,acc):
    endpointParams = dict()
    endpointParams['grant_type'] = 'fb_exchange_token'
    endpointParams['client_id'] = client_id
    endpointParams['client_secret'] = client_secret
    endpointParams['fb_exchange_token'] = acc

    url = params['endpoint_base'] + 'oauth/access_token'

    return makeAPIcalls(url,endpointParams,params['debug'])

def refresh_access_tokens(id):


    def get_client_id(id):
        conn = sqlite3.connect("Instadata.db")
        c = conn.cursor()
        clientids = [job[0] for job in c.execute("SELECT client_id FROM instagramdata WHERE rowid = (?) ", (id))]
        idc = ''
        for clientid in clientids:
            idc += clientid
        '''print(idc)'''

        return idc


    def get_client_secret(id):
        conn = sqlite3.connect("Instadata.db")
        c = conn.cursor()
        clientsecs = [job[0] for job in c.execute("SELECT client_secret FROM instagramdata WHERE rowid = (?) ", (id))]
        secret = ''
        for clientsec in clientsecs:
            secret += clientsec
        '''print(secret)'''

        return secret

    def get_ll_access_token(id):
        conn = sqlite3.connect("Instadata.db")
        c = conn.cursor()
        llaccs = [job[0] for job in c.execute("SELECT ll_accesstoken FROM instagramdata WHERE rowid = (?) ", (id))]
        llat = ''
        for llacc in llaccs:
            llat += llacc
        '''print(llat)'''

        return llat

    client_id = get_client_id(id)
    client_secret = get_client_secret(id)
    at = get_ll_access_token(id)
    params = getCreds()
    params['debug'] = 'yes'

    response = longLivedAccessToken(params, client_id, client_secret, at)
    actoken = response['json_data']['access_token']
    print(actoken)
    return actoken


conn = sqlite3.connect("Instadata.db")

c = conn.cursor()
c.execute("SELECT rowid FROM instagramdata ")
ids = c.fetchall()

for id in ids:
    rids= [job[0] for job in c.execute("SELECT rowid FROM instagramdata WHERE rowid = (?) ", (id))]
    row_id = ''
    for rid in rids:
        row_id += str(rid)
    '''print(row_id)'''

    new_ll_at = refresh_access_tokens(id)
    c.execute("UPDATE instagramdata SET ll_accesstoken = ? WHERE rowid = ?", (new_ll_at, row_id))
    conn.commit()

