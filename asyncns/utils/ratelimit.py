import time


class Limiter:
    """
    Rate limiter class for API interactions.

    Not thread safe.
    """

    def __init__(self, limit, interval):
        self.limit = limit
        self.interval = interval
        self.reset_time = time.time()
        self.count = 0

    def __call__(self, func):
        """
        Decorator for rate limiting.
        """
        def wrapper(*args, **kwargs):
            if self.count < self.limit:
                self.count += 1
                return func(*args, **kwargs)
            else:
                if time.time() - self.reset_time > self.interval:
                    self.reset_time = time.time()
                    self.count = 0
                    return func(*args, **kwargs)
                else:
                    return None
        return wrapper

    def reset(self):
        """
        Reset method for the limiter.
        """
        self.count = 0
        self.reset_time = time.time()

    def __repr__(self):
        return f"<Limiter limit={self.limit} interval={self.interval} count={self.count}>"

    def __str__(self):
        return f"<Limiter limit={self.limit} interval={self.interval} count={self.count}>"


