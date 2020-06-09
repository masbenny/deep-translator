"""Top-level package for deep_translator."""
from .google_trans import GoogleTranslator
from .pons import PonsTranslator
# import exceptions

__author__ = """Nidhal Baccouri"""
__email__ = 'nidhalbacc@gmail.com'
__version__ = '0.1.2'

__all__ = [GoogleTranslator, PonsTranslator]
