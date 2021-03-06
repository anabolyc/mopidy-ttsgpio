from __future__ import unicode_literals

import logging
import os

from mopidy import config, ext



__version__ = '1.0.1'


logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = 'Mopidy-TtsGpio-opi'
    ext_name = 'ttsgpio-opi'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['debug_gpio_simulate'] = config.Boolean()
        schema['pin_play_led'] = config.String()
        schema['inverted'] = config.Boolean()
        return schema

    def setup(self, registry):

        from .frontend import TtsGpioOpi
        registry.add('frontend', TtsGpioOpi)
