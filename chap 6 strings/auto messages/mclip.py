#! python3
# mclip.py - A multi-clipboard program

TEXT = {'login': """Hi, All,
        
Logging in.
        
Thank you,""",

'logout': """Hi, All,
        
Logging out. DAR is attached.
        
Thank you,""",
        
'complete': """Hi, All,
        
This is completed.

PMW Path:""",

'reel': """Hi, All,
        
Reel 01 is attached.

PMW Path:""",

'template': """Hi, All,
        
Template files and loadables attached.

PMW Path:"""}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [insert keyphrase here] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]     # first command like arg is keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard')
else:
    print('There is no text for ' + keyphrase)