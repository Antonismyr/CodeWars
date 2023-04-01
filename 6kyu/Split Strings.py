def solution(s):
    return [s[i-2:i] if len(s[i-2:i]) == 2 else s[i-2:i] + '_' for i in range(2, len(s)+2, 2)]