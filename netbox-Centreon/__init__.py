from extras.plugins import PluginConfig

class CentreonConfig(PluginConfig):
    name = 'netbox-Centreon'
    verbose_name = 'netbox-Centreon'
    description = 'A plugin for Centreon'
    version = '0.1'
    author = 'Gabriel KAHLOUCHE'
    author_email = 'gabriel.kahlouche@gmail.com'
    base_url = 'netbox-Centreon'
    required_settings = []
    default_settings = {    }

config = CentreonConfig