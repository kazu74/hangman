def hangman(word):
    life=10
    rletters = list(word)
    board = ["_"] * len(word)
    #win=False
    print("ハングマンへようこそ！")

    while life > 0 :

        print("\n")
        msg = "1文字を予想すべし"
        char =input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            life -= 1
        
        print(",".join(board))
        print("\n","LIFE=",life)
       
        if "_" not in board:
            print("あなたの勝ち！！")
            print("  ".join(board))
            break
        
    if life==0:
            print("残念！あなたの負け")        


import random
wordlist=["hokkaido","aomori","iwate","akita","yamagata","miyagi","fukusima", \
        "niigata","ibaraki","chiba","gunma","tochigi","yamanashi","saitama", \
            "tokyo","kanagawa","shizuoka","nagano","aichi","gifu","mie","fukui","ishikawa","toyama", \
                "shiga","kyoto","nara","wakayama","osaka","hyogo","okayama","hiroshima" ,\
                    "yamaguchi","shimane","tottori","kagawa","ehime","kochi","tokushima", \
                        "fukuoka","saga","nagasaki","kumamoto","oita","miyazaki","kagoshima","okinawa"]
num=random.randint(0,len(wordlist))
answer=wordlist[num]


hangman(answer)

