"""You are creating a fantasy video game.
The data structure to model the player's inventory will be
a dictionnary where the keys are string values
describing the item in the items in the inventory
and the value is an integer value detailing
how many of that item the player has.
write a function named displayInventory()
that would take any possible inventory and display it
imagine that a vanquished dragon loot is represented as a list of strings
write a function named addToInventory(inventory, addedItems)
where the onventory parameter is the one previously used
and the addedItems parameter is a list like dragonloot
the addToInventory function should return
a dictionary that represents the updated inventory """

inventory = {'rope': 1, 'torch': 5, 'gold coin': 56, 'dagger': 3, 'arrow': 56}
dragonloot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(v , k)
        item_total += v
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    # update the player’s inventory dictionary
    # by adding each item from the addedItems list – one by one –
    # and incrementing the count for that item.

    # iterate over each items in addedItems
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

inventory = addToInventory(inventory, dragonloot)
displayInventory(inventory)