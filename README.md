# Ogre Boger Booger Fart

## config.yaml

total_dice: the total number of dice to roll
trials: the total number of simulations to run (higher=more accurate, lower=shorter run-time)

## value.yaml

Point values

## dice.yaml

Definition of each dice and their sides

## How to Run

`python main.py`

## Output

```
Trials: 100000
Total Dice: 10
Dice Types: 2
Dice Sides: {'Sword', 'Ogre', 'Dragon', 'Diamond', 'Pick-Axe'}
Scored: {'Pick-Axe': 1.61608, 'Diamond': 0.8873, 'Sword': 1.09094, 'Dragon': 0.47615, 'Ogre': 1.18947}
Points: {'Pick-Axe': 1.61608, 'Diamond': 1.7746, 'Sword': 2.18188, 'Dragon': 1.9046, 'Ogre': 2.37894}
```

"Points" is the average score of a player who chose each type (during the entire 100000 trial run). So with this configuration it would be optimal to pick Ogre every time over many plays (playing blind).
