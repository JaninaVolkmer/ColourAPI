#3rd party modules
import os
from flask import abort


# Data to serve with the API
PICTURES = {
    "Malachite": {
        "hex": "08BF49.png"
    },
    "PewterBlue": {
        "hex": "7EA0B5.png"
    },
    "Disco": {
        "hex": "9A183C.png"
    },
    "Spray": {
        "hex": "71F2D7.png"
    }
}

# Create a handler for the read (GET) people
def read_all():
    """
    Function responds to a request for /api/pictures
    with the comp[lete list of hex values
    : return: sorted list of hex
    """
    # Create the list of people from the data
    return [PICTURES[key] for key in sorted(PICTURES.keys())]

def read_one(hex):
    """
    This function responds to a request for /api/pictures/{hex}
    with one matching hexvalue from pictures

    :param hex: hex of hex-value to find
    :return:      colour matching hex
    """
    # Does the person exist in people?
    for hex in os.listdir('static/images'):
        if hex in PICTURES:
            hexval = PICTURES.get(hex)
    # otherwise, not found
        else:
            abort(
                404, "Colour with value {hex} not found".format(hex=hex)
        )
        return hexval
