import sys
path = '/home/ben/mysite/FeatureRequestApp'
if path not in sys.path:
   sys.path.insert(0, path)

from feature_app import app as application