import sys, logging

class Whitelist(logging.Filter):
    def __init__(self, *whitelist):
        self.whitelist = [logging.Filter(name) for name in whitelist]

    def filter(self, record):
        return any(f.filter(record) for f in self.whitelist)

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)-8s %(message)s'
)
for handler in logging.root.handlers:
    handler.addFilter(Whitelist('root'))

logger = logging
