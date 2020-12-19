if __name__ == "__main__":
    pass

    n=input("数字を入力")
    try:
        N=int(n)
        if N%2==0:
            print(N , "Gusu")
        else:
            print(N ,"Kisu")
    except ValueError:
        print("数字でばありません")
      



    
    

  