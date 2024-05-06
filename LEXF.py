import rosalind
import re


def translate(alphabet, string):
    ret = ''
    for i in range(len(string)):
        ret = ret + alphabet[int(string[i])]
    return (ret)

def LexicographicallyPrint(string, n):
    # 가능한 최대 숫자 계산
    digit = len(string)
    max_number = digit**n
    # 0부터 max_number까지 모든 숫자에 대해
    for num in range(max_number):
        # 숫자를 n진수로 변환하고, zfill()로 앞쪽을 '0'으로 채워 k자리수를 맞춤
        num_in_base_digit = ''
        temp = num
        while temp > 0:
            num_in_base_digit = str(temp % digit) + num_in_base_digit
            temp //= digit
        # 남은 자릿수를 0으로 채우기
        num_in_base_digit = num_in_base_digit.zfill(n)

        # 숫자를 출력
        print(translate(string, num_in_base_digit))
