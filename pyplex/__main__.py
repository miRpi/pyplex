import argparse
from handler import runLoop

if __name__ == '__main__':
     parser = argparse.ArgumentParser(description='A daemon to listen for UDP plex playback requests, and relay them to OMXPlayer')
     parser.add_argument('--hdmi', action='store_true',help="Send audio over HDMI instead of 3.5mm jack")
     args = parser.parse_args()
     runLoop(args.hdmi)
    
