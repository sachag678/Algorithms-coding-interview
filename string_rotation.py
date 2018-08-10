"""Cracking the Coding Interview: Chapter 1 problem 1.9."""


def is_substring(s1, s2):
    """Check if s2 is a substring of s1."""
    val = s1.find(s2)
    if val == -1:
        return False
    else:
        return True


def is_rotation(s1, s2):
    """Check if s2 reversed is a substring of s1."""
    if len(s1) == len(s2):
        return is_substring(s1, s2[::-1])
    else:
        return False

if __name__ == '__main__':

    w1 = 'waterbottle'
    w2 = 'retawf'

    print(is_rotation(w1, w2))
