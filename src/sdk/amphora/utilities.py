import ntpath

def path_leaf(path: str) -> str:
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def isNumber(x) -> bool:
    try:
        return bool(0 == x*0) # multiply by zero should be zero
    except:
        return False

def isString(x) -> bool:
    return isinstance(x, str)

def infer_value_type_from_value(value) -> str:
    if isNumber(value):
        return "Numeric"
    elif isString(value):
        return "String"
    else:
        return None