# V.G. Data
# These lists contain the data used in the recommendation software.

#This is the list of genres of video games included.

types = ["survival/crafting", "action", "simulation", "turn-based rpg", "open-world rpg", "metroidvania", "rogue-like", "first-person shooter", "third-person shooter", "comedy", "puzzle", "sandbox", "social deduction", "horror", "crpg"]

#This is the list of all video games and related attributes.
video_games = [['social deduction', 'Among Us', 'Innersloth', 'Very Positive'],
               ['action', "Assassin's Creed", 'Ubisoft', 'Very Positive'],
               ['survival/crafting', 'Astroneer', 'System Era Softworks', 'Very Positive'],
               ['crpg', "Baldur's Gate 3", 'Lirian Studios', 'Overwhelmingly Positive'],
               ['action', 'Bastion', 'Supergiant Games', 'Overwhelmingly Positive'],
               ['simulation', 'Besiege', 'Spiderling Studios', 'Overwhelmingly Positive'],
               ['first-person shooter', 'Borderlands', 'Gearbox Software/2K', 'Overwhelmingly Positive'],
               ['metroidvania', 'Cave Story', 'Nicalis, Inc.', 'Very Positive'],
               ['turn-based rpg', 'Child of Light', 'Ubisoft', 'Very Positive'],
               ['open-world rpg', 'Elden Ring', 'FromSoftware Inc.', 'Very Positive'],
               ['rogue-like', 'Dead Cells', 'Motion Twin', 'Overwhelmingly Positive'],
               ['open-world rpg', 'Dragon Age Inquisition', 'EA/Bioware', 'Mostly Positive'],
               ['rogue-like', 'Dungeon Souls', 'Lamina Studios', 'Mostly Positive'],
               ['open-world rpg', 'Skyrim', 'Bethesda', 'Very Positive'],
               ['open-world rpg', 'Fallout 4', 'Bethesda', 'Very Positive'],
               ['first-person shooter', 'Far Cry', 'Ubisoft', 'Very Positive'],
               ['horror', "Five Nights at Freddy's", 'Scott Cawthon', 'Very Positive'],
               ['sandbox', "Garry's Mod", 'Valve', 'Overwhelmingly Positive'],
               ['metroidvania', 'Ghost 1.0', 'Unepic Games', 'Very Positive'],
               ['first-person shooter', 'Half-Life 2', 'Valve', 'Overwhelmingly Positive'],
               ['first-person shooter', 'Left 4 Dead 2', 'Valve', 'Overwhelmingly Positive'],
               ['comedy', 'Magicka', 'Paradox Interactive', 'Very Positive'],
               ['comedy', 'Trover Saves the Universe', 'Squanch Games, Inc.', 'Very Positive'],
               ['third-person shooter', 'Mass Effect', 'EA/Bioware', 'Very Positive'],
               ['metroidvania', 'Ori and the Blind Forest', 'Moon Studios GmbH', 'Overwhelmingly Positive'],
               ['puzzle', 'Portal 2', 'Valve', 'Overwhelmingly Positive'],
               ['action', 'Prince of Persia', 'Mostly Positive'],
               ['action', 'Prototype', 'Mostly Positive'],
               ['survival/crafting', 'Raft', 'Axolot Games/Redbeet Interactive', 'Very Positive'],
               ['action', 'Remember Me', 'Capcom', 'Very Positive'],
               ['metroidvania', 'Shantae', 'WayForward', 'Very Positive'],
               ['sandbox', 'Spore', 'EA/Maxis', 'Very Positive'],
               ['sandbox', 'Starbound', 'Chucklefish', 'Very Positive'],
               ['simulation', 'Stardew Valley', 'ConcernedApe', 'Overwhelmingly Positive'],
               ['open-world rpg', 'Starfield', 'Bethesda', 'Mixed'],
               ['horror', 'Subnautica', 'Unknown Worlds Entertainment', 'Overwhelmingly Positive'],
               ['metroidvania', 'Sundered', 'Thunder Lotus Games', 'Very Positive'],
               ['survival/crafting', 'Terraria', 'Re-Logic', 'Overwhelmingly Positive'],
               ['third-person shooter', 'Tomb Raider', 'Crystal Dynamics, Eidos,...', 'Overwhelmingly Positive'],
               ['social deduction', 'Town of Salem', 'BlankMediaGames LLC', 'Mostly Positive'],
               ['social deduction', 'West Hunt', 'Wandering Wizard/NewGen', 'Very Positive'],
               ['turn-based rpg', 'Darkest Dungeon', 'Red Hook Studios', 'Very Positive'],
               ['puzzle', 'It Takes Two', 'EA/Hazelight', 'Very Positive'],
               ['puzzle', 'Animal Well', 'Bigmode/Billy Basso', 'Overwhelmingly Positive'],
               ['crpg', 'Caves of Qud', 'Kitfox Games/Freehold Games', 'Overwhelmingly Positive'],
               ['crpg', 'Pathfinder: Wrath of the Righteous', 'Owlcat Games', 'Very Positive'],
               ['horror', 'Dying Light', 'Techland', 'Overwhelmingly Positive'],
               ['horror', 'Lethal Company', 'Zeekerss', 'Overwhelmingly Positive'],
               ['simulation', 'PowerWash Simulator', 'Square Enix/FuturLab', 'Overwhelmingly Positive'],
               ['simulation', 'Microsoft Flight Simulator', 'Asobo Studio', 'Mostly Positive']
]

#These functions sort the tables above and overwrites them.
video_games.sort()
types.sort()