import pyautogui

def click_at_position(clicks):
    input("Move the mouse to the desired location and press Enter.")
    
    # Get the current mouse position
    x, y = pyautogui.position()

    print(f"Mouse positioned at: ({x}, {y}). Starting clicks.")

    # Perform clicking action 1000 times
    for _ in range(clicks):
        pyautogui.click(x, y)
 
        #time.sleep(click_interval)  # Adding a small delay between clicks

    print("Clicking completed.")

# Example usage
click_at_position(100)
