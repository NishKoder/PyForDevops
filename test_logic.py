from mylib.logic import wiki


def test_wiki():
    assert "Python" in wiki("Python", 2)
