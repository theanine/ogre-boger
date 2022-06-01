#!/bin/python

import yaml
import random

with open("dice.yaml", "r") as yamlfile:
    dice_data = yaml.load(yamlfile, Loader=yaml.FullLoader)
with open("value.yaml", "r") as yamlfile:
    value_data = yaml.load(yamlfile, Loader=yaml.FullLoader)
with open("config.yaml", "r") as yamlfile:
    config_data = yaml.load(yamlfile, Loader=yaml.FullLoader)

total_dice=config_data["total_dice"]
trials=config_data["trials"]

sides = set()

for dice in dice_data:
	for side in dice_data[dice]:
		sides.add(side)

dice_count=len(dice_data)
if total_dice % dice_count != 0:
	print("ERROR: total dice is {total_dice}, which can't divide into {dice_count}")

count_per_dice = total_dice // dice_count

eatMap = {
	"Pick-Axe": "Diamond",
	"Diamond": "",
	"Sword": "Dragon",
	"Dragon": "Ogre",
	"Ogre": "",
}

scoreMap = {
	"Pick-Axe": 0,
	"Diamond": 0,
	"Sword": 0,
	"Dragon": 0,
	"Ogre": 0,
}

for i in range(trials):
	countMap = {
		"Pick-Axe": 0,
		"Diamond": 0,
		"Sword": 0,
		"Dragon": 0,
		"Ogre": 0,
	}

	for dice_num in range(dice_count):
		for num in range(count_per_dice):
			side_idx = random.randrange(6)
			countMap[dice_data[dice_num][side_idx]] += 1

	scoreMap["Pick-Axe"] += min(countMap["Pick-Axe"], countMap["Diamond"])
	scoreMap["Diamond"] += max(0, countMap["Diamond"] - countMap["Pick-Axe"])
	scoreMap["Sword"] += min(countMap["Sword"], countMap["Dragon"])
	scoreMap["Dragon"] += min(max(0, countMap["Dragon"] - countMap["Sword"]), countMap["Ogre"])
	scoreMap["Ogre"] += max(0, countMap["Ogre"] - max(0, countMap["Dragon"] - countMap["Sword"]))

pointsMap = {
	"Pick-Axe": 0,
	"Diamond": 0,
	"Sword": 0,
	"Dragon": 0,
	"Ogre": 0,
}

for k in scoreMap:
	scoreMap[k] /= trials
	pointsMap[k] = scoreMap[k] * value_data[k]

print("Trials:", trials)
print("Total Dice:", total_dice)
print("Dice Types:", dice_count)
print("Dice Sides:", sides)
if trials == 1:
	print("Rolled:", countMap)
print("Scored:", scoreMap)
print("Points:", pointsMap)
