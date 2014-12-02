def filterTags(attrs):
	if not attrs: return

	tags = {}
	
	#tags to all
	tags.update({'boundary':'protected_area'})
	tags.update({'name':attrs['Name'].strip(' ').title()})
	tags.update({'official_name':attrs['EASE_NUM_N'].strip(' ').title()})
	#type
	if attrs['PROT'] == "COP":
		tags.update({'leisure':'park')})
		tags.update({'protect_class':'5')})
		tags.update({'protection_title':'County Owned Park')})
	elif attrs['PROT'] == "OS":
		tags.update({'landuse':'preservation')})
		tags.update({'protect_class':'27')})
		tags.update({'protection_title':'Open Space')})
	return tags
