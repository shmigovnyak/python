from merge_and_write import merge_and_write
import pytest
@pytest.mark.parametrize(
        "file_1, file_2, file_3, shmiga",
        [
            ("./3.txt","./12.txt","./out.txt","Один из файлов не найден"),
        ]
)
def test_merge_and_write(file_1, file_2, file_3, shmiga):
    assert merge_and_write(file_1, file_2, file_3) == shmiga