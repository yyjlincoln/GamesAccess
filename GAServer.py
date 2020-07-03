from flask import Flask, request, jsonify

app = Flask(__name__)

acceptver = '0.1'
acceptedhash = 'nnLQMw8j6CThacNwtYrJgA=='

UUID_MAP = {
    'yijun.yan':'CodeEx1'
}

EXECODE = {
    'CodeEx1':'''
import getpass
import os
if getpass.getpass('Password:')=='lincoln':
    os.system('subst a: c:\\\\')
print('Finished.')
'''
}

BLOCKLIST = {
    # 'yijun.yan':'PERMISSION DENIED'
}

# @app.route('/cs')
@app.route('/ga/cs')
def codeservice():
    token = request.values.get('token')
    uuid = request.values.get('uuid')
    clientver = request.values.get('clientver')
    if clientver != acceptver:
        return jsonify({
            'code':'VER_VERIFICATION_FAILED',
            'errmsg':'This version of the script is not supported.'
        })
    if token != acceptedhash:
        print(token)
        return jsonify({
            'code':'TOKEN_VERIFICATION_FAILED',
            'errmsg':'Modification detected. Please download a new copy of the software.'
        })

    if uuid in BLOCKLIST:
        return jsonify({
            'code':'PERMISSON_DENIED',
            'errmsg':BLOCKLIST[uuid]
        })

    if uuid in UUID_MAP:
        if UUID_MAP[uuid] not in EXECODE:
            return jsonify({
                'code':'SCRIPT_NOT_FOUND',
                'errmsg':'Script is not found on the server side. Try again later.'
            })
        return jsonify({
            'code':0,
            'execode': EXECODE[UUID_MAP[uuid]]
        })

    return jsonify({
        'code':'dev_success',
        'errmsg':'Token='+token+' uuid='+uuid
    })

app.run(port=80)