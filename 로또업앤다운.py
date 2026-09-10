import random

ranking = []
while True:
    aw = int(input("1번 누르면 모드 선택, 2번 누르면 랭킹보기, 3번 누르면 종료 : "))

    if aw == 1:
        mo = int(input("1번 로또번호 추출기 2번 업앤다운 3. 프로그램 종료 : "))

        if mo == 1:
            lo = random.sample(range(1, 45), 6)
            lo.sort()
            print(*lo, end=' ')
            print()

        elif mo == 2:
            key = 0
            while True:
                i = int(input("1번 이름 입력 2번 사용 종료 : "))
                if i == 1:
                    key = input("이름을 입력하세요. : ")
                    break
                elif i == 2:
                    print("사용종료")
                    break

            if key:
                count = 0
                i = int(input("난이도를 설정하세요. 1. 쉬움 2. 중간 3. 어려움 : "))

            if i == 1:
                max_num = 10
            elif i == 2:
                max_num = 50
            else:   
                max_num = 100

            game = random.randint(1, max_num)

            while True:
                    aw2 = int(input(f"업앤다운 게임 숫자를 입력하세요(1~{max_num}) : "))
                    count += 1

                    if game == aw2:
                        print("정답입니다!")
                        break
                    elif game < aw2:
                        print("숫자가 높습니다.")
                    else:
                        print("숫자가 낮습니다.")

            print(f"시도 횟수 {count}번")

            user = {}
            user["name"] = key
            user["value"] = count
            print(user)

            ranking.append(user)
    elif mo == 3:
        print("사용종료")
    elif aw == 2:
        if not ranking:
            print("아직 랭킹 기록이 없습니다.")
        else:
            with open("memo.txt", "w", encoding = "utf-8")as file:
                sorted_ranking = sorted(ranking, key=lambda x: x["value"])
                print("랭킹")
                for rank, r in enumerate(sorted_ranking, start=1):
                    print(f"{rank}등 {r['name']} {r['value']}회")
                
                    
    elif aw == 3:
        print("프로그램을 종료합니다.")
        break