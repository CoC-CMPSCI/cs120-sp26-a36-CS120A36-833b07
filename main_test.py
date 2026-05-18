import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # student female cs -> factor=3.0, amount=30000.00
    content = open('result1.txt').read()
    print(content)
    regex_test([r'\b3\.0', r'\b30000\b'], content)

@pytest.mark.T2
def test_main_2():
    # student male cs -> factor=2.0, amount=20000.00
    content = open('result2.txt').read()
    print(content)
    regex_test([r'\b2\.0', r'\b20000\b'], content)

@pytest.mark.T3
def test_main_3():
    # student female other -> factor=1.0, amount=10000.00
    content = open('result3.txt').read()
    print(content)
    regex_test([r'\b1\.0', r'\b10000\b'], content)

@pytest.mark.T4
def test_main_4():
    # nonstudent male other -> factor=0.1, amount=1000.00
    content = open('result4.txt').read()
    print(content)
    regex_test([r'\b0\.1', r'\b1000\b'], content)
