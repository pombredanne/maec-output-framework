"""
Configuration data for modules used by the framework
"""

from maec.misc.options import ScriptOptions

modules = [
    {
        "import_path":"threatexpert_to_maec",
        "options": {
                    "deduplicate_bundles": True,
                    "dereference_bundles": True,
                    "normalize_bundles": True
        }
    },
    {
        "import_path":"virustotal_to_maec",
        "options": {
                    "deduplicate_bundles": True,
                    "dereference_bundles": True,
                    "normalize_bundles": True
        },
        "api_key":"REPLACE THIS STRING WITH AN API KEY FROM https://www.virustotal.com"
    },
    {
        "import_path":"pefile_to_maec",
        "options": {
                    "deduplicate_bundles": True,
                    "dereference_bundles": True,
                    "normalize_bundles": True
        }
    },
]

global_config = {
    "proxies": {
        #"http":"http://example.com:80",
        #"https":"http://example.com:80"
    }
}

# turn options dicts into ScriptOptions objects
for module in modules:
    options_object = ScriptOptions()
    options_dict = module['options']
    options_object.deduplicate_bundles = options_dict['deduplicate_bundles']
    options_object.dereference_bundles = options_dict['dereference_bundles']
    options_object.normalize_bundles = options_dict['normalize_bundles']
    module['options'] = options_object

