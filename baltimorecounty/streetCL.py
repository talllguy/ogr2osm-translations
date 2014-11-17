'''
Baltimore County Translate
'''

def filterTags(attrs):
    if not attrs:
        return
    tags = {}

    # Changing tag caps
    if 'STLABEL' in attrs:
        tags['name'] = attrs['STLABEL'.title()]
    if 'FTR_SUB' in attrs:
        tags['highway'] = attrs['FTR_SUB']
    if 'TRAFFIC_FL' in attrs:
        tags['oneway'] = attrs['TRAFFIC_FL']

    return tags