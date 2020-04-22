from typing import Sequence, TypeVar
import ntpath


def path_leaf(path: str) -> str:
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def isNumber(x) -> bool:
    try:
        return bool(0 == x * 0)  # multiply by zero should be zero
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


T = TypeVar('ITEM')  # Declare type variable


def filter_by_id(items: [T], item_id: str) -> T:
    for i in items:
        if hasattr(i, 'id'):
            if i.id == item_id:
                return i
        elif hasattr(i, "_id"):
            if i._id == item_id:
                return i
        else:
            raise ValueError("Item had no attribute _id or id")

    # we got here, means none of them had the id
    print(f'Warning: Item with id {item_id} was not found.')
    return None
