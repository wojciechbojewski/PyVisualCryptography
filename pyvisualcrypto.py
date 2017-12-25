import PyHador.Files
import PyHador.Crypthography

import argparse

parser = parser = argparse.ArgumentParser()
parser.add_argument('--filename')
args = parser.parse_args()

try:
    if args.filename:
        f = PyHador.Files.File(args.filename)
        crypt = PyHador.Crypthography.BitmapCryptography(f)
        crypt.Save()
    else:
        parser.print_help()    
except:
    parser.print_help()    
    