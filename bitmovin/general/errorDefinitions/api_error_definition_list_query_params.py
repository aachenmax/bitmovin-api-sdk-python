
class ApiErrorDefinitionListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, *args, **kwargs):
        super(ApiErrorDefinitionListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit