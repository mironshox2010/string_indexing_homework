def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    s_count = 0
    if s[0].isdigit():
        s_count += 1
    if s[1].isdigit():
        s_count += 1
    if s[2].isdigit():
        s_count += 1
    if s[3].isdigit():
        s_count += 1
    if s[4].isdigit():
        s_count += 1
    return s_count
print(main("56567"))
    