import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class IndecisiveZombie:
    # Zombie randomly decides if it will roll for every roll after first roll

    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):
        results = zombiedice.roll()

        while results is not None:
            if random.randint(0, 1) == 0:
                results = zombiedice.roll()
            else:
                break

class ContentZombie:
    # Zombie stops after rolling 2 brains

    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):
        results = zombiedice.roll()

        brains = 0
        while results is not None:
            brains += results['brains']

            if brains < 2:
                results = zombiedice.roll()
            else:
                break

class CowardZombie:
    # Zombie stops after rolling 2 shotguns (probably smart tbh)

    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):
        results = zombiedice.roll()

        shotguns = 0
        while results is not None:
            shotguns += results['shotgun']

            if shotguns < 2:
                results = zombiedice.roll()
            else:
                break

class SpookedZombie:
    # Zombie randomly decides to roll 1-4 times, but will stop after rolling 2 shotguns

    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):
        results = zombiedice.roll()

        rollNum = random.randint(1,4)

        shotguns = 0
        shotguns += results['shotgun']
        for roll in range(rollNum):
            if shotguns == 2 or results is None:
                break

            shotguns += results['shotgun']
            results = zombiedice.roll()

class MathingZombie:
    # Zombie stops rolling after it's rolled more shotguns than brains

    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):
        results = zombiedice.roll()

        shotguns = 0
        brains = 0

        while results is not None:
            shotguns += results['shotgun']
            brains += results['brains']

            if shotguns < brains:
                results = zombiedice.roll()
            else:
                break

zombies = (
    # zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    # zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    #MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
    MathingZombie(name="Mathing Zombie"),
    CowardZombie(name="Coward Zombie"),
    ContentZombie(name = "Content Zombie" ),
    SpookedZombie(name = "Spooked Zombie"),
    IndecisiveZombie(name = "Indecisive Zombie")

)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
