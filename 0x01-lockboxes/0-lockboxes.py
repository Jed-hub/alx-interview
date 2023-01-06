#!/usr/bin/python3
"""
Module lockboxes
"""


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened
    else return False
    """
    unlocked = [0]
    for i in unlocked:
        for j in boxes[i]:
            if j < len(boxes):
                if j not in unlocked:
                    unlocked.append(j)

    if len(boxes) == len(unlocked):
        return True
    else:
        return False
