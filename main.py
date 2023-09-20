from random import randint as roll

spell = {
	"fire_ball": {
		'name'			: "fire_ball",
		'damage'		: "2d6",
		'type_damege'	: "fire",
	},
	"star_rain": {
		'name'			: "star_rain",
		'damage'		: "2d6",
		'type_damage'	: "light",
	}
}
iten = {
	"base_sword":{
		'name'			: "base_sword",
		'damage'		: "1d6", 
		'type_damage'	: "physic",
	}
}

class sheet_token():
	def __init__(self) -> None:
		self.char_name	= ""
		self.char_class	= ""
		self.char_job	= ""

		self.attributes = {
			'strength'		: 0,
			'dexterity'		: 0,
			'constitution'	: 0,
			'intelligence'	: 0,
			'wisdom'		: 0,
			'charisma'		: 0,
		}
		self.modifiers = {
			'stre_mod'		: 0,
			'dext_mod'		: 0,
			'cons_mod'		: 0,
			'inte_mod'		: 0,
			'wisd_mod'		: 0,
			'char_mod'		: 0,
		}
		self.inventory	= []
		self.spells		= []
		self.skills		= []

	def dice_roll(self, type:int, quanty):
		

		# here
		 
		for time in range(quanty):
			roll(1, type)

	def set_class(self, arg_class):
		match arg_class:
			case "mage":
				self.char_class = "Mage"
				self.spells.append(spell['star_rain'])
				self.spells.append(spell['fire_ball'])
				self.inventory.append(iten['base_sword'])




