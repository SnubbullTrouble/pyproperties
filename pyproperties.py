import os
import toml

#decorator that turns each field into a class property and assigns each one a getter
def propertygetter(cls):
    for x in cls.properties:
        getter = lambda self, x=x: self.properties[x]
        setattr(cls, "{}".format(x), property(getter))
    return cls

@propertygetter
class PyProperties(object):
    properties_file = ".properties.toml"
    properties = toml.load(properties_file)["Properties"] if os.path.exists(properties_file) else None

    def get_properties(self):
        return self.properties

    def write_properties(self, dict):
        with open(self.properties_file, 'w') as file:
            toml.dump({"Properties": dict}, file)
