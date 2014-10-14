# MAEC Output Framework

A framework for producing MAEC output from multiple tools at once. Given a binary file or an MD5, the framework will run a list of modules

## Usage

    python runtools.py <input file path or MD5> [--md5] [--verbose]
    
## Configuration

Per-module configuration and global configuration options can be set in `config.py`.

## Tool Interface

A conversion module may support any of the following methods used by the output framework:

  * `generate_package_from_binary_filepath` - given an filepath, the module returns a python-maec Pacakge object
  * `generate_package_from_md5` - given an MD5 string, the module returns a python-maec Pacakge object
  * `set_proxies` - optionally used to supply proxy information to the module; supplied as a dictionary like `{ "http": "http://example.com:80", ... }`
  * `set_api_key` - optionally used to supply API key information to the module
  
If the framework attempts a particular operation, and the module does not support the particular method required for that operation, the module will simply be skipped for that operation.
