'''
Baltimore County Translate
'''

def filterTags(attrs):
    if not attrs:
        return
    tags = {}

    # Changing tag caps
    if 'FEATURE_TY' in attrs:
        tags['building'] = attrs['FEATURE_TY']
    if 'BUILDING' in attrs:
        tags['building'] = attrs['BUILDING']
    if 'ADDR_HOUSE' in attrs:
        tags['addr:housenumber'] = attrs['ADDR_HOUSE']
    if 'ADDR_STREE' in attrs:
        tags['addr:street'] = attrs['ADDR_STREE']
    if 'ADDR_STATE' in attrs:
        tags['addr:state'] = attrs['ADDR_STATE']
    if 'ADDR_CITY' in attrs:
        tags['addr:city'] = attrs['ADDR_CITY']
    if 'POSTCODE' in attrs:
        tags['addr:postcode'] = attrs['POSTCODE']
    if 'ADDR_POSTA' in attrs:
        tags['addr:postcode'] = attrs['ADDR_POSTA']

    return tags