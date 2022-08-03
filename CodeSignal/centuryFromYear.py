from re import I


def solution(year):
    i=0
    while year>0:
        year=year-100
        i=i+1 
    print(i)
    #return i
year=1700
solution(year)