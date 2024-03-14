#!/usr/bin/env python3
"""
Defines a function that takes a list of
lists representing the keys of each box
"""


def canUnlockAll(boxes):
    """This function determines if all the boxes can be opened."""
    visited = [False] * len(boxes)
    visited[0] = True

    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
