import inspect
import os
from typing import Any, Optional
import tomlkit

class PyProperties(object):
    properties_file = ".properties.toml"
    properties_group = "Properties"
    properties = {}

    def __init__(self, file_location: str = os.getcwd()):
        self.properties_file = '/'.join([file_location.replace('\\', '/'), self.properties_file])
        self.properties = tomlkit.load(open(self.properties_file))[self.properties_group] if os.path.exists(self.properties_file) else {}

    def __getattr__(self, __name: str) -> Optional[str]:
        if __name in ["properties_file", "properties_group", "poperties"]:
            return super(PyProperties, self).__getattribute__(__name)
        elif __name in self.properties.keys():
            return self.properties[__name]
        else:
            return None
        
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ["properties_file", "properties_group", "properties"]:
            super(PyProperties, self).__setattr__(__name)
        else:
            self.properties[__name] = str(__value)

    def write_properties(self):
        if len(self.properties) > 0:
            with open(self.properties_file, 'w') as file:
                tomlkit.dump({self.properties_group: self.properties}, file)