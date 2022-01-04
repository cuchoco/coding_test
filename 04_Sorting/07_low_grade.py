# 성적이 낮은 순서대로
def sort(data):
 
    return sorted(data, key= lambda x : x[-1])

data = [('홍길동', 95), ('이순신', 77)]

print(sort(data))