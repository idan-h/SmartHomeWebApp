import clipboard
import time


def decode_from_windows_1255(encoded_str):
    encoded_bytes = encoded_str.encode('latin-1')
    return encoded_bytes.decode('windows-1255')


def change_clipboard(content):
    try:
        result = decode_from_windows_1255(content)
    except (Exception,):
        return content

    clipboard.copy(result)
    return result


def clipboard_monitor():
    """
    Monitors the clipboard for changes and checks for special characters.
    """
    recent_value = ""
    while True:
        tmp_value = clipboard.paste()
        if tmp_value != recent_value:
            recent_value = change_clipboard(tmp_value)
        time.sleep(0.1)


if __name__ == "__main__":
    clipboard_monitor()
