import json
import os

# Application configuration for PS5 homebrew launcher
APP_TITLE = "Kroma Autoloader PLD"
APP_TITLE_ID = "KROM00002"
DEEPLINK_URL = "https://nobodyttk.github.io/relapse/relapse.html"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)

ORIG_ELF = os.path.join(BASE_DIR, "ps5", "poopspl", "payloads", "browser_launcher.elf")
ICON_PNG = os.path.join(SCRIPT_DIR, "best_icon.png")
OUT_ELF = os.path.join(SCRIPT_DIR, "kroma_autoloader_pld.elf")

def build():
    with open(ORIG_ELF, "rb") as f:
        data = bytearray(f.read())

    with open(ICON_PNG, "rb") as f:
        icon_data = f.read()

    # Icon: exactly 8261 bytes allocated in .rodata
    ORIG_ICON_SIZE = 8261
    assert len(icon_data) <= ORIG_ICON_SIZE, "Icon exceeds allocated 8261 bytes!"
    padded_icon = icon_data.ljust(ORIG_ICON_SIZE, b"\x00")

    config = {
        "titleId": APP_TITLE_ID,
        "applicationCategoryType": 65536,
        "deeplinkUri": DEEPLINK_URL,
        "localizedParameters": {
            "defaultLanguage": "en-US",
            "en-US": {
                "titleName": APP_TITLE
            }
        }
    }

    # JSON configuration block must be exactly 264 bytes to preserve ELF alignment
    json_bytes = (json.dumps(config, indent=2) + "\n   ").encode("utf-8")
    assert len(json_bytes) == 264, f"Invalid JSON byte length: {len(json_bytes)}"

    json_start = data.find(b'{\n    "titleId"')
    assert json_start == 159648

    # 1. Replace JSON configuration block
    data[json_start : json_start + 264] = json_bytes

    # 2. Replace titleId occurrences
    data = bytearray(bytes(data).replace(b"BRWS00001", APP_TITLE_ID.encode()))

    # 3. Embed custom icon
    icon_offset = 159920
    assert data[icon_offset:icon_offset+4] == b"\x89PNG"
    data[icon_offset : icon_offset + ORIG_ICON_SIZE] = padded_icon

    assert len(data) == 416352, f"Invalid ELF size: {len(data)}"

    with open(OUT_ELF, "wb") as f:
        f.write(data)

    print(f"[SUCCESS] Output generated: {OUT_ELF} ({len(data)} bytes)")
    print(f"Title:    {APP_TITLE} ({APP_TITLE_ID})")
    print(f"Deeplink: {DEEPLINK_URL}")

if __name__ == "__main__":
    build()
