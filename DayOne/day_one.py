from typing import List, Tuple

def get_left_and_right_line(file_name: str) -> Tuple[List[int], List[int]]:
    """
    Get the left and right line from the input file.
    """
    left_line = []
    right_line = []
    with open(file_name) as input:
        lines = input.readlines()
        
        for line in lines:
            line = line.strip()
            split_line = line.split('   ')
            left_line.append(int(split_line[0]))
            right_line.append(int(split_line[1]))

    return left_line, right_line


def get_total_distance(left_line: List[int], right_line: List[int]) -> int:
    """
    Get the total distance of the two lines.
    """
    total_distance = 0

    while len(left_line) > 0:
        smallest_left = min(left_line)
        smallest_right = min(right_line)

        if smallest_left <= smallest_right:
            total_distance += smallest_right - smallest_left
        else:
            total_distance += smallest_left - smallest_right
    
        left_line.remove(smallest_left)
        right_line.remove(smallest_right)
    return total_distance

def get_the_similarity_score(left_line: List[int], right_line: List[int]) -> int:
    """
    Get the similarity score of the two lines by counting how many left number is occuring on right line.
    """
    similarity_score = 0

    for left_number in left_line:
        left_number_count_in_right_line = right_line.count(left_number)
        similarity_score += left_number * left_number_count_in_right_line

    return similarity_score
