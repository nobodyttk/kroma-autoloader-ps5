# Kroma Autoloader PLD (PS5)

A standalone PS5 homebrew ELF shortcut launcher that automatically runs the **Relapse** WebKit + Kernel exploit chain by **soniciso1** and immediately auto-loads the **PS5 Payload Manager (pldmgr v0.5.2)** on port `9021`.

---

## Why I Built This

I came up with this idea because, unfortunately, the `webkit-autoloader` isn't fully stable for me yet (huge shoutout and stay strong, itsPLK!). Other solutions I tested that attempted to bundle and load multiple payloads at once (kstuff, etaHEN, etc.) were frequently triggering kernel panics / crashing my console.

As a provisional workaround and fueled by a healthy dose of pure laziness I created this shortcut to automate the entire process through soniciso1's method, which solely focuses on a clean, reliable jailbreak. From there, I chose to auto-load only what was essential for my workflow: the **PS5 Payload Manager (pldmgr)**. 

### Want to Auto-Load a Different Payload?

Because the official upstream host (`soniciso1.github.io`) cannot be modified remotely, customizing which payload auto-loads requires hosting your own modified copy of Relapse:

1. **Fork or Clone Relapse:** Head over to [soniciso1/relapse](https://github.com/soniciso1/relapse) and create your own fork.
2. **Edit `relapse.html`:** Near the bottom of `relapse.html` (inside `run().then(...)`), specify the payload file you want to automatically trigger upon a successful jailbreak (e.g., `etaHEN.elf`, `kstuff-lite_v1.11.elf`, etc.):
   ```javascript
   if (window.__elfldrUp && typeof window.__sendPayload === "function") {
       showPayloadMenu();
       await window.__sendPayload("YOUR_CHOSEN_PAYLOAD.elf");
   }
   ```
3. **Deploy to GitHub Pages:** In your repository settings, enable **GitHub Pages** (Settings > Pages > Source: `main` branch).
4. **Build Your Custom ELF:** Update `DEEPLINK_URL` in `build_kroma.py` with your new GitHub Pages URL and run the script to generate your custom installer!

---

## Features

- **Home Screen Shortcut:** Installs directly to the PS5 dashboard with a custom title and icon (`icon0.png`).
- **No Jailbreak Required on Boot:** Launches via the native PS5 system deeplink API (`browser_install_app`). Once installed, you can launch it anytime without an active jailbreak.
- **Full Automation:**
  1. Opens the customized [Relapse exploit](https://nobodyttk.github.io/relapse/relapse.html).
  2. Runs the WebKit + Kernel jailbreak chain automatically.
  3. Once `elfldr` is active on port `9021`, it immediately auto-loads `pldmgr_v0.5.2.elf` without requiring any controller input.
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
