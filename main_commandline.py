#This is a very lightweight version of the to-do list program I created solely for testing, but it is
#technically functional. Use at your own risk.

from item import *
from file_manager import *

def get_all_groups_in_group(group):
    groups_to_check = [group]
    groups = []
    while len(groups_to_check) > 0:
        g = groups_to_check.pop(0)
        for child in g.children:
            if type(child) is Group:
                groups_to_check.append(child)
                groups.append(child)
    
    return groups

if __name__ == "__main__":
    escape = False
    fm = FileManager()
    main_group = None
    try:
        main_group = fm.load_data()
    except:
        main_group = Group("Top Level Item")
    finally:
        if type(main_group) is not Group:
            main_group = Group("Top Level Item")

    while not escape:
        t = input("Input item type (task/group/print/escape/remove):")
        while t.lower() not in ['task','group', 'print', 'escape', 'remove']:
            t = input("Invalid item type. Input item type (task/group/print/escape/remove):")

        

        if t.lower() == 'task':
            n = input("Input item name:")
            new_task = Task(n)

            print("All groups:")
            print("    None")
            for group in get_all_groups_in_group(main_group):
                print(f"    {group.name}")

            parent = input("Select a parent group:")
            fin = parent in ([group.name for group in get_all_groups_in_group(main_group)] + ["None"])
            while not fin:
                parent = input("Not a valid group name. Select a parent group:")
                fin = parent in ([group.name for group in get_all_groups_in_group(main_group)] + ["None"])
            
            if parent == "None":
                parent = None
            else:
                for group in get_all_groups_in_group(main_group):
                    if group.name == parent:
                        parent = group
                        break
                
            exit_loop = False

            query = input("Additional options (-Dsdi) or -C to exit:")
            while not exit_loop:
                if query == "-D":
                    new_task.description = input("Set task descripion:")

                elif query == "-s":
                    s = None
                    fin = False
                    while not fin:
                        try:
                            s = int(input("Set task state (0-5):"))
                            fin = s in [0,1,2,3,4,5]
                        except:
                            pass
                    new_task.state = s

                elif query == "-d":
                    d = None
                    fin = False
                    while not fin:
                        try:
                            d = int(input("Set task difficulty (1-5):"))
                            fin = d in [1,2,3,4,5]
                        except:
                            pass
                    new_task.difficulty = d

                elif query == "-i":
                    i = None
                    fin = False
                    while not fin:
                        try:
                            i = int(input("Set task importance (1-5):"))
                            fin = i in [1,2,3,4,5]
                        except:
                            pass
                    new_task.importance = i

                elif query == "-C":
                    exit_loop = True
                    if parent is not None:
                        parent.add_child(new_task)
                    else:
                        main_group.add_child(new_task)

                if not exit_loop:
                    query = input("Additional options (-Dsdi) or -C to exit:")
        
        elif t.lower() == 'group':
            n = input("Input item name:")
            new_group = Group(n)

            print("All groups:")
            print("    None")
            for group in get_all_groups_in_group(main_group):
                print(f"    {group.name}")

            parent = input("Select a parent group:")
            fin = parent in ([group.name for group in get_all_groups_in_group(main_group)] + ["None"])
            while not fin:
                parent = input("Not a valid group name. Select a parent group:")
                fin = parent in ([group.name for group in get_all_groups_in_group(main_group)] + ["None"])
            
            if parent == "None":
                parent = None
            else:
                for group in get_all_groups_in_group(main_group):
                    if group.name == parent:
                        parent = group
                        break
                
            exit_loop = False

            query = input("Additional options (-D) or -C to escape:")
            while not exit_loop:
                if query == "-D":
                    new_group.description = input("Set task descripion:")
                    
                elif query == "-C":
                    exit_loop = True
                    if parent is not None:
                        parent.add_child(new_group)
                    else:
                        main_group.add_child(new_group)

                if not exit_loop:
                    query = input("Additional options (-D) or -C to escape:")

        elif t.lower() == "print":
            print(main_group)
        
        elif t.lower() == "escape":
            fm.save_data(main_group)
            escape = True

        elif t.lower() == "remove":
            print("All groups:")
            print("    None")
            for group in get_all_groups_in_group(main_group):
                print(f"    {group.name}")

            parent = input("Select a parent group:")
            fin = parent in ([group.name for group in get_all_groups_in_group(main_group)] + ["None"])
            while not fin:
                parent = input("Not a valid group name. Select a parent group:")
                fin = parent in ([group.name for group in get_all_groups_in_group(main_group)] + ["None"])
            
            if parent == "None":
                parent = main_group
            else:
                for group in get_all_groups_in_group(main_group):
                    if group.name == parent:
                        parent = group
                        break
                
            exit_loop = False

            print(f"Items in {parent.name}:")
            for child in parent.children:
                print(f"    {child.name}")

            child = input("Select an item to remove:")
            fin = child in [child.name for child in parent.children]
            while not fin:
                child = input("Select an item to remove:")
                fin = child in [child.name for child in parent.children]
        
            for item in parent.children:
                if item.name == child:
                    child = item
                    break
            
            parent.remove_child(child)