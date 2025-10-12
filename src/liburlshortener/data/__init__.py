from libutil.engines import get_engine

engine_url_shortener = get_engine('url_shortener')

from . import models
