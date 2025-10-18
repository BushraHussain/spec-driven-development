def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
        
    Returns:
        The sum of a and b
        
    Raises:
        TypeError: If either argument is not a number
    """
    # Check if both arguments are numbers (int or float) but not booleans
    # In Python, bool is a subclass of int, so we need to check for bool separately
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError(f"Boolean values are not allowed, got {type(a).__name__} and {type(b).__name__}")
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both arguments must be numbers (int or float), got {type(a).__name__} and {type(b).__name__}")
    
    return a + b