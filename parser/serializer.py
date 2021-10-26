import json
import os.path
import jsonSerializer



def define_path():
    abspath = os.path.abspath("")
    sys_path = os.path.join(abspath, "data", "data.json")
    return sys_path


def serialize(obj):
    serialization_path = define_path()
    data_dict = dict()
    if os.path.exists(serialization_path):
        with open(serialization_path, 'r') as json_file:
            try:
                data_dict = json.load(json_file)
            except Exception:
                pass
    data_dict.update(obj)
    with open(serialization_path, 'w') as json_file:
         json.dump(data_dict, json_file, cls=jsonSerializer.itemEncoder, indent=4)
