import json

from egroupai.engine.entity.TrainResult import TrainResult


class TrainResultEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, TrainResult):
            return obj.to_dict()
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
