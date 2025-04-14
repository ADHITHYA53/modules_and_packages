def convert_number(value, base_from, base_to):
    """Convert between hex, dec, oct, and bin."""
    base_dict = {
        'bin': 2,
        'oct': 8,
        'dec': 10,
        'hex': 16
    }
    try:
        # Convert input to decimal first
        decimal_value = int(value, base_dict[base_from.lower()])
        # Convert decimal to target base
        if base_to == 'bin':
            return bin(decimal_value)
        elif base_to == 'oct':
            return oct(decimal_value)
        elif base_to == 'dec':
            return str(decimal_value)
        elif base_to == 'hex':
            return hex(decimal_value)
        else:
            return "Invalid target base"
    except:
        return "Invalid number or base input."


def bitwise_operations(a, b=None, op="and"):
    """Perform bitwise operations: and, or, not, <<, >>"""
    try:
        a = int(a, 0)  # Accepts hex/bin/dec with prefixes like 0x, 0b
        if b is not None:
            b = int(b, 0)

        if op == "and":
            return bin(a & b)
        elif op == "or":
            return bin(a | b)
        elif op == "not":
            return bin(~a & 0xFFFFFFFF)  # limit to 32 bits
        elif op == "lshift":
            return bin(a << b)
        elif op == "rshift":
            return bin(a >> b)
        else:
            return "Invalid operation"
    except:
        return "Error in input or operation"
