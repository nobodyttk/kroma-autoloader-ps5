# Kroma Autoloader PLD (PS5)

A standalone PS5 homebrew ELF shortcut launcher that automatically runs the **Relapse** WebKit + Kernel exploit by **soniciso1** and immediately auto-loads **PS5 Payload Manager (pldmgr v0.5.2)** on port `9021`.

---

## Features

- **Home Screen Shortcut:** Installs directly to the PS5 dashboard with a custom title and icon (`icon0.png`).
- **No Jailbreak Required on Boot:** Launches via the native PS5 system deeplink API (`browser_install_app`). Once installed, you can launch it anytime without an active jailbreak.
- **Full Automation:**
  1. Opens the customized [Relapse exploit](https://nobodyttk.github.io/relapse/relapse.html).
  2. Runs the WebKit + Kernel jailbreak chain automatically.
  3. Once `elfldr` is active on port `9021`, it immediately auto-loads `pldmgr_v0.5.2.elf` without any manual controller input.
- **Custom Title ID:** Uses `KROM00002` so it does not overwrite or conflict with any existing browser apps or other homebrew shortcuts.

---

## Installation on PS5

1. Run your PS5 jailbreak so the ELF loader is listening on port `9021`.
2. Send `kroma_autoloader_pld.elf` to the PS5 on port `9021` using any payload sender or via terminal:
   ```bash
   python -c "import socket; s = socket.create_connection(('YOUR_PS5_IP', 9021)); s.sendall(open('kroma_autoloader_pld.elf', 'rb').read()); s.close(); print('Sent!')"
   ```
3. Return to the PS5 home screen. You will see **Kroma Autoloader PLD** installed with the custom icon.
4. Launch it anytime directly from your dashboard!

---

## Building from Source

To customize the deeplink URL, app title, or embed your own icon:

1. Place your desired icon as `best_icon.png` (or convert from `logo.jpg`).
2. Run the builder script:
   ```bash
   python build_kroma.py
   ```
3. The script will generate a new `kroma_autoloader_pld.elf`.

---

## Credits & Acknowledgements

- **[ps5xploit (WBrowser)](https://github.com/ps5xploit/WBrowser):** Based on the concepts and structure of the WBrowser project for PS5.
- **[soniciso1 (Relapse)](https://github.com/soniciso1/relapse):** Special thanks to soniciso1 for the amazing Relapse PS5 WebKit + kernel exploit chain.
- **itsPLK:** For the modern `pldmgr` (PS5 Payload Manager) dashboard and autoloader tools.
- **Karo Sharifi:** For original loader templates and PS5 scene contributions.
