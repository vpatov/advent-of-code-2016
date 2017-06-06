from collections import Counter
import operator

rooms = open('test4.txt','r').read().split('\n')

def is_real(room):
    cnt = Counter()
    encrypted = room[:room.index('[') - 3]
    sector_id = int(room[room.index('[') - 3 : room.index('[')])
    checksum = room[room.index('[') + 1: -1]
    for ch in encrypted:
        if ch == '-':
            continue
        if ch.isalpha():
            cnt[ch] += 1
    i = 0
    letters = sorted(cnt.items(), key=lambda x: (x[1],x[0]),reverse=False)
    #sorted(y.items(), key=lambda x: (x[1],x[0]), reverse=True)

    while (i < 5 and i < len(cnt)):
        if letters[i][0] != checksum[i]:
            print letters[i][0],checksum[i]
            print letters, checksum
            return False
        i+=1
    return sector_id

print sum([is_real(room) for room in rooms])

