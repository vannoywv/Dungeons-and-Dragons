###Imports###
import random
###Standard Question Setup. Can present a multiple choice question up to 18 units in length. It returns the name from the list that is queried.###
def multich(list=[], ch1="error1", ch2="error2", ch3="error3", ch4="error4", ch5="error5", ch6="error6", ch7="error7", ch8="error8", ch9="error9", ch10="error10", ch11="error11", ch12="error12", ch13="error13", ch14="error14", ch15="error15", ch16="error16", ch17="error17", ch18="error18"):
	if len(list) > 0:
		ch1=list[0]
	else:
		None
	if len(list) > 0:
		ch1=list[0]
	else:
		None
	if len(list) > 1:
		ch2=list[1]
	else:
		None
	if len(list) > 2:
		ch3=list[2]
	else:
		None
	if len(list) > 3:
		ch4=list[3]
	else:
		None
	if len(list) > 4:
		ch5=list[4]
	else:
		None
	if len(list) > 5:
		ch6=list[5]
	else:
		None
	if len(list) > 6:
		ch7=list[6]
	else:
		None
	if len(list) > 7:
		ch8=list[7]
	else:
		None
	if len(list) > 8:
		ch9=list[8]
	else:
		None
	if len(list) > 9:
		ch10=list[9]
	else:
		None
	if len(list) > 10:
		ch11=list[10]
	else:
		None
	if len(list) > 11:
		ch12=list11[11]
	else:
		None
	if len(list) > 12:
		ch13=list[12]
	else:
		None
	if len(list) > 13:
		ch14=list[13]
	else:
		None
	if len(list) > 14:
		ch15=list[14]
	else:
		None
	if len(list) > 15:
		ch16=list[15]
	else:
		None
	if len(list) > 16:
		ch17=list[16]
	else:
		None
	if len(list) > 17:
		ch18=list[17]
	else:
		None
	if ch1 !="error1":
		print(f"A.{ch1}")
	else:
		None
	if ch2 !="error2":
		print(f"B.{ch2}")
	else:
		None
	if ch3 !="error3":
		print(f"C.{ch3}")
	else:
		None
	if ch4 !="error4":
		print(f"D.{ch4}")
	else:
		None
	if ch5 !="error5":
		print(f"E.{ch5}")
	else:
		None
	if ch6 !="error6":
		print(f"F.{ch6}")
	else:
		None
	if ch7 !="error7":
		print(f"G.{ch7}")
	else:
		None
	if ch8 !="error8":
		print(f"H.{ch8}")
	else:
		None
	if ch9 !="error9":
		print(f"I.{ch9}")
	else:
		None
	if ch10 !="error10":
		print(f"J.{ch10}")
	else:
		None
	if ch11 !="error11":
		print(f"K.{ch11}")
	else:
		None
	if ch12 !="error12":
		print(f"L.{ch12}")
	else:
		None
	if ch13 !="error13":
		print(f"M.{ch13}")
	else:
		None
	if ch14 !="error14":
		print(f"N.{ch14}")
	else:
		None
	if ch15 !="error15":
		print(f"O.{ch15}")
	else:
		None
	if ch16 !="error16":
		print(f"P.{ch16}")
	else:
		None
	if ch17 !="error17":
		print(f"Q.{ch17}")
	else:
		None
	if ch18 !="error18":
		print(f"R.{ch18}")
	else:
		None
	choice= input(f"""	Select Option:""")
	if choice=='A':
	    choice=list[0]
	else:
	    None
	if choice=='A':
	    choice=list[0]
	else:
	    None
	if choice=='B':
	    choice=list[1]
	else:
	    None
	if choice=='C':
	    choice=list[2]
	else:
	    None
	if choice=='D':
	    choice=list[3]
	else:
	    None
	if choice=='E':
	    choice=list[4]
	else:
	    None
	if choice=='F':
	    choice=list[5]
	else:
	    None
	if choice=='G':
	    choice=list[6]
	else:
	    None
	if choice=='H':
	    choice=list[7]
	else:
	    None
	if choice=='I':
	    choice=list[8]
	else:
	    None
	if choice=='J':
	    choice=list[9]
	else:
	    None
	if choice=='K':
	    choice=list[10]
	else:
	    None
	if choice=='L':
	    choice=list[11]
	else:
	    None
	if choice=='M':
	    choice=list[12]
	else:
	    None
	if choice=='N':
	    choice=list[13]
	else:
	    None
	if choice=='O':
	    choice=list[14]
	else:
	    None
	if choice=='P':
	    choice=list[15]
	else:
	    None
	if choice=='Q':
	    choice=list[16]
	else:
	    None
	if choice=='R':
	    choice=list[17]
	else:
	    None
	return choice
#Determines the stat modifier (IE: Con=15 ConMod=2).	
def modify(modstat):
	mod=round(((modstat-10)/2)-0.1)	
	return mod
###Questions for naming and selecting play class and race also defines starting stats for class. Give start items.###
#Makes the player type in the name and returns that name.
def givename():
	name= input(print("Type name."))
	return name
#Does basically everything for starting up the player. This is the only function you need to call to start the player. 
#Defines the starting items and proficiencies by class. Runs other necessary functions
def giveclass(self):
    play= multich(ch1='Barbarian', ch2='Bard', ch3='Cleric', ch4='Druid', ch5='Fighter', ch6='Monk', ch7='Paladin', ch8='Ranger', ch9='Rogue', ch10='Sorcerer', ch11='Warlock', ch12='Wizard')
    confirm=0
    while play== 'A' and confirm==0:
    	self.playclass= 'Barbarian'
    	self.items= []
    	martial= givemartial(self=self)
    	self.items.append(martial)
    	simple= givesimple(self=self)
    	self.items.append(simple)
    	self.items.append("Explorer's Pack")
    	self.items.append("Javelin")
    	self.spells= 'None'
    	self.spellslots= 'None'
    	self.equipment= self.items
    	self.proficiencies.append('Light Armor')
    	self.proficiencies.append('Medium Armor')
    	self.proficiencies.append('Shields')
    	self.proficiencies.append('Simple Weapons')
    	self.proficiencies.append('Martial Weapons')
    	self.proficiencies.append('Strength')
    	self.proficiencies.append('Constitution')
    	giveskills(self=self)
    	givestats(self=self)
    	givemaxhp(self=self)
    	giverace(self=self)
    	statblock(self)
    	print(f'Would you like to start with this character?')
    	confirm=multich(ch1='Yes', ch2='No')
    	if confirm== 'A':
    		print(f'You are starting.')
    		break
    	if confirm=='B':
    		giveclass(self)
    while play== 'B' and confirm==0:
    	self.playclass= 'Bard'
    	self.spells= [None]
    	self.spellslots= [None, 3,0,0,0,0,0,0,0,0]
    	self.proficiencies.append('Light Armor')
    	self.proficiencies.append('Simple Weapons')
    	self.proficiencies.append('Hand Crossbow')
    	self.proficiencies.append('Longsword')
    	self.proficiencies.append('Rapier')
    	self.proficiencies.append('Shortsword')
    	self.proficiencies.append('Instruments')
    	self.proficiencies.append('Dexterity')
    	self.proficiencies.append('Charisma')
    	startweapon=multich(ch1='Rapier', ch2='Longsword', ch3='Simple Weapon')
    	if startweapon=='A':
    		self.items.append('Rapier')
    	elif startweapon=='B':
    		self.items.append('Longsword')
    	elif startweapon=='C':
    		simple= givesimple(self=self)
    		self.items.append(simple)
    	else:
    		None
    	startpack= multich(ch1="Diplomat's Pack", ch2="Entertainer's Pack")
    	if startpack=='A':
    		self.items.append("Diplomat's Pack")
    	elif startpack=='B':
    		self.items.append("Entertainer's Pack")
    	else:
    		None
    	self.items.append('Instrument')
    	self.items.append('Leather Armor')
    	self.items.append('Dagger')
    	self.equipment=self.items
    	giveskills(self=self)
    	givestats(self=self)
    	givemaxhp(self=self)
    	giverace(self=self)
    	statblock(self)
    	print(f'Would you like to start with this character?')
    	confirm=multich(ch1='Yes', ch2='No')
    	if confirm== 'A':
    		break
    	if confirm=='B':
    		giveclass(self)
    	return self.playclass 
    while play== 'C' and confirm==0:
    	self.playclass= 'Cleric'
    	self.spells= []
    	self.spellslots= [None, 2,0,0,0,0,0,0,0,0]
    	self.proficiencies.append('Light Armor')
    	self.proficiencies.append('Medium Armor')
    	self.proficiencies.append('Shields')
    	self.proficiencies.append('Simple Weapons')
    	self.proficiencies.append('Wisdom')
    	self.proficiencies.append('Charisma')
    	self.items.append()
    	self.equipment= self.items
    	giveskills(self=self)
    	givestats(self=self)
    	givemaxhp(self=self)
    	giverace(self=self)
    	statblock(self)
    	print(f'Would you like to start with this character?')
    	confirm=multich(ch1='Yes', ch2='No')
    	if confirm== 'A':
    		break
    	if confirm=='B':
    		giveclass(self)
    	return self.playclass  
    while play== 'D' and confirm==0:
    	self.items= 'Sword' + ', ' + 'Shield' + ', ' + 'Chain Mail'
    	self.playclass= 'Druid'
    	self.spells= 'None'
    	self.spellslots= [None, 3,0,0,0,0,0,0,0,0]
    	self.equipment= self.items
    	giveskills(self=self)
    	givestats(self=self)
    	givemaxhp(self=self)
    	giverace(self=self)
    	statblock(self)
    	print(f'Would you like to start with this character?')
    	confirm=multich(ch1='Yes', ch2='No')
    	if confirm== 'A':
    		break
    	if confirm=='B':
    		giveclass(self)
    	return self.playclass  
    while play== 'E' and confirm==0:
    	self.items= 'Sword' + ', ' + 'Shield' + ', ' + 'Chain Mail'
    	self.playclass= 'Fighter'
    	self.spells= 'None'
    	self.spellslots= 'None'
    	self.equipment= self.items
    	giveskills(self=self)
    	givestats(self=self)
    	givemaxhp(self=self)
    	giverace(self=self)
    	statblock(self)
    	print(f'Would you like to start with this character?')
    	confirm=multich(ch1='Yes', ch2='No')
    	if confirm== 'A':
    		break
    	if confirm=='B':
    		giveclass(self)
    	return self.playclass  
    while play== 'F' and confirm==0:
    	self.items= 'Sword' + ', ' + 'Shield' + ', ' + 'Chain Mail'
    	self.playclass= 'Monk'
    	self.spells= 'None'
    	self.spellslots= 'None'
    	self.equipment= self.items
    	giveskills(self=self)
    	givestats(self=self)
    	givemaxhp(self=self)
    	giverace(self=self)
    	statblock(self)
    	print(f'Would you like to start with this character?')
    	confirm=multich(ch1='Yes', ch2='No')
    	if confirm== 'A':
    		break
    	if confirm=='B':
    		giveclass(self)
    	return self.playclass  
    while play== 'G' and confirm==0:
    	self.items= 'Sword' + ', ' + 'Shield' + ', ' + 'Chain Mail'
    	self.playclass= 'Paladin'
    	self.spells= 'None'
    	self.spellslots= [None, 3,0,0,0,0,0,0,0,0]
    	self.equipment= self.items
    	statblock(self)
    	print(f'Are you sure you want to be a {self.playclass}?')
    	confirm=multich(ch1='Yes', ch2='No')
    	if confirm== 'A':
    		break
    	if confirm=='B':
    		giveclass(self)
    	return self.playclass  
    while play== 'H' and confirm==0:
    	self.items= 'Sword' + ', ' + 'Shield' + ', ' + 'Chain Mail'
    	self.playclass= 'Ranger'
    	self.spells= ['None']
    	self.spellslots= [None, 3,0,0,0,0,0,0,0,0]
    	self.equipment= self.items
    	statblock(self)
    	giveskills(self=self)
    	givestats(self=self)
    	givemaxhp(self=self)
    	giverace(self=self)
    	statblock(self)
    	print(f'Would you like to start with this character?')
    	confirm=multich(ch1='Yes', ch2='No')
    	if confirm== 'A':
    		break
    	if confirm=='B':
    		giveclass(self)
    	return self.playclass  
    while play== 'I' and confirm==0:
    	self.items= 'Sword' + ', ' + 'Shield' + ', ' + 'Chain Mail'
    	self.playclass= 'Rogue'
    	self.spells= 'None'
    	self.spellslots= 'None'
    	self.equipment= self.items
    	giveskills(self=self)
    	givestats(self=self)
    	givemaxhp(self=self)
    	giverace(self=self)
    	statblock(self)
    	print(f'Would you like to start with this character?')
    	confirm=multich(ch1='Yes', ch2='No')
    	if confirm== 'A':
    		break
    	if confirm=='B':
    		giveclass(self)
    	return self.playclass  
    while play== 'J' and confirm==0:
    	self.items= 'Sword' + ', ' + 'Shield' + ', ' + 'Chain Mail'
    	self.playclass= 'Sorcerer'
    	self.spells= 'None'
    	self.spellslots= [None, 3,0,0,0,0,0,0,0,0]
    	self.equipment= self.items
    	statblock(self)
    	print(f'Are you sure you want to be a {self.playclass}?')
    	confirm=multich(ch1='Yes', ch2='No')
    	if confirm== 'A':
    		break
    	if confirm=='B':
    		giveclass(self)
    	return self.playclass  
    while play== 'K' and confirm==0:
    	self.items= 'Sword' + ', ' + 'Shield' + ', ' + 'Chain Mail'
    	self.playclass= 'Warlock'
    	self.spells= 'None'
    	self.spellslots= [None, 3,0,0,0,0,0,0,0,0]
    	self.equipment= self.items
    	giveskills(self=self)
    	givestats(self=self)
    	givemaxhp(self=self)
    	giverace(self=self)
    	statblock(self)
    	print(f'Would you like to start with this character?')
    	confirm=multich(ch1='Yes', ch2='No')
    	if confirm== 'A':
    		break
    	if confirm=='B':
    		giveclass(self)
    	return self.playclass  
    while play== 'L' and confirm==0:
    	self.items= 'Sword' + ', ' + 'Shield' + ', ' + 'Chain Mail'
    	self.playclass= 'Wizard'
    	self.spells= 'None'
    	self.spellslots= [None, 3,0,0,0,0,0,0,0,0]
    	self.equipment= self.items
    	giveskills(self=self)
    	givestats(self=self)
    	givemaxhp(self=self)
    	giverace(self=self)
    	statblock(self)
    	print(f'Would you like to start with this character?')
    	confirm=multich(ch1='Yes', ch2='No')
    	if confirm== 'A':
    		break
    	if confirm=='B':
    		giveclass(self)
    	return self.playclass  
#Makes the player choose a race and applies bonuses based on choice.
def giverace(self):
	race= multich(ch1='Dragonborn', ch2='Dwarf', ch3='Elf', ch4='Gnome', ch5='Half-Elf', ch6='Halfling', ch7='Half-Orc', ch8='Human', ch9='Tiefling')
	if race == 'A':
		print("""
Your Draconic heritage manifests in a variety of Traits you share with other dragonborn.

Ability Score Increase: Your Strength score increases by 2, and your Charisma score increases by 1.

Age: Young dragonborn grow quickly. They walk hours after hatching, attain the size and Development of a 10-year-old human child by the age of 3, and reach Adulthood by 15. They live to be around 80.

Alignment: Dragonborn tend to extremes, making a conscious choice for one side or the other in the cosmic war between good and evil. Most dragonborn are good, but those who side with evil can be terrible Villains.

Size: Dragonborn are taller and heavier than Humans, standing well over 6 feet tall and averaging almost 250 pounds. Your size is Medium.

Speed: Your base walking speed is 30 feet.""")
		self.race='Dragonborn'
		self.strength= self.strength + 2
		self.charisma= self.charisma + 1
		self.speed= 30
	elif race=='B':
		self.race='Dwarf'
	elif race=='C':
		self.race='Elf'
	elif race=='D':
		self.race='Gnome'
	elif race=='E':
		self.race='Half-Elf'
	elif race=='F':
		self.race='Halfling'
	elif race=='G':
		self.race='Half-Orc'
	elif race=='H':
		self.race='Human'
	elif race=='I':
		self.race='Tiefling'
	else:
		print('Option not supported.')
###Calls to assign the players stats by dice rolling.
###Roll stats (4d6-1) and picks them for which trait.
def givestats(self):
	def stat1():
		stat=[]
		for i in range(0,4):
			n = random.randint(1,6)
			stat.append(n)
			stat= sorted(stat)
		print(stat)
		del stat[0]
		stat= sum(stat)
		print(stat)
		return stat
	def stat2():
		statlist = []
		stat=stat1()
		statlist.append(stat)
		stat2=stat1()
		statlist.append(stat2)
		stat3=stat1()
		statlist.append(stat3)
		stat4=stat1()
		statlist.append(stat4)
		stat5=stat1()
		statlist.append(stat5)
		stat6=stat1()
		statlist.append(stat6)
		statlist= sorted(statlist)
		print(statlist)
		return statlist
	player1stats=stat2()
	print(player1stats)
	print(len(player1stats))
	str=0
	dex=0
	con=0
	wis=0
	int=0
	cha=0
	while len(player1stats) > 0:
		lennum= len(player1stats) -1
		print(f'Select stat to assign {player1stats[lennum]}')
		statgive=multich(ch1='Strength',ch2='Dexterity',ch3='Constitution',ch4='Wisdom',ch5='Intelligence',ch6='Charisma')
		if statgive=='A' and str==0:
			self.strength=player1stats[lennum]
			str=player1stats[lennum]
			player1stats= player1stats[:-1]
			print(f"{self.name}'s strength is set to {self.strength}.")
			print(player1stats)
		elif statgive=='A' and str!=0:
			print(f"{self.name}'s strength is set to {self.strength}.")
		else:
			None
		if statgive=='B' and dex==0:
			self.dexterity=player1stats[lennum]
			dex=player1stats[lennum]
			player1stats= player1stats[:-1]
			print(f"{self.name}'s dexterity is set to {self.dexterity}.")
			print(player1stats)
		elif statgive=='B' and dex!=0:
			print(f"{self.name}'s dexterity is set to {self.dexterity}.")
		else:
			None
		if statgive=='C' and con==0:
			self.constitution=player1stats[lennum]
			con=player1stats[lennum]
			player1stats= player1stats[:-1]
			print(f"{self.name}'s constitution is set to {self.constitution}.")
			print(player1stats)
		elif statgive=='C' and con!=0:
			print(f"{self.name}'s constitution is set to {self.strength}.")
		else:
			None
		if statgive=='D' and wis==0:
			self.wisdom=player1stats[lennum]
			wis=player1stats[lennum]
			player1stats= player1stats[:-1]
			print(f"{self.name}'s wisdom is set to {self.wisdom}.")
			print(player1stats)
		elif statgive=='D' and wis!=0:
			print(f"{self.name}'s wisdom is set to {self.wisdom}.")
		else:
			None
		if statgive=='E' and int==0:
			self.intelligence=player1stats[lennum]
			int=player1stats[lennum]
			player1stats= player1stats[:-1]
			print(f"{self.name}'s intelligence is set to {self.intelligence}.")
			print(player1stats)
		elif statgive=='E' and int!=0:
			print(f"{self.name}'s intelligence is set to {self.intelligence}.")
		else:
			None
		if statgive=='F' and cha==0:
			self.charisma=player1stats[lennum]
			cha=player1stats[lennum]
			player1stats= player1stats[:-1]
			print(f"{self.name}'s charisma is set to {self.charisma}.")
			print(player1stats)
		elif statgive=='G' and cha!=0:
			print(f"{self.name}'s charisma is set to {self.charisma}.")
		else:
			None			
#Function to call statblock. Currently shows all assigned class properties.
def statblock(player):
	self= player
	itemright= ', '.join(self.items)
	proficiencyright= ', '.join(self.proficiencies)
	equipright= ', '.join(self.equipment)
	skillsright= ', '.join(self.skills)
	statblock=print(f"""
	Name: {self.name}
	Location: {self.location}
	Items: {itemright}
	Level: {self.level}
	Experience: {self.experience}
	Class: {self.playclass}
	Race: {self.race}
	Strength: {self.strength}
	Dexterity: {self.dexterity}
	Constitution: {self.constitution}
	Wisdom: {self.wisdom}
	Intelligence: {self.intelligence}
	Charisma: {self.charisma}
	Maximum HP: {self.maxhp}
	HP: {self.hp}
	Spells: {self.spells}
	Spellslots: {self.spellslots}
	Equipment:{equipright}
	Speed: {self.speed}
	Skills: {skillsright}
	Proficiencies: {proficiencyright}""")
	return self	
#Give a martial weapon. Called in giveclass setup.
martiallist=['Battleaxe','Flail','Glave','Greataxe','Greatsword','Halberd','Lance','Longsword','Maul','Morningstar','Pike','Rapier','Scimitar','Shortsword','Trident','Warpick','Warhammer','Whip']
def givemartial(self):
	marchoice=multich(ch1=martiallist[0], ch2=martiallist[1], ch3=martiallist[2], ch4=martiallist[3], ch5=martiallist[4], ch6=martiallist[5], ch7=martiallist[6], ch8=martiallist[7], ch9=martiallist[8], ch10=martiallist[9], ch11=martiallist[10], ch12=martiallist[11], ch13=martiallist[12], ch14=martiallist[13], ch15=martiallist[14], ch16=martiallist[15], ch17=martiallist[16], ch18=martiallist[17])
	if marchoice=='A':
		given= martiallist[0]
	elif marchoice=='B':
		given= martiallist[1]
	elif marchoice=='C':
		given= martiallist[2]
	elif marchoice=='D':
		given= martiallist[3]
	elif marchoice=='E':
		given= martiallist[4]
	elif marchoice=='F':
		given= martiallist[5]
	elif marchoice=='G':
		given= martiallist[6]
	elif marchoice=='H':
		given= martiallist[7]
	elif marchoice=='I':
		given= martiallist[8]
	elif marchoice=='J':
		given= martiallist[9]
	elif marchoice=='K':
		given= martiallist[10]
	elif marchoice=='L':
		given= martiallist[11]
	elif marchoice=='M':
		given= martiallist[12]
	elif marchoice=='N':
		given= martiallist[13]
	elif marchoice=='O':
		given= martiallist[14]
	elif marchoice=='P':
		given= martiallist[15]
	elif marchoice=='Q':
		given= martiallist[16]
	elif marchoice=='R':
		given= martiallist[17]	
	else:
		print('Option not supported')	
	return given
#Give a simple weapon. Called in giveclass.
simplelist=['Club','Dagger','Greatclub','Handaxe','Javelin','Light Hammer','Mace','Quarterstaff','Sickle','Spear','Light Crossbow','Dart','Shortbow','Sling']
def givesimple(self):
	marchoice=multich(ch1=simplelist[0], ch2=simplelist[1], ch3=simplelist[2], ch4=simplelist[3], ch5=simplelist[4], ch6=simplelist[5], ch7=simplelist[6], ch8=simplelist[7], ch9=simplelist[8], ch10=simplelist[9], ch11=simplelist[10], ch12=simplelist[11], ch13=simplelist[12], ch14=simplelist[13])
	if marchoice=='A':
		given= simplelist[0]
	elif marchoice=='B':
		given= simplelist[1]
	elif marchoice=='C':
		given= simplelist[2]
	elif marchoice=='D':
		given= simplelist[3]
	elif marchoice=='E':
		given= simplelist[4]
	elif marchoice=='F':
		given= simplelist[5]
	elif marchoice=='G':
		given= simplelist[6]
	elif marchoice=='H':
		given= simplelist[7]
	elif marchoice=='I':
		given= simplelist[8]
	elif marchoice=='J':
		given= simplelist[9]
	elif marchoice=='K':
		given= simplelist[10]
	elif marchoice=='L':
		given= simplelist[11]
	elif marchoice=='M':
		given= simplelist[12]
	elif marchoice=='N':
		given= simplelist[13]
	else:
		print('Option not supported')	
	return given
#Gives four skills. Currently Barbarian, Bard, Cleric work.
def giveskills(self):
	print("Choose from the skills below.")
	skill1=0
	skill2=0
	skill3=0
	skill4=0
	while self.playclass=='Barbarian' and len(self.skills) < 2:
		skill1=multich(ch1='Animal Handling', ch2='Athletics', ch3='Intimidation', ch4='Nature', ch5='Perception', ch6='Survival')
		if skill1=='A':
			self.skills.append('Animal Handling')
		elif skill1=='B':
			self.skills.append('Athletics')
		elif skill1=='C':
			self.skills.append('Intimidation')
		elif skill1=='D':
			self.skills.append('Nature')
		elif skill1=='E':
			self.skills.append('Perception')
		elif skill1=='F':
			self.skills.append('Survival')
		else:
			None
	while self.playclass=='Cleric' and len(self.skills) < 2:
		skill1=multich(ch1='History', ch2='Insight', ch3='Medicine', ch4='Persuasion', ch5='Religion')
		if skill1=='A':
			self.skills.append('History')
		elif skill1=='B':
			self.skills.append('Insight')
		elif skill1=='C':
			self.skills.append('Medicine')
		elif skill1=='D':
			self.skills.append('Persuasion')
		elif skill1=='E':
			self.skills.append('Religion')
		else:
			None
	while len(self.skills) < 4 and self.playclass!='Bard':
		skill=multich(ch1='Acrobatics', ch2='Animal Handling', ch3='Arcana', ch4='Athletics', ch5='Deception', ch6='History', ch7='Insight', ch8='Intimidation', ch9='Investigation', ch10='Medicine', ch11='Nature', ch12='Perception', ch13='Performance', ch14='Persuasion', ch15='Religion', ch16='Sleight of Hand', ch17='Stealth', ch18='Survival')
		if skill=='A':
			self.skills.append('Acrobatics')
		if skill=='B':
			self.skills.append('Animal Handling')
		if skill=='C':
			self.skills.append('Arcana')
		elif skill=='D':
			self.skills.append('Athletics')
		elif skill=='E':
			self.skills.append('Deception')
		elif skill=='F':
			self.skills.append('History')
		elif skill=='G':
			self.skills.append('Insight')
		elif skill=='H':
			self.skills.append('Intimidation')
		elif skill=='I':
			self.skills.append('Investigation')
		elif skill=='J':
			self.skills.append('Medicine')
		elif skill=='K':
			self.skills.append('Nature')
		elif skill=='L':
			self.skills.append('Perception')
		elif skill=='M':
			self.skills.append('Performance')
		elif skill=='N':
			self.skills.append('Persuasion')
		elif skill=='O':
			self.skills.append('Religion')
		elif skill=='P':
			self.skills.append('Slight of Hand')
		elif skill=='Q':
			self.skills.append('Stealth')
		elif skill=='R':
			self.skills.append('Survival')
		else:
			None
	while len(self.skills) < 5 and self.playclass=='Bard':
		skill=multich(ch1='Acrobatics', ch2='Animal Handling', ch3='Arcana', ch4='Athletics', ch5='Deception', ch6='History', ch7='Insight', ch8='Intimidation', ch9='Investigation', ch10='Medicine', ch11='Nature', ch12='Perception', ch13='Performance', ch14='Persuasion', ch15='Religion', ch16='Sleight of Hand', ch17='Stealth', ch18='Survival')
		if skill=='A':
			self.skills.append('Acrobatics')
		if skill=='B':
			self.skills.append('Animal Handling')
		if skill=='C':
			self.skills.append('Arcana')
		elif skill=='D':
			self.skills.append('Athletics')
		elif skill=='E':
			self.skills.append('Deception')
		elif skill=='F':
			self.skills.append('History')
		elif skill=='G':
			self.skills.append('Insight')
		elif skill=='H':
			self.skills.append('Intimidation')
		elif skill=='I':
			self.skills.append('Investigation')
		elif skill=='J':
			self.skills.append('Medicine')
		elif skill=='K':
			self.skills.append('Nature')
		elif skill=='L':
			self.skills.append('Perception')
		elif skill=='M':
			self.skills.append('Performance')
		elif skill=='N':
			self.skills.append('Persuasion')
		elif skill=='O':
			self.skills.append('Religion')
		elif skill=='P':
			self.skills.append('Slight of Hand')
		elif skill=='Q':
			self.skills.append('Stealth')
		elif skill=='R':
			self.skills.append('Survival')
		else:
			None
#Define Maxhp according to assigned class and rolled stats.
def givemaxhp(self):
	if self.playclass=='Barbarian':
		self.maxhp= 12 + modify(self.constitution)
	elif self.playclass=='Bard':
		self.maxhp= 8 + modify(self.constitution)
	elif self.playclass=='Cleric':
		self.maxhp= 8 + modify(self.constitution)
	elif self.playclass=='Druid':
		self.maxhp= 8 + modify(self.constitution)
	elif self.playclass=='Fighter':
		self.maxhp= 10 + modify(self.constitution)
	elif self.playclass=='Monk':
		self.maxhp= 8 + modify(self.constitution)
	elif self.playclass=='Paladin':
		self.maxhp= 10 + modify(self.constitution)
	elif self.playclass=='Ranger':
		self.maxhp= 10 + modify(self.constitution)
	elif self.playclass=='Rogue':
		self.maxhp= 8 + modify(self.constitution)
	elif self.playclass=='Sorcerer':
		self.maxhp= 6 + modify(self.constitution)
	elif self.playclass=='Warlock':
		self.maxhp= 8 + modify(self.constitution)
	elif self.playclass=='Wizard':
		self.maxhp= 6 + modify(self.constitution)
	else:
		None
#Defining the classes for NPC and PC.
class Character:
    def __init__(self, name, location, items):
        self._name = name
        self._location = location
        self._items = items
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, value):
        if value == 0:
            raise ValueError("Not assigned")
        self._location = value
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        if value == 0:
            raise ValueError("Not Assigned")
        self._items = value
    @property
    def name(self):
        return self._name
class Player(Character):
    def __init__(self, name, location, items, level, experience, playclass, race, strength, dexterity, constitution, wisdom, intelligence, charisma, maxhp, hp, spells, spellslots, equipment, speed, skills, proficiencies):
        super().__init__(name=name, location=location, items=items)
        self._level= level
        self._experience= experience
        self._playclass= playclass
        self._race= race
        self._strength= strength
        self._dexterity= dexterity
        self._constitution= constitution
        self._wisdom= wisdom
        self._intelligence= intelligence
        self._charisma= charisma
        self._maxhp= maxhp
        self._hp= hp
        self._spells= spells
        self._spellslots= spellslots
        self._equipment= equipment     
        self._speed= speed   
        self._skills= skills
        self._proficiencies= proficiencies
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, value):
        self._level = value        
    @property
    def experience(self):
        return self._experience
    @experience.setter
    def experience(self, value):
        self._experience = value        
    @property
    def playclass(self):
        return self._playclass
    @playclass.setter
    def playclass(self, value):
        self._playclass = value   
    @property
    def race(self):
        return self._race
    @race.setter
    def race(self, value):
        self._race = value        
    @property
    def strength(self):
        return self._strength
    @strength.setter
    def strength(self, value):
        self._strength = value        
    @property
    def dexterity(self):
        return self._dexterity
    @dexterity.setter
    def dexterity(self, value):
        self._dexterity = value       
    @property
    def constitution(self):
        return self._constitution
    @constitution.setter
    def constitution(self, value):
        self._constitution = value        
    @property
    def wisdom(self):
        return self._wisdom
    @wisdom.setter
    def wisdom(self, value):
        self._wisdom = value        
    @property
    def intelligence(self):
        return self._intelligence
    @intelligence.setter
    def intelligence(self, value):
        self._intelligence = value        
    @property
    def charisma(self):
        return self._charisma
    @charisma.setter
    def charisma(self, value):
        self._charisma = value        
    @property
    def maxhp(self):
        return self._maxhp
    @maxhp.setter
    def maxhp(self, value):
        self._maxhp = value     
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, value):
        self._hp = value      
    @property
    def spells(self):
        return self._spells
    @spells.setter
    def spells(self, value):
        self._spells = value        
    @property
    def spellslots(self):
        return self._spellslots
    @spellslots.setter
    def spellslots(self, value):
        self._spellslots = value        
    @property
    def equipment(self):
        return self._equipment
    @equipment.setter
    def equipment(self, value):
        self._equipment = value     
    @property
    def speed(self):
    	return self._speed
    @speed.setter
    def speed(self,value):
    	self._speed= value
    @property
    def skills(self):
    	return self._skills
    @skills.setter
    def skills(self,value):
    	self._skills= value
    @property
    def proficiencies(self):
    	return self._proficiencies
    @proficiencies.setter
    def proficiencies(self,value):
    	self._proficiencies= value
###Start PC 'player'.###
player1= Player(name=givename(), location=0, items=[], level=1, experience=0, playclass=0, race=0, strength= 0, dexterity=0, constitution=0, wisdom=0, intelligence=0, charisma=0, maxhp=0, hp=0, spells=0, spellslots=[], equipment=[], speed=0, skills=[], proficiencies=[])
giveclass(player1)
statblock(player1)
