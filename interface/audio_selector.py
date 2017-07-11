# AUDIO NAMING CONVENTION
# "sector_ageGroup.mp3"
# where sector:
# - "norte"
# - "centro"
# - "sur"
# and ageGroup:
# - "joven"
# - "medio"
# - "mayor"

def return_audio_name(region, age):
	return sector(region) + "_" + ageGroup(age) + ".mp3"

def ageGroup(age):
	if age < 28:
		return "joven"
	elif 28 <= age < 55:
		return "medio"
	elif 55 <= age:
		return "mayor"
	else: return "error"

def sector(region):
	norte = ["XV Arica y Paricanota", "I Tarapacá", "II Antofagasta", "III Atacama", "IV Coquimbo"]
	centro = ["Región Metropolitana", "V Valparaíso", "VI O'Higgins", "VII Maule"]
	sur = ["VIII Biobío", "IX La Araucanía", "XIV Los Ríos", "X Los Lagos", "XI Aysén", "XII Magallanes y Antártica"]

	if region in norte: return "norte"
	elif region in centro: return "centro"
	elif region in sur: return "sur"
	else: return "error"

