from collections import Counter


def getMarker(filename) -> int:
    curr_marker = []
    count = 0
    with open(filename) as f:
        message = f.read()
        for char in message:
            if len(curr_marker) == 4 and curr_marker[0] not in curr_marker[1:]\
                and curr_marker[1] not in curr_marker[2:] and curr_marker[2] != curr_marker[3]:
                    return count
            elif len(curr_marker) < 4:
                curr_marker.append(char)
                count +=1
            else:
                curr_marker[count % 4] = char
                count += 1


def smarterGetMarker(filename) -> int:
    curr_marker = []
    count = 0
    with open(filename) as f:
        message = f.read()
        for char in message:
            if len(curr_marker) < 14:
                curr_marker.append(char)
                count += 1
            elif len(curr_marker) == 14 and len(set(curr_marker)) == len(curr_marker):
                return count
            else:
                curr_marker[count % 14] = char
                count += 1

print(getMarker("DataInputs\Day6Data.txt"))


print(smarterGetMarker("DataInputs\Day6Data.txt"))