
class sheet_token():
	def __init__(self) -> None:
		char_name	= ""
		char_class	= ""
		char_job	= ""

		attributes = {
			'strength'		: 0,
			'dexterity'		: 0,
			'constitution'	: 0,
			'intelligence'	: 0,
			'wisdom'		: 0,
			'charisma'		: 0
		}
		modifiers = {
			'stre_mod'		: 0,
			'dext_mod'		: 0,
			'cons_mod'		: 0,
			'inte_mod'		: 0,
			'wisd_mod'		: 0,
			'char_mod'		: 0,
		}
		inventory	= []
		spells		= []
		skills		= []


char_sheet = {
	'name'		: "",
	'class'		: "",
	'job'		: "",
	
	'attributes': {
		'strength'		: 0,
		'dexterity'		: 0,
		'constitution'	: 0,
		'intelligence'	: 0,
		'wisdom'		: 0,
		'charisma'		: 0
	},
	'modifiers' : {
		'stre_mod'		: 0,
		'dext_mod'		: 0,
		'cons_mod'		: 0,
		'inte_mod'		: 0,
		'wisd_mod'		: 0,
		'char_mod'		: 0,
	},
	
	'inventory'	: [],
	'spells'	: [],
	'skills'	: [],
}