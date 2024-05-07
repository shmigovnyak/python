from merge_and_write import merge_and_write
import pytest
@pytest.mark.parametrize(
        "file1, file2, output, result",
        [
            ("./3.txt","./12.txt","./out.txt","Один из файлов не найден"),
        ]
)
def test_merge_and_write(file1, file2, output, result):
    assert merge_and_write(file1, file2, output) == result