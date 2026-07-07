"""
Retry helper.
"""

import time


def retry(
    func,
    retries=3,
    delay=1,
    exceptions=(Exception,),
):

    last_exception = None

    for attempt in range(retries):

        try:
            return func()

        except exceptions as e:

            last_exception = e

            if attempt < retries - 1:
                time.sleep(delay)

    raise last_exception