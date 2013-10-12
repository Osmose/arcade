# Settings that are only active while tests are being run.

# Arguments to pass to nose when running tests.
NOSE_ARGS = ['--logging-clear-handlers', '--logging-filter=-factory,-south,-django_browserid']
