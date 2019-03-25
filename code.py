"""
This example goes and gets the number of signers to the Petition to revoke article 50 in the UK
"""

import time
import board
from adafruit_pyportal import PyPortal

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# pylint: disable=line-too-long
DATA_SOURCE = "https://petition.parliament.uk/petitions/241584/count.json"
DATA_LOCATION1 = [ "signature_count" ]

# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(url=DATA_SOURCE,
                    json_path=DATA_LOCATION1,
                    status_neopixel=board.NEOPIXEL,
                    default_bg=cwd+"/revoke50.bmp",
                    text_font=cwd+"/fonts/AmaticSC-Bold-80.bdf",
                    text_position=(50, 80),
                    text_color=0xFFFFFF,
                    caption_text="#revokearticle50",
                    caption_font=cwd+"/fonts/AmaticSC-Bold-40.bdf",
                    caption_position=(50, 180),
                    caption_color=0xFFFFFF)


while True:
    try:
        sigs = pyportal.fetch()
        sigs = int(sigs)
        print("Signatures:", sigs)
    except RuntimeError as e:
        print("Some error occured, retrying! -", e)

    time.sleep(60)