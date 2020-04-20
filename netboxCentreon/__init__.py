from extras.plugins import PluginConfig

class CentreonConfig(PluginConfig):
    name = 'netboxCentreon'
    verbose_name = 'netboxCentreon'
    description = 'A plugin for Centreon'
    version = '0.1'
    author = 'Gabriel KAHLOUCHE'
    author_email = 'gabriel.kahlouche@gmail.com'
    base_url = 'netboxCentreon'
    required_settings = []
    default_settings = {    }

config = CentreonConfig