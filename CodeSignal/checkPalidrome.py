#my solution
def solution(inputString):
    reversedString=inputString[::-1]
    if inputString==reversedString:
        return True
    else:
        return False
    
#top solution
def solution(inputString):
    return inputString == inputString[::-1]