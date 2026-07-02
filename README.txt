NOTE: THE DESIRED DIRECTORY MAY BE IN C:\Users\YOUR_USERNAME\AppData\Local\Orsoniks\CasualtiesUnknown NOT C:\Users\YOUR_USERNAME\AppData\LocalLow\Orsoniks\CasualtiesUnknown

HOW TO USE
place the RemoveHollow.py file in your C:\Users\YOUR_USERNAME\AppData\LocalLow\Orsoniks\CasualtiesUnknown directory

in powershell/cmd, after replacing YOUR_USERNAME, run:
cd C:\Users\YOUR_USERNAME\AppData\LocalLow\Orsoniks\CasualtiesUnknown
py RemoveHollow.py

this will run the python script, which should create a save_EDITED.sv file

MOVE YOUR OLD "save.sv" FILE SOMEWHERE YOU CAN RECOVER IT LATER
then rename "save_EDITED.sv" -> "save.sv"

when loading the save ingame check the in-game console for any errors, if there are none the save should be otherwise the same, if there are errors:
- white text -> non-critical error; you can keep playing after making sure you didnt lose anything important
- red text -> the save wont load, delete the new "save.sv" file and move the old "save.sv" file in its place to recover the save
