
def all_longer_than(obj: Union[str, List], n:int) -> bool:
    def helper(obj: list, n: int):
        for item in obj:

            if type(item) == list:
                helper(item, n)
            else:
                if len(item) < n:
                    return False

    result = helper(obj, n)
    
    if result == False:
        return result

    return True