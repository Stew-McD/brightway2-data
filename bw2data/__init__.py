# -*- coding: utf-8 -*
__version__ = (2, 0, "dev")

from ._config import config
from .utils import set_data_dir, bw2setup, safe_save
from .meta import databases, methods, mapping, reset_meta, geomapping, \
    weightings, normalizations
from .serialization import JsonWrapper
from .database import DatabaseChooser as Database
from .data_store import DataStore
from .method import Method
from .proxies.activity import Activity
from .proxies.exchange import Exchange
from .search import Searcher, IndexManager
from .weighting_normalization import Weighting, Normalization
from .query import Query, Filter, Result
from .revisions import RevisionsInterface
# Don't confuse nose tests
from .updates import Updates

Updates.check_status()

# Print only warning messages
from .colors import Fore
import warnings


def warning_message(message, *args, **kwargs):
    return Fore.RED + "Warning: " + Fore.RESET + unicode(message).encode("utf8", "ignore") + "\n"

warnings.formatwarning = warning_message
