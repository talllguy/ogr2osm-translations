'''
MD DNR County translate
'''

def filterTags(attrs):
	if not attrs:
		return
	tags = {}

	#tags to all
	tags.update({'boundary':'protected_area'})
	tags.update({'name':attrs['Name']})
	tags.update({'official_name':attrs['FIRST_EASE']})
	#type
	if 'FIRST_PROT' in attrs:
		if attrs['FIRST_PROT'] == "COP":
			tags.update({'leisure':'park')})
			tags.update({'protect_class':'5')})
			tags.update({'protection_title':'County Owned Park')})
		elif attrs['FIRST_PROT'] == "OS":
			tags.update({'landuse':'preservation')})
			tags.update({'protect_class':'27')})
			tags.update({'protection_title':'Open Space')})


	return tags
