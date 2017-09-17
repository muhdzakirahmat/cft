from unit6 import create_app
from unit6.utils import import_ctf

import zipfile
import sys

app = create_app()
with app.app_context():
    import_ctf(sys.argv[1])
