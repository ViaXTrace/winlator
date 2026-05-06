# Winlator

An Android application that lets you run Windows (x86_64) applications with Wine and Box86/Box64.

## Run & Operate

- **Dev server:** `python3 serve.py` (serves static files on port 5000)
- No build step required — static HTML only

## Stack

- Static HTML/CSS (index.html)
- Python 3 SimpleHTTPServer for local preview

## Where things live

- `index.html` — main informational page
- `serve.py` — local dev HTTP server
- `input_controls/` — game input control profiles (.icp files)
- `installable_components/` — box64, dxvk, turnip, vkd3d, wined3d bundles
- `installable_components/wine-*.msi` — Wine Gecko and Mono installers
- `android_alsa/` — Android ALSA audio module source
- `glibc_patches/` — GLIBC patches from Termux Pacman
- `wine_addons/` — Additional Wine component installers

## Architecture decisions

- This is a native Android APK project — there is no web server or backend
- The Replit preview shows a static informational page about the project
- Submodules (`app`, `vortek`, `gladio`) contain the main Android app source but are not initialized in this clone
- Deployment is configured as a static site serving the root directory

## Product

- Winlator lets Android users run Windows games and applications
- Uses Wine for Windows API compatibility
- Uses Box86/Box64 for x86/x86_64 emulation on ARM processors
- Supports DXVK and VKD3D for DirectX-to-Vulkan translation
- Includes 50+ game input control profiles

## User preferences

_Populate as you build_

## Gotchas

- Submodules (app, vortek, gladio) are empty — they require `git submodule update --init` to populate
- The actual Android build requires Android SDK/NDK, not available in the Replit environment

## Pointers

- [GitHub Releases](https://github.com/brunodev85/winlator/releases) — APK downloads
- [winehq.org](https://www.winehq.org/) — Wine documentation
