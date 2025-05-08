import filecmp
import os


def create_test_files():
    with open('file1.txt', 'w') as f:
        f.write("Hello, World!\nThis is a test file.")

    with open('file2.txt', 'w') as f:
        f.write("Hello, World!\nThis is a test file.")

    with open('file3.txt', 'w') as f:
        f.write("Hello, World!\nThis is a different test file.")


def remove_test_files():
    os.remove('file1.txt')
    os.remove('file2.txt')
    os.remove('file3.txt')


def test_files_are_identical():
    create_test_files()
    result = filecmp.cmp('file1.txt', 'file2.txt', shallow=False)
    assert result
    remove_test_files()


def test_files_are_different():
    create_test_files()
    result = filecmp.cmp('file1.txt', 'file3.txt', shallow=False)
    assert not result
    remove_test_files()


def test_file_size_comparison():
    create_test_files()
    size1 = os.path.getsize('file1.txt')
    size2 = os.path.getsize('file2.txt')
    assert size1 == size2
    remove_test_files()


def test_file_content_comparison():
    create_test_files()
    with open('file1.txt') as f1, open('file2.txt') as f2:
        content1 = f1.read()
        content2 = f2.read()
        assert content1 == content2
    remove_test_files()


if __name__ == '__main__':
    test_files_are_identical()
    test_files_are_different()
    test_file_size_comparison()
    test_file_content_comparison()

