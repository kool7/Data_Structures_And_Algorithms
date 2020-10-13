# if __name__ == "__main__":
#     n = int(input())
#     phonebook = {}

#     for _ in range(n):
#         name, number = map(str, input().split())
#         phonebook[name] = number

#     while True:
#         try:
#             query = input()

#             if query in phonebook:
#                 number = phonebook[query]
#                 print(query + "=" + number)
#             else:
#                 print("Not found")
#         except:
#             break

def anagramDistance(s1, s2):
    count = 0
    char_count = [0] * 26
    for i in range(26):
        char_count[i] = 0
        
    for i in range(len( s1)):  
        char_count[ord(s1[i]) - ord('a')] += 1
        
    for i in range(len(s2)):  
        char_count[ord(s2[i]) - ord('a')] -= 1
        if (char_count[ord(s2[i]) - 
                       ord('a')] < 0) : 
            count += 1
  
    return count

if __name__ == '__main__' :
    n = int(input())
    for _ in range(n):
        s1, s2 = map(str, input().rstrip().split())
        print(anagramDistance(s1, s2))



