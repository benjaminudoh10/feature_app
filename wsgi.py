import sys
path = '/home/benjaminudoh10/feature_app'
if path not in sys.path:
   sys.path.insert(0, path)

from feature_app import app as application
