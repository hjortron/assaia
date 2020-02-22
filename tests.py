from main import BattleshipBoard


# import pytest


def test_has_neighbors_false():
    test_board = BattleshipBoard(name='test')
    test_board.board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

    assert test_board.has_neighbors(x=1, y=1) is False


def test_has_neighbors_true_00():
    test_board = BattleshipBoard(name='test')
    test_board.board = [
        ['=', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

    assert test_board.has_neighbors(x=1, y=1) is True


def test_has_neighbors_true_01():
    test_board = BattleshipBoard(name='test')
    test_board.board = [
        [' ', '=', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

    assert test_board.has_neighbors(x=1, y=1) is True


def test_has_neighbors_true_02():
    test_board = BattleshipBoard(name='test')
    test_board.board = [
        [' ', ' ', '='],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

    assert test_board.has_neighbors(x=1, y=1) is True


def test_has_neighbors_true_10():
    test_board = BattleshipBoard(name='test')
    test_board.board = [
        [' ', ' ', ' '],
        ['=', ' ', ' '],
        [' ', ' ', ' '],
    ]

    assert test_board.has_neighbors(x=1, y=1) is True


def test_has_neighbors_true_11():
    test_board = BattleshipBoard(name='test')
    test_board.board = [
        [' ', ' ', ' '],
        [' ', '=', ' '],
        [' ', ' ', ' '],
    ]

    assert test_board.has_neighbors(x=1, y=1) is True


def test_has_neighbors_true_12():
    test_board = BattleshipBoard(name='test')
    test_board.board = [
        [' ', ' ', ' '],
        [' ', ' ', '='],
        [' ', ' ', ' '],
    ]

    assert test_board.has_neighbors(x=1, y=1) is True


def test_has_neighbors_true_20():
    test_board = BattleshipBoard(name='test')
    test_board.board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        ['=', ' ', ' '],
    ]

    assert test_board.has_neighbors(x=1, y=1) is True


def test_has_neighbors_true_21():
    test_board = BattleshipBoard(name='test')
    test_board.board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', '=', ' '],
    ]

    assert test_board.has_neighbors(x=1, y=1) is True


def test_has_neighbors_true_22():
    test_board = BattleshipBoard(name='test')
    test_board.board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', '='],
    ]

    assert test_board.has_neighbors(x=1, y=1) is True
