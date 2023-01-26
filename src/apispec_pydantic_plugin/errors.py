class ApispecPydanticPluginError(Exception):
    pass


class ApiSpecPydanticPluginValueError(ValueError):
    pass


class ApiSpecPydanticPluginKeyError(KeyError):
    pass


class ModelNotFoundError(ApiSpecPydanticPluginKeyError):
    pass


class ResolverNotFound(ApiSpecPydanticPluginValueError):
    pass
