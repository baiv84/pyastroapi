from common.basicfunc import get_file_name


def test_filename_extraction():
    """Test file extraction """
    assert ('hello world.txt') == get_file_name("https://example.com/txt/hello%20world.txt?v=9#python")
    assert ('Поездка в Париж.txt') == get_file_name("https://example.com/txt/Поездка%20в%20Париж.txt?type=plane")
