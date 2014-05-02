from .premailer import Premailer, transform

__version__ = '2.1.0'

def get_version(full=False):
    """
    Returns a string-ified version number.

    Optionally accepts a ``full`` parameter, which if ``True``, will include
    any pre-release information. (Default: ``False``)
    """
    version = '.'.join([str(bit) for bit in __version__[:3]])

    if full:
        version = '-'.join([version] + list(__version__[3:]))

    return version
