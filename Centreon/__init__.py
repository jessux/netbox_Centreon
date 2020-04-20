from extras.plugins import PluginConfig

class CentreonConfig(PluginConfig):
    name = 'netbox_centreon'
    verbose_name = 'Centreon'
    description = 'A plugin for Centreon'
    version = '0.1'
    author = 'Gabriel KAHLOUCHE'
    author_email = 'gabriel.kahlouche@gmail.com'
    base_url = 'centreon'
    required_settings = []
    default_settings = {    }

config = CentreonConfig