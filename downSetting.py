import pyautogui,keyboard
pos = list(range(78,60*11,60))
selectedPos = 0
savedPos = selectedPos
while True:
    if savedPos != selectedPos:
        savedPos = selectedPos
        pyautogui.click(pos[selectedPos],750)
    if keyboard.is_pressed('alt+ctrl+left'):
        if selectedPos == 0:
            selectedPos = 9
        else:
            selectedPos -= 1
    elif keyboard.is_pressed('alt+ctrl+right'):
        if selectedPos == 9:
            selectedPos = 0
        else:
            selectedPos += 1
    elif keyboard.is_pressed('alt+ctrl+m'):
        pyautogui.alert(title = "Mode",text = "Mode:" + str(selectedPos+1),button = "Done!")
    elif keyboard.is_pressed('alt+ctrl+s'):
        pyautogui.alert(title = "Setting",text = "Alt+Ctrl+'left':left Pos\nAlt+Ctrl+'right':right Pos\nAlt+Ctrl+s:Setting Page\nAlt+Ctrl+m:Selected Mode",button = "OK")
