"""
Student: Elon Hadad
Assignment no. 3
Program: python_words.py
"""
import keyword


def remove_from_string(s, start, end):
    """receives a string s and two substring (start,end) and returns the resulting string
    from 's' after deleting all the sub-strings from it starting at the end and ending at the end."""

    for i in range(0, len(s)):
        start_s = start
        end_s = end
        for ele in s:
            index_s = s.find(start_s)
            index_e = s.find(end_s)
            if ele == s[index_s]:
                d = s[index_s:index_e + 1]
                s = s.replace(d, "")
    return s


def split_all(s, str_lst):
    """Receives s string and list of python words and returns a list of strings"""
    
    for value in str_lst:
        s_split = s.split(value)
        s = "".join(s_split)
    return s.split()


def main():
    try:
        f = open('my_prog.py', 'r')
        s = f.read()
        f.close()
        start = '"'
        end = '"'
        str_lst = ["!", ".", ")", "(", ",", "==", ":", "^", "<", ">", "*", "_", "+", "-", ";", "#", "%", "[", "]"]
        keywordlist = keyword.kwlist
        new_str = remove_from_string(s, start, end)
        start_2 = '#'
        end_2 = '\n'
        new_str_2 = remove_from_string(new_str, start_2, end_2)
        w_lst = split_all(new_str_2, str_lst)

        for value in keywordlist:
            x = w_lst.count(value)
            if x > 0:
                print(f"{value:6} : {x}")

    except FileNotFoundError:
        print('File not found')


if __name__ == '__main__':
    main()
