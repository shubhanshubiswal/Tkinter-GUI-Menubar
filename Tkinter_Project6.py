import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Menubar')

def func():
    print('func called ')

# Menu 

# ******************************* simple menu bar ***********************
# menubar = tk.Menu(win)
# menubar.add_command(label='Save', command=func)
# menubar.add_command(label='Save As', command=func)
# menubar.add_command(label='Copy', command=func)
# menubar.add_command(label='Paste', command=func)

# ******************************* complex menu bar ***********************
main_menu = tk.Menu(win)

## file menu
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New File', command=func)
file_menu.add_command(label='New Window', command=func)
file_menu.add_separator()
file_menu.add_command(label='Open File', command=func)
file_menu.add_command(label='Open Folder', command=func)
file_menu.add_command(label='Open Workspace', command=func)
file_menu.add_command(label='Open Recent', command=func)
file_menu.add_separator()
file_menu.add_command(label='Add Folder to Workspace ', command=func)
file_menu.add_command(label='Save Workspace as..', command=func)
file_menu.add_separator()
file_menu.add_command(label='Save', command=func)
file_menu.add_command(label='Save As..', command=func)
file_menu.add_command(label='Save All', command=func)
file_menu.add_separator()
file_menu.add_command(label='Revert File', command=func)
file_menu.add_command(label='Close Window', command=func)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=func)


## edit menu
edit_menu = tk.Menu(main_menu, tearoff=0)
edit_menu.add_command(label='Undo', command=func)
edit_menu.add_command(label='Redo', command=func)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', command=func)
edit_menu.add_command(label='Copy', command=func)
edit_menu.add_command(label='Paste', command=func)
edit_menu.add_separator()
edit_menu.add_command(label='Find', command=func)
edit_menu.add_command(label='Replace', command=func)
edit_menu.add_separator()
edit_menu.add_command(label='Find in Files', command=func)
edit_menu.add_command(label='Replace in Files', command=func)

## Selection Menu
selection_menu = tk.Menu(main_menu, tearoff=0)
selection_menu.add_command(label='Select All', command=func)
selection_menu.add_command(label='Expand Selection', command=func)
selection_menu.add_command(label='Shrink Selection', command=func)
selection_menu.add_separator()
selection_menu.add_command(label='Copy Line Up', command=func)
selection_menu.add_command(label='Copy Line Down', command=func)
selection_menu.add_command(label='Duplicate Selection', command=func)
selection_menu.add_separator()
selection_menu.add_command(label='Select All Occurrences', command=func)
selection_menu.add_command(label='Column Selection Mode', command=func)


## view Menu
view_menu = tk.Menu(main_menu, tearoff=0)
view_menu.add_command(label='Command Palette..', command=func)
view_menu.add_command(label='Open View..', command=func)
view_menu.add_separator()
view_menu.add_command(label='Apprearance', command=func)
view_menu.add_command(label='Editor Layout', command=func)
view_menu.add_separator()
view_menu.add_command(label='Explorer', command=func)
view_menu.add_command(label='Search', command=func)
view_menu.add_separator()
view_menu.add_command(label='Run', command=func)
view_menu.add_command(label='Output', command=func)

## Help Menu
help_menu = tk.Menu(main_menu, tearoff=0)
help_menu.add_command(label='Welcome', command=func)
help_menu.add_command(label='Documentation', command=func)
help_menu.add_separator()
help_menu.add_command(label='Join Us On Twitter', command=func)
help_menu.add_command(label='Report Issue', command=func)
help_menu.add_separator()
help_menu.add_command(label='View License', command=func)
help_menu.add_command(label='Privacy Statement', command=func)
help_menu.add_separator()
help_menu.add_command(label='Check For Updates', command=func)
help_menu.add_command(label='About', command=func)



main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)
main_menu.add_cascade(label='Selection', menu=selection_menu)
main_menu.add_cascade(label='View', menu=view_menu)
main_menu.add_cascade(label='Help', menu=help_menu)


win.config(menu=main_menu)
win.mainloop()