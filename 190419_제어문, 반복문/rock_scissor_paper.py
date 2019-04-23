import random
def get_player_choice():
    """
    interface
    get_player_choice() -> string
    반환값 : "바위" or "가위" or "보"
    """
    choice = input("당신의 선택은? : ")
    while choice != "바위" and choice != "가위" and choice != "보":
        choice = input("당신의 선택은? : ")
        '''
        반환값만을 반환하게 만들어야 함 -> while문
        '''
    return choice
    # if choice == "바위" or choice == "가위" or choice == "보":
    #     print(choice)
def get_computer_choice():
    '''
    get_computer_choice() -> string
    반환값 : "바위" | "가위" | "보"
    '''
    # 첫번째 방법 : 딕셔너리
    # dic = {0 : "바위", 1 : "가위", 2 : "보"}
    # ran = random.randint(0,2)
    # return dic[ran]
    # 두번째 방법 : 튜플
    tu=("가위","바위","보")
    ran = random.randint(0,2)
    return tu[ran]

def who_wins(player, com):
    '''
    who_wins(player, com) -> string
    반환값 : 플레이어가 이기면 'player'
             컴퓨터가 이기면 'computer'
             비기면 None
    '''
    if player == com:
        return None
    
    elif (player == "가위" and com == "보") or \
        (player == "바위" and com == "가위") or \
        (player == "보" and com == "바위"):
        return 'player'
    else:
        return 'computer'

def play_one():
    '''
    play_one() -> string
    반환값 : 플레이어가 이기면 'player'
             컴퓨터가 이기면 'computer'
    '''
    while True:
        player = get_player_choice()
        com = get_computer_choice()
        result = who_wins(player, com)
        print(f'player : {player}, computer : {com}')
        
        if result == 'player':
            print("you win !")
            return 'player'
        elif result == 'computer':
            print("you lose")
            return 'computer'
        else:
            print("draw")
            continue

def check_final_winner(result):
    '''
    check_final_winner(result) -> string
    result : ex) ['player', 'player']
    반환값 : result 안에 'player'가 2개 이상이면 : 'player'
                        'com'가 2개 이상이면 : 'computer'
            그렇지 않다면, None
    '''
    print(f"플레이어 : {result.count('player')}승, 컴퓨터 : {result.count('computer')}승")
    if result.count('player') >= 2:
        return 'player'
    elif result.count('computer') >= 2:
        return 'computer'
    else:
        None

def play():
    '''
    play() -> None
    3판 2선승 가위바위보 게임
    '''
    result_list = []
    while True:
        result_list.append(play_one())
        checked = check_final_winner(result_list)

        if checked == 'player':
            print("축하합니다! 당신이 이겼어요!!!!!!!!!!!!!!") 
        elif checked == 'computer':
            print("당신이 졌습니다........... 다음에 다시 도전하세요")
        else:
            continue       
        



'''
for문을 3번 돌려서 이기는 사람을 리스트에 저장
'''
if __name__ == "__main__":
    play()
    # player =get_player_choice()
    # com = get_computer_choice()
    # result = who_wins(player, com)
    # print(f'player : {player}, computer : {com}')

    # if result == 'player':
    #     print("you win"!)
    # elif result == 'computer':
    #     print("you lose")
    # else:
    #     print("draw")


    # for i in range(3):
    #     # string = get_player_choice( )
    #     string = get_computer_choice( )

    #     print(string)