import random
import sys #Para la función sys.exit() (cierra el programa al haber un vencedor)

print("¿Estás listo para enfrentarte a Despojo al 3 en Raya?")
print("   _")
print("  ( \  ")
print("   ) )")
print('  ( (  .-""""-.  A.-.A  ')
print("   \ \/        \/ , , \ ")
print("    \    \     =;  t  /=")
print("     \    |··-   ',--'  ")
print("      /  //  |  ||      ")
print("     /__,))  |__,))     ")

print("\nPara colocar las fichas se usará un sistema de coordenadas")
print("Por ejemplo: Si deseas colocar tu ficha arriba a la derecha")
print("deberás introducir la fila 1 y la columna 3")

Tablero = [[" "," "," "],
           [" "," "," "],
           [" "," "," "]]

F = [[[None,None],[None,None],[None,None]],    #Coordenadas fichas usuario
     [[None,None],[None,None],[None,None]]]    #Coordenadas fichas Despojo
direccion_posible_linea = [0,0]
I=[5,5]

def DibujarTablero (Tablero):
    i=0
    j=0
    print("\n----------")
    while i<3:
        print("|",end="")     #Lo del end es para que no haga salto de linea automaticamente
        while j<3:
            print(Tablero[i][j],"|",end="")  
            j+=1
        i+=1
        j=0
        print("\n----------")

def ColocarFichaUsuario (Tablero, ficha):
    repetir =True
    while repetir:
        print("Coloca tu ficha")
        i=int(input("Introduce fila: "))-1
        j=int(input("Introduce columna: "))-1
        if (i==0 or i==1 or i==2) and (j==0 or j==1 or j==2) and Tablero[i][j]==" ":
            print("Has colocado tu ficha en",i+1,j+1)
            Tablero[i][j]="X"
            F[0][ficha][0]=i
            F[0][ficha][1]=j
            repetir = False
        else:
            print("Posición no válida",i+1,j+1)
#Selección primera ficha
ColocarFichaUsuario (Tablero, 0)
DibujarTablero(Tablero)
#Primera Selección de Despojo
print("\nLe toca a Despojo")
if Tablero[1][1] == " ":
    Tablero[1][1]="D"
    F[1][0][0]=1
    F[1][0][1]=1
else:
    i=2*random.randint(0,1)
    j=2*random.randint(0,1)
    Tablero[i][j]="D"
    F[1][0][0]=i
    F[1][0][1]=j
DibujarTablero(Tablero)
print("Segundo turno")
ColocarFichaUsuario (Tablero, 1)
DibujarTablero(Tablero)
print("Segundo turno de Despojo")
#Segundo turno del oponente
#Comprobar si despojo puede hacer línea
def Comprobar_linea (Tablero, ficha_nueva, k, k_):
    victoria_Despojo = False
    victoria_usuario=0
    f=0
    g=1
    while f<2:
        while g<3:
            if F[k][f][0] != None and F[k][g][0] != None:
                direccion_posible_linea[0]=F[k][f][0]-F[k][g][0]
                direccion_posible_linea[1]=F[k][f][1]-F[k][g][1]
                j=0
                i=0
                if direccion_posible_linea[0]==0: #Horizontal
                    fila_posible_linea=F[k][f][0]
                    while j<3:
                        if Tablero[fila_posible_linea][j]==" ":
                            Tablero[fila_posible_linea][j]="D"
                            victoria_Despojo = True
                            F[k_][ficha_nueva][0]=fila_posible_linea
                            F[k_][ficha_nueva][1]=j
                            if k == 0:
                                victoria_usuario += 1
                        j+=1

                if direccion_posible_linea[1]==0: #Vertical
                    columna_posible_linea=F[k][f][1]
                    while i<3:
                        if Tablero[i][columna_posible_linea]==" ":
                            Tablero[i][columna_posible_linea]="D"
                            victoria_Despojo = True
                            F[k_][ficha_nueva][0]=i
                            F[k_][ficha_nueva][1]=columna_posible_linea
                            if k == 0:
                                victoria_usuario += 1
                        i+=1
                        
                #Posible Diagonal
                if direccion_posible_linea[0]==direccion_posible_linea[1] or direccion_posible_linea[0]==-direccion_posible_linea[1]:
                    if k==0:
                        a="X"
                    if k==1:
                        a="D"
                #Comprobacion Diagonal como bandera Galicia
                    if (Tablero[0][0]==a or Tablero[2][2]==a) and Tablero[1][1]==a:
                        i=0
                        while i<3:
                            if Tablero[i][i]==" ":
                                Tablero[i][i]="D"
                                victoria_Despojo = True
                                F[k_][ficha_nueva][0]=i
                                F[k_][ficha_nueva][1]=i
                                if k == 0:
                                    victoria_usuario += 1
                            i+=1
                        
                #Comprobacion de la otra Diagonal
                    if (Tablero[0][2]==a or Tablero[2][0]==a) and Tablero[1][1]==a:
                        if Tablero[0][2]==" ":
                            Tablero[0][2]="D"
                            victoria_Despojo = True
                            F[k_][ficha_nueva][0]=0
                            F[k_][ficha_nueva][1]=2
                            if k == 0:
                                victoria_usuario += 1
                        if Tablero[2][0]==" ":
                            Tablero[2][0]="D"
                            victoria_Despojo = True
                            F[k_][ficha_nueva][0]=2
                            F[k_][ficha_nueva][1]=0
                            if k == 0:
                                victoria_usuario += 1                                    
            g+=1
        g=2
        f+=1
    if victoria_usuario > 1:
        print("   Me rindo, has ganado")
        sys.exit()
    return victoria_Despojo
        
ficha_nueva=1
k=0
k_=1
Comprobar_linea (Tablero, ficha_nueva, k, k_)
print(Comprobar_linea (Tablero, ficha_nueva, k, k_))
def ultima_opcion_despojo (Tablero, k_, ficha_nueva):
    if F[k_][ficha_nueva][0]==None:
        repetir = True
        while repetir:
            i=random.randint(0,2)
            j=random.randint(0,2)
            if Tablero[i][j]==" ":
                Tablero[i][j]="D"
                F[k_][ficha_nueva][0]=i
                F[k_][ficha_nueva][1]=j
                repetir = False
ultima_opcion_despojo(Tablero, k_, ficha_nueva)
DibujarTablero(Tablero)
#Tercer turno usuario

ColocarFichaUsuario (Tablero, 2)
DibujarTablero(Tablero)

print("Turno de Despojo")

ficha_nueva=2
k=1
k_=1
#Comprueba si Despojo Puede ganar
#Comprobar_linea(Tablero, ficha_nueva, k, k_)

if Comprobar_linea(Tablero, ficha_nueva, k, k_):
    print("Ya te vale, has perdido contra Despojo")
    DibujarTablero(Tablero)
    sys.exit()

#Despojo evita tu victoria
k=0
k_=1
Comprobar_linea (Tablero, ficha_nueva, k, k_)

#Si aún Despojo no ha puesto su ficha
ficha_nueva=2
ultima_opcion_despojo (Tablero, k_, ficha_nueva)
DibujarTablero(Tablero)

def CambiarFichaUsuario (Tablero):
    repetir =True
    while repetir:
        print("Elije la posición de la ficha que deseas mover")
        i=int(input("Introduce fila: "))-1
        j=int(input("Introduce columna: "))-1
        if (i==0 or i==1 or i==2) and (j==0 or j==1 or j==2) and Tablero[i][j]=="X":
            print("Has quitado tu ficha de",i+1,j+1)
            Tablero[i][j]=" "
            repetir = False
            f=0
            while f<3:
                if F[0][f][0]==i and F[0][f][1]==j:
                    ficha=f
                f+=1
        else:
            print("No puedes quitar esa ficha",i+1,j+1)
        I=[i,j]
    print("¿Dónde vas a poner la ficha?")
    repetir =True
    while repetir:
        print("Coloca tu ficha, recuerda que no puedes ponerla en", I[0]+1, I[1]+1)
        i_=int(input("Introduce fila: "))-1
        j_=int(input("Introduce columna: "))-1
        I_=[i_,j_]
        if (i_==0 or i_==1 or i_==2) and (j_==0 or j_==1 or j_==2) and Tablero[i_][j_]==" " and I != I_:
            print("Has colocado tu ficha en",i_ +1,j_ +1)
            Tablero[i_][j_]="X"
            F[0][ficha][0]=i_
            F[0][ficha][1]=j_
            repetir = False
        else:
            print("Posición no válida")
    return I
            
#Función decidir movimiento Despojo
def Cambiar_ficha_Despojo (Tablero):
    victoria_Despojo = False
    victoria_usuario=0
    f=0
    g=1
    k=1
    tapar=[None,None]
    while k >= 0:
        while f<2:
            while g<3:
                if F[k][f][0] != None and F[k][g][0] != None:
                    direccion_posible_linea[0]=F[k][f][0]-F[k][g][0]
                    direccion_posible_linea[1]=F[k][f][1]-F[k][g][1]
                    j=0
                    i=0
                    if direccion_posible_linea[0]==0: #Horizontal
                        fila_posible_linea=F[k][f][0]
                        while j<3:
                            if Tablero[fila_posible_linea][j]==" ":
                                if k==1:
                                    victoria_Despojo = True
                                    ficha_nueva=3-(f+g)
                                    F[1][ficha_nueva][0]=fila_posible_linea
                                    F[1][ficha_nueva][1]=j
                                    return 1
                                if k==0:
                                    victoria_usuario += 1
                                    tapar=[fila_posible_linea,j]
                            j+=1

                    if direccion_posible_linea[1]==0: #Vertical
                        columna_posible_linea=F[k][f][1]
                        while i<3:
                            if Tablero[i][columna_posible_linea]==" ":
                                if k==1:
                                    victoria_Despojo = True
                                    ficha_nueva=3-(f+g)
                                    F[1][ficha_nueva][0]=i
                                    F[1][ficha_nueva][1]=columna_posible_linea
                                    return 1
                                if k==0:
                                    victoria_usuario += 1
                                    tapar=[i,columna_posible_linea]
                            i+=1
                            
                    #Posible Diagonal
                    if direccion_posible_linea[0]==direccion_posible_linea[1] or direccion_posible_linea[0]==-direccion_posible_linea[1]:
                        if k==0:
                            a="X"
                        if k==1:
                            a="D"
                    #Comprobacion Diagonal como bandera Galicia
                        if (Tablero[0][0]==a or Tablero[2][2]==a) and Tablero[1][1]==a and direccion_posible_linea[0]==direccion_posible_linea[1]:
                            i=0
                            while i<3:
                                if Tablero[i][i]==" ":
                                    if k==1:
                                        victoria_Despojo = True
                                        ficha_nueva=3-(f+g)
                                        F[k_][ficha_nueva][0]=i
                                        F[k_][ficha_nueva][1]=i
                                        return 1
                                    if k==0:
                                        victoria_usuario += 1
                                        b=3
                                        tapar=[i,i]
                                i+=1                           
                    #Comprobacion de la otra Diagonal
                        if (Tablero[0][2]==a or Tablero[2][0]==a) and Tablero[1][1]==a:
                            if Tablero[0][2]==" ":
                                if k==1:
                                    victoria_Despojo = True
                                    ficha_nueva=3-(f+g)
                                    F[1][ficha_nueva][0]=0
                                    F[1][ficha_nueva][1]=2
                                    return 1
                                if k==0:
                                    victoria_usuario += 1
                                    tapar=[0,2]
                            if Tablero[2][0]==" ":
                                if k==1:
                                    victoria_Despojo = True
                                    ficha_nueva=3-(f+g)
                                    F[1][ficha_nueva][0]=2
                                    F[1][ficha_nueva][1]=0
                                    return 1
                                if k==0:
                                    victoria_usuario += 1
                                    tapar=[2,0]
                g+=1
            g=2
            f+=1
        k-=1
        f=0
        g=1
    if victoria_usuario > 0:
        quitar=random.randint(0,2)
        F[1][quitar][0]=tapar[0]
        F[1][quitar][1]=tapar[1]
        return 3
    if victoria_usuario == 0:
        quitar=random.randint(0,2)
        seguir = True
        while seguir:
            i=random.randint(0,2)
            j=random.randint(0,2)
            if Tablero[i][j]==" ":
                F[1][quitar][0]=i
                F[1][quitar][1]=j
                Tablero[i][j]=="D"
                seguir = False
        return 4           
            
def SacarTablero (F):
    i=0
    j=0
    k=0
    f=0
    Tablero = [[" "," "," "],
               [" "," "," "],
               [" "," "," "]]
    while k<2:
        while f<3: 
            if k==0:
                Tablero[F[k][f][0]][F[k][f][1]]="X"
            if k==1:
                Tablero[F[k][f][0]][F[k][f][1]]="D"
            f+=1
        f=0
        k+=1
    return Tablero          
            
def SacarF (Tablero):
    f=0
    f_=0
    i=0
    j=0
    while i<3:
        while j<3:
            if Tablero[i][j]=="X":
                F[0][f][0]=i
                F[0][f][1]=j
                f+=1
            if Tablero[i][j]=="D":
                F[1][f_][0]=i
                F[1][f_][1]=j
                f_+=1
            j+=1
        j=0
        i+=1           
            
while True:
    I=CambiarFichaUsuario(Tablero)
    #Comprobar posible victoria usuario debido error de Despojo
    if F[0][0][0]==F[0][1][0] and F[0][1][0]==F[0][2][0]:   #Línea Horizontal
        print("Enhorabuena, has ganado")
        DibujarTablero(Tablero)
        sys.exit()
    if F[0][0][1]==F[0][1][1] and F[0][1][1]==F[0][2][1]:   #Línea Vertical
        print("Enhorabuena, has ganado")
        DibujarTablero(Tablero)
        sys.exit()
    if F[0][0][0]==F[0][0][1] and F[0][1][0]==F[0][1][1] and  F[0][2][0]==F[0][2][1]:#Diagonal Bandera Galicia
        print("Enhorabuena, has ganado")
        DibujarTablero(Tablero)
        sys.exit()
    if F[0][0][0]==2-F[0][0][1] and F[0][1][0]==2-F[0][1][1] and  F[0][2][0]==2-F[0][2][1]:#Diagonal distinta Bandera Galicia
        print("Enhorabuena, has ganado")
        DibujarTablero(Tablero)
        sys.exit()       
    DibujarTablero(Tablero)
    SacarF(Tablero)
    print("\nTurno de Despojo")
    a=Cambiar_ficha_Despojo(Tablero)
    if a==1:
        print("Ya te vale, has perdido contra Despojo")
        DibujarTablero(Tablero)
        sys.exit()
    if a==2:
        print("Enhorabueba")
        DibujarTablero(Tablero)
        sys.exit()
    Tablero = SacarTablero(F)
    DibujarTablero(Tablero)
    

    

