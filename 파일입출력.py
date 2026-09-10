""" file=open("test.txt","w",encoding="utf-8")
file.write("안녕하세요")
file.close() """



""" while True:
	memo=input("메모를 입력하세요. 종료하려면 q 입력: ").strip()

	if memo.lower()=="q":
		break
	
	with open("memo.txt","a",encoding="utf-8")as file:
		file.write(memo+"\n")
	
	print("메모 저장이 완료되었습니다.") """



""" import os

d = os.getcwd

print(d) """



import os

if os.path.exists("ranking.txt"):
    print("랭킹 파일이 있습니다.")
else:
    print("랭킹 파일이 없습니다.")