def urljoin(*args):
    if len(args) > 2:
        args = (
            args[0].rstrip('/'),
            '/'.join(s.strip('/') for s in args[1:-1]),
            args[-1].lstrip('/')
        )
    return '/'.join(args)
