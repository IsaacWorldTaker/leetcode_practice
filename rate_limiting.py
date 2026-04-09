"""
This function tracks how many times a user has called a function within a fix window and raises an exception if the user has exceeded the limit.
Assumptions:
- User Id is passed as an argument to the function
- Single threadeed environment so race conditions are not handled in this implementation
- the call list should be defined in sth like redis to be shared across multiple systems. Since we are implementing a single-threaded example, we are using a global variable to store the call count.
"""

from collections import deque
from typing import Callable
import time

# user_id: [timestamp1, timestamp2, ...]


def remove_old_timestamps(call_list, time):
    while call_list and time - call_list[0] > 60:
        call_list.popleft()


def rate_limit(limit):

    call_count = {}

    def decorator_func(func: Callable):
        def wrapper(*args, **kwargs):
            user_id = kwargs.get("user_id")
            if user_id is None:
                raise Exception("User Id is required")
            now = time.time()

            if user_id not in call_count:
                call_count[user_id] = deque()

            remove_old_timestamps(call_count[user_id], now)
            if len(call_count[user_id]) >= limit:
                raise Exception("Rate limit exceeded. wait for another {} seconds".format(
                    60-(now-call_count[user_id][0])))
            call_count[user_id].append(now)
            return func(*args, **kwargs)

        return wrapper
    return decorator_func


@rate_limit(3)
def test_function(user_id: int):
    print(f"Function called by user {user_id}")


test_function(user_id=1)
