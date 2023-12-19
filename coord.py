from pynput import mouse

def on_click(x, y, button, pressed):
    if button == mouse.Button.right:
        if pressed:
            print(f"Right click at position {x}, {y}")
            return False  # Detiene el listener

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
