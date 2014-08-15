'''
Baltimore County Translate
'''

def filterTags(attrs):
    if not attrs:
        return
    tags = {}

    # Changing tag caps
    if 'FEATURE_TYPE' in attrs:
        tags['building'] = attrs['FEATURE_TYPE']
    if 'ADDR_HOUSENUMBER' in attrs:
        tags['addr:housenumber'] = attrs['ADDR_HOUSENUMBER']
    if 'ADDR_STREET' in attrs:
        tags['addr:street'] = attrs['ADDR_STREET']
    if 'ADDR_STATE' in attrs:
        tags['addr:state'] = attrs['ADDR_STATE']
    if 'ADDR_CITY' in attrs:
        tags['addr:city'] = attrs['ADDR_CITY']
    if 'POSTCODE' in attrs:
        tags['addr:postcode'] = attrs['POSTCODE']
    if 'ADDR_POSTAL' in attrs:
        tags['addr:postcode'] = attrs['ADDR_POSTAL']

    return tags