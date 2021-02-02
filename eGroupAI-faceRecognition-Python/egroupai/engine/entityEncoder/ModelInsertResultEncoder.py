import json

from egroupai.engine.entity.ModelInsertResult import ModelInsertResult


class ModelInsertResultEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ModelInsertResult):
            return obj.to_dict()
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
