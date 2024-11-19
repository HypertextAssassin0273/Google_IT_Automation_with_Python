#!/usr/bin/env python3

def validate_user(username, minlen):
    assert type(username) == str, "Error: username must be a string"

    if minlen < 1:
        raise ValueError("Error: min. length must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    
    return True


# test-cases (manual testing):
if __name__ == "__main__":
    try:
        validate_user("", -1)         # fail
        # validate_user("", 1)          # pass
        # validate_user("myuser", 1)    # pass
        # validate_user(88, 1)          # fail
        # validate_user([], 1)          # fail
        # validate_user(["name"], 1)    # fail

    except Exception as e: # catches all exceptions
        print(e)
