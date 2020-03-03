import requests
import jwt

reqKeysDict = {
    'users': ['first_name', 'last_name', 'company_name', 'email']
}


def requirements(data, type):
    keys = data.keys()
    req_keys = reqKeysDict[type]
    err = False
    msg = ""
    for key in req_keys:
        if key not in keys:
            err = True
            msg = key + " is missing"

    return err, msg
