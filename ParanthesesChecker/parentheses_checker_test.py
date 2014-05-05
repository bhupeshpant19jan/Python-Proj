# TEST CASES for the blanced expression checker
from parentheses_checker import check_balanced_parentheses

#INVALID SCENARIOS
def test_testcase1():
    test_string = "abc{def}ghi(jkl)mno[pqr]"
    assert(check_balanced_parentheses(test_string))

def test_testcase2():
    test_string = "a{([b])}"
    assert(check_balanced_parentheses(test_string))

def test_testcase3():
    test_string = ""
    assert(check_balanced_parentheses(test_string))

def test_testcase4():
    test_string = "{{{{{{}}}}}}"
    assert(check_balanced_parentheses(test_string))

def test_testcase5():
    test_string = "[][][]()()(){}{}{}"
    assert(check_balanced_parentheses(test_string))

def test_testcase12():
    test_string = "abc{def}"
    assert(check_balanced_parentheses(test_string))

def test_testcase14():
    test_string = "111[]abc{()}def"
    assert(check_balanced_parentheses(test_string))


#INVALID SCENARIOS
def test_testcase6():
    test_string = "abc{(def})"
    assert(not check_balanced_parentheses(test_string))

def test_testcase7():
    test_string = "ab[c)"
    assert(not check_balanced_parentheses(test_string))

def test_testcase8():
    test_string = "abc}def{"
    assert(not check_balanced_parentheses(test_string))

def test_testcase9():
    test_string = "{"
    assert(not check_balanced_parentheses(test_string))

def test_testcase10():
    test_string = "{{{{{{{{{{{{{"
    assert(not check_balanced_parentheses(test_string))

def test_testcase11():
    test_string = "}}}}}}}}}}"
    assert(not check_balanced_parentheses(test_string))

def test_testcase13():
    test_string = "abc{d[efg}]hl123"
    assert(not check_balanced_parentheses(test_string))

def test_testcase15():
    test_string = "abc{}[]())"
    assert(not check_balanced_parentheses(test_string))


test_testcase1()
test_testcase2()
test_testcase3()
test_testcase4()
test_testcase5()
test_testcase6()
test_testcase7()
test_testcase8()
test_testcase9()
test_testcase10()
test_testcase11()
test_testcase12()
test_testcase13()
test_testcase14()
test_testcase15()


