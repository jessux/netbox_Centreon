from extras.plugins import PluginConfig

class CentreonSoundsConfig(PluginConfig):
    name = 'netbox_Centreon'
    verbose_name = 'Centreon'
    description = 'An example plugin for development purposes'
    version = '0.1'
    author = 'Gabriel KAHLOUCHE'
    author_email = 'gabriel.kahlouche@groupama.com'
    base_url = 'Centreon'
    required_settings = []
    default_settings = {
        'centreon_url': "digsflrp1k.dig.intra.groupama.fr"
    }

config = CentreonSoundsConfig