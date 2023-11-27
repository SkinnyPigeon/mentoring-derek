from binary_tree import BinaryTree

def test_insert():
    app = BinaryTree()
    app.insert(1, 'a')
    app.insert(2, 'b')
    app.insert(3, 'c')
    app.insert(-1, 'd')
    app.insert(-1, 'e')

    assert app.search(1) == 'a'
    assert app.search(2) == 'b'
    assert app.search(3) == 'c'
    assert app.search(-1) == 'e'
    assert app.search(0) == None

def test_delete():
    app = BinaryTree()
    app.insert(1, 'a')
    app.insert(2, 'b')
    app.insert(3, 'c')
    app.insert(-1, 'd')
    app.insert(-1, 'e')
    

    app.delete(1)
    assert app.search(1) == None
    assert app.search(2) == 'b'
    assert app.search(3) == 'c'
    assert app.search(-1) == 'e'
    assert app.search(0) == None

    app.delete(2)
    assert app.search(1) == None
    assert app.search(2) == None
    assert app.search(3) == 'c'
    assert app.search(-1) == 'e'
    assert app.search(0) == None

    app.delete(3)
    assert app.search(1) == None
    assert app.search(2) == None
    assert app.search(3) == None
    assert app.search(-1) == 'e'
    assert app.search(0) == None

    app.delete(-1)
    assert app.search(1) == None
    assert app.search(2) == None
    assert app.search(3) == None
    assert app.search(-1) == None
    assert app.search(0) == None

    app.delete(0)
    assert app.search(1) == None
    assert app.search(2) == None
    assert app.search(3) == None
    assert app.search(-1) == None
    assert app.search(0) == None
