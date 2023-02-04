from basic import get_file_extension


def test_filename_extraction():
    """Test file extraction """
    assert ('.txt') == get_file_extension("https://example.com/txt/hello%20world.txt?v=9#python")
    assert ('.jpg') == get_file_extension("https://example.com/txt/Поездка%20в%20Париж.jpg?type=plane")
