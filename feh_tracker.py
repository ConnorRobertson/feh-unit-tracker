# Allows you to stat units and update them as time goes on.
# Allows you to perform queries on your units

import numpy as np
import pandas as pd
import math


"""
    Units are manually formatted with this data structure:
    ["Name", "HP", "Atk", "Spd", "Def", "Res"]

    Total will be calculated when UpdateTotal gets run
"""


def CreateSheet():
    listUnits = np.array([])  # Feel free to populate this in the format below.
    df = pd.DataFrame(listUnits)
    df.columns = ["Name", "HP", "Atk", "Spd", "Def", "Res"]

    df.to_csv("UnitList.csv", index=False)
    print(df.head())


def ImportSheet():
    df = pd.read_csv("UnitList.csv")
    return df


def AddDragonFlowers(name, stats, df):
    row_ind = df.loc[df["Name"] == name].index[0]
    # Update Stats Note: this will change the csv when saved
    df.loc[row_ind, "HP"] = df.loc[row_ind, "HP"] + stats[0]
    df.loc[row_ind, "Atk"] = df.loc[row_ind, "Atk"] + stats[1]
    df.loc[row_ind, "Spd"] = df.loc[row_ind, "Spd"] + stats[2]
    df.loc[row_ind, "Def"] = df.loc[row_ind, "Def"] + stats[3]
    df.loc[row_ind, "Res"] = df.loc[row_ind, "Res"] + stats[4]


def RemoveDragonFlowers(name, stats, df):
    row_ind = df.loc[df["Name"] == name].index[0]
    # Update Stats Note: this will change the csv when saved
    df.loc[row_ind, "HP"] = df.loc[row_ind, "HP"] - stats[0]
    df.loc[row_ind, "Atk"] = df.loc[row_ind, "Atk"] - stats[1]
    df.loc[row_ind, "Spd"] = df.loc[row_ind, "Spd"] - stats[2]
    df.loc[row_ind, "Def"] = df.loc[row_ind, "Def"] - stats[3]
    df.loc[row_ind, "Res"] = df.loc[row_ind, "Res"] - stats[4]


def SaveCSV(df):
    """
    Note: Saves changes caused by below functions to the CSV
    """
    df.to_csv("UnitList.csv", index=False)


def AddUnit(unit, df):
    """
    Adds unit in the shape of:
            ["Name", "HP", "Atk", "Spd", "Def", "Res"]
    Note: this will change the csv when saved
    """
    df.loc[len(df)] = unit  # Duplicate units must be added with different formatting
    print(df)


def UpdateTotal(df):
    """
    Will add total BST to units if missing.
    Note: this will change the csv when saved
    """
    total = df[["HP", "Atk", "Spd", "Def", "Res"]].agg("sum", axis=1)
    df = df.assign(Total=total)
    return df


def FunctionStat(stat, function, df):
    """
    Performable functions:
            mean, mode, max, sum, min

    Will return a floored integer

    """
    res = df[[stat]].agg(function, axis=0)
    print("The ", function, "of the ", stat, " is:", res)
    return math.floor(res[stat])


def SearchUnitByStat(stat, value, df):
    res = df[df[stat] == value]
    print(res)


def SearchUnitsWithGreaterThanEqualToStat(stat, value, df):
    res = df[df[stat] >= value]
    print(res)


def SearchUnitsWithLessThanEqualToStat(stat, value, df):
    res = df[df[stat] <= value]
    print(res)


df = ImportSheet()  # IFF a csv named "UnitList.csv" exists otherwise CreateSheet
print(df.head())  # Do this to display the first 5 entries of the CSV
# AddDragonFlowers("LNinian", [1, 1, 1, 1, 1], df)
StatTest = "Def"  # Can be changed to HP Atk Spd Def Res and Total (if UpdateTotal has been run on the CSV)
# test = FunctionStat(StatTest, "min", df) this returns a value

SearchUnitByStat(
    StatTest, test, df
)  # Finds the name of the units around the resulting value
SaveCSV(df)
