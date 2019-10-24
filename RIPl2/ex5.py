from time import sleep
from librip.ctxmngrs import timer

# with timer():
#    sleep(5.5)

@timer
def	good():
	import time
	time.sleep(5.5)

good()
