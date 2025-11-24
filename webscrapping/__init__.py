# Source - https://stackoverflow.com/a
# Posted by zmo, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-24, License - CC BY-SA 3.0

#!/usr/bin/env python
import os, pkgutil
__all__ = list(module for _, module, _ in pkgutil.iter_modules([os.path.dirname(__file__)]))
