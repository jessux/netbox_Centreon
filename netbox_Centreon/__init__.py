from extras.plugins import PluginConfig

class CentreonConfig(PluginConfig):
    name = 'netbox_Centreon'
    verbose_name = 'netbox Centreon'
    description = 'A plugin for Centreon'
    version = '0.1'
    author = 'Gabriel KAHLOUCHE'
    author_email = 'gabriel.kahlouche@gmail.com'
    base_url = 'centreon'
    required_settings = ["centreon_url"]
    default_settings = {
        'sync_type' : "async"
    }

config = CentreonConfig