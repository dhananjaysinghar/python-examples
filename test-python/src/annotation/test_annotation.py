import functools


# Define the log decorator
def log(func):
    @functools.wraps(func)  # Preserve the original function's metadata
    def wrapper(*args, **kwargs):
        # Log function input
        print(f"Calling {func.__name__} with args={args} and kwargs={kwargs}")

        # Call the original function
        result = func(*args, **kwargs)

        # Log function output
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


# Example usage
@log
def add(a: int, b: int) -> int:
    return a + b


# Test the decorated functions
if __name__ == "__main__":
    add_result = add(10, 20)
