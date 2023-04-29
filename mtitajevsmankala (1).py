
class CLAUKUMS:
    
    def __init__(T1, spele):
        if (spele != None):
            T1.spele = spele[:]
            
        else:
            T1.spele = [0 for N in range(14)]
            
            for N in range(0,6):
                T1.spele[N] = 4
                
            for N in range(7,13):
                T1.spele[N] = 4





    def FGAJIENS(T2, N):
        NF = N
        velreiz = False
        pievienot = T2.spele[NF]
        T2.spele[NF] = 0
        
        
        if (N > 6):
            graudi = pievienot
            
            while graudi > 0:
                N = N+1
                N = N % 14
                
                if (N == 6):
                    continue
                
                else:
                    T2.spele[N % 14] += 1
                    
                    
                    graudi=graudi - 1
                
            if (N > 6 and T2.spele[N] == 1 and N != 13 and T2.spele[5-(N-7)] != 0):
                
                T2.spele[13] += 1 + T2.spele[5-(N-7)]
                T2.spele[N] = 0
                T2.spele[5-(N-7)] = 0
                
                
            if (N == 13):
                velreiz = True
        else:
            graudi = pievienot
            
            
            while (graudi > 0):
                N = N+1
                N = N % 14
                
                if (N == 13):
                    continue
                else:
                    T2.spele[N%14] = 1 + T2.spele[N%14]
                    
                    
                graudi = graudi - 1
                
            if (N < 6 and T2.spele[N] == 1 and N !=6 and T2.spele[-N + 12]!=0):
                T2.spele[6] += 1 + T2.spele[-N + 12]
                T2.spele[N] = 0
                T2.spele[-N + 12] = 0
                
            if (N == 6):
                velreiz = True
                
        return velreiz



    def FBEIGAS(T3):
        if (sum(T3.spele[0:6]) == 0) :
            T3.spele[13] += sum(T3.spele[7:13])
            
            for N in range(14):
                if  (N != 13 and N != 6):
                    T3.spele[N] = 0

            return True
        
        elif (sum(T3.spele[7:13])==0):
            T3.spele[6] += sum(T3.spele[0:6])
            
            for N in range(14):
                if  (N != 13 and N != 6):
                    T3.spele[N] = 0
            return True



        return False




    def FIZVADE(T4):
        for N in range(12,6,-1):
            print('__', T4.spele[N], '___', end = '_')
            
            
        print('__')
        print(T4.spele[13],'____________________________________________________',T4.spele[6])

        for N in range(0,6,1):
            print('__', T4.spele[N], '___', end='_')
            
            
        print('__')
        
        
        
        
        
    def FVERT(T5):
        if (T5.FBEIGAS()):
            if (T5.spele[13]>T5.spele[6]):
                return 100
            
            elif (T5.spele[13]==T5.spele[6]):
                return 0
            
            else :
                 return -100
                
                
        else:
            return T5.spele[13] - T5.spele[6]

def ALFABETA(spele, skaits, ALFA, BETA , MINIMAX):
    if (skaits == 0 or spele.FBEIGAS()):
        return spele.FVERT(),-1
    
    if (MINIMAX):
        temp_value = -1000000
        FGAJIENS = -1
        
        for N in range(7,13,1):
            if (spele.spele[N]==0):
                continue
            
            LAUK = CLAUKUMS(spele.spele[:])
            MINIMAX_2 = LAUK.FGAJIENS(N)
            new_value,_ =  ALFABETA(LAUK, skaits-1, ALFA, BETA, MINIMAX_2)
            
            if (temp_value < new_value):
                FGAJIENS = N
                temp_value = new_value
                
            ALFA = max(ALFA, temp_value)
            
            if (ALFA >= BETA) :
                break
            
        return temp_value, FGAJIENS
    
    
    else:
        temp_value = 1000000
        FGAJIENS = -1
        
        for N in range(0, 6, 1):
            if (spele.spele[N] == 0):
                continue
            
            LAUK = CLAUKUMS(spele.spele[:])
            MINIMAX_2 = LAUK.FGAJIENS(N)
            new_value,_ = ALFABETA(LAUK, skaits - 1, ALFA, BETA, not  MINIMAX_2)
            
            if (temp_value > new_value):
                FGAJIENS = N
                temp_value = new_value
                
            BETA = min(BETA, temp_value)
            
            if (ALFA >= BETA):
                break
            
        return temp_value, FGAJIENS




def FPRETPROGRAMMU():                                    
    NF = CLAUKUMS(None)
    NF.FIZVADE()
    while (True):
        if (NF.FBEIGAS()):
            break
        
        while (True):
            if (NF.FBEIGAS()):
                break
            
            POZICIJA = int(input("Tagad Jusu gajiens ----> "))
            
            if (POZICIJA > 5 or NF.spele[POZICIJA] == 0):
                print("Izveleties citu poziciju")
                continue
            
            POZICIJA_2 = NF.FGAJIENS(POZICIJA)
            NF.FIZVADE()
            
            if (not POZICIJA_2):
                break
            
        while (True):
            if (NF.FBEIGAS()):
                break
            
            print("programmas gajiens ----> ", end = "")
            _,VAL_3 = ALFABETA(NF, 10, -100000, 100000, True)
            
            print(VAL_3)
            POZICIJA_2 = NF.FGAJIENS(VAL_3)
            NF.FIZVADE()
            
            if (not POZICIJA_2):
                break
            
    if (NF.spele[0] < NF.spele[13]):
        print("programma uzvare")
        
    else:
        print("Apsveicam, Jus uzvarejat")
        
        
    print('Paldies par speli')
    NF.FIZVADE()



while (True):
        print("laukums izskatas sadi: ||  ||..|..|..|..|..|..||  || <---- programmas pozicijas")
        print("\n                       ||  || 0| 1| 2| 3| 4| 5||  || <---- Jusu pozicijas")
        FPRETPROGRAMMU()
        break