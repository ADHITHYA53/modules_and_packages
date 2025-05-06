def convert_number(value, base_from, base_to):
    """Convert between hex, dec, oct, and bin."""
    base_dict = {'bin': 2,'oct': 8,'dec': 10,'hex': 16}
    try:
        decimal_value = int(value, base_dict[base_from.lower()])
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


