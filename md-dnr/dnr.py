def filterTags(attrs):
	if not attrs: return

	tags = {}
	tags.update({'name':attrs['NAME'].strip().replace("Ctr","Center")})
	tags.update({'website':attrs['WebLink'].strip()})
	#automagically convert names
	if attrs['Agency']:
		if attrs['Agency'] == "Dept of Justice":
			tags.update({'amenity':'prison'})
			tags.update({'operator':'United States Department of Justice'})
			tags.update({'protect_class':'27'})
		elif attrs['Agency'] == "Dept. of Energy":
			tags.update({'landuse':'commericial'})
			tags.update({'operator':'United States Department of Energy'})
			tags.update({'protect_class':'27'})
		elif attrs['Agency'] == "NASA":
			tags.update({'landuse':'military'})
			tags.update({'operator':'United States NASA'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protect_class':'25'})
			tags.update({'protection_title':'Military Area'})
		elif attrs['Agency'] == "SERC":
			tags.update({'leisure':'nature_reserve'})
			tags.update({'operator':'Smithsonian Institution'})
			tags.update({'wikipedia':'en:Smithsonian_Environmental_Research_Center'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protect_class':'1'})
			tags.update({'protection_title':'Environmental Research Area'})
		elif attrs['Agency'] == "U.S. MILITARY":
			tags.update({'landuse':'military'})
			tags.update({'operator':'United States Department of Defense'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protect_class':'25'})
			tags.update({'protection_title':'Military Area'})
		elif attrs['Agency'] == "U.S. PARK SERV.":
			tags.update({'operator':'United States Park Service'})
			tags.update({'boundary':'national_park'})
			tags.update({'protect_class':'2'})
			tags.update({'protection_title':'National Park'})
		elif attrs['Agency'] == "U.S.A.":
			tags.update({'operator':'United States of America'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protect_class':'27'})
		elif attrs['Agency'] == "U.S.A.- Utility":
			tags.update({'operator':'United States of America'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protect_class':'27'})
		elif attrs['Agency'] == "U.S.D.A.":
			tags.update({'operator':'United States Department of Agriculture'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protect_class':'27'})
		elif attrs['Agency'] == "U.S.F.W.":
			tags.update({'operator':'United States Fish and Wildlife Service'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protect_class':'27'})
		elif attrs['Agency'] == "US DEPT OF AG":
			tags.update({'operator':'United States Department of Agriculture'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protect_class':'27'})
		elif attrs['Agency'] == "US Dept. Trans.":
			tags.update({'operator':'United States Department of Transportation'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protect_class':'27'})
		elif attrs['Agency'] == "US Fire Admin.":
			tags.update({'operator':'United States Fire Administration'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protect_class':'27'})

	return tags
