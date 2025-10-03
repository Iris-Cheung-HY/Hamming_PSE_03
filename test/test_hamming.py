from main.hamming import hamming_distance
import pytest

# example input 1:
# expected output 1:

# example input 2:
# expected output 2:

def test_hamming_distance_normal_output():
    # ^rename with meaningful test name
    # and complete test implementation below
    # arrange
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "CATCGTAATGACGGCCT"

    # act
    result = hamming_distance(strand1, strand2)

    # assert
    assert result == 7
    
# def test_character_not_in_list():
#     # ^rename with meaningful test name
#     # and complete test implementation below
    
#     strand1 = "GAGCCTACTAACGGGAT"
#     strand2 = "CATCGTAATGACGGCUT"

#     # act
#     result = hamming_distance(strand1, strand2)

#     # assert
#     with pytest.raises(ValueError):
#         hamming_distance(strand1, strand2)
    
def test_not_the_same_length():
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "CATCGTAATGAC"

    # act
    # assert
    with pytest.raises(ValueError):
        hamming_distance(strand1, strand2)  
    

