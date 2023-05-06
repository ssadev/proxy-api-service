def endpoint_serializer(ep) -> dict:
    return {
        'id': str(ep["_id"]),
        'name': ep["endpoint"]
    }


def endpoints_serializer(eps) -> list:
    return [endpoint_serializer(ep) for ep in eps]
