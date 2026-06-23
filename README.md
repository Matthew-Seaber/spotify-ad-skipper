# 🪧 Spotify Ad Avoider

This repo automatically skips ads on Spotify by restarting the app when an ad starts playing. A list of common ad names can be found in the `common_ad_names.txt` file, which you can modify to add or remove any names of ads you want to avoid.

## How to Access
Download the latest release (v1.0-beta) on GitHub -->
### OR
- Download the project files as a `.ZIP` or clone the repo using `git clone https://github.com/matthew-seaber/spotify-ad-skipper.git` in your terminal
- Run `pip install -r requirements.txt` to install the required dependencies
- Run `python main.py` to start the program
- To create your own .exe file, run `pyinstaller --onefile --noconsole main.py --add-data "images;images" --add-data "common_ad_names.txt;."` in your terminal (the executable will appear in the `dist` folder)

## Features
- Automatically detects when an ad is playing on Spotify and restarts the app to skip it
- Customisable list of ad names
- Fully available offline
- Can be added to Windows startup in one click