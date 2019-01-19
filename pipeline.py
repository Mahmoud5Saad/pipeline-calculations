import math


# introduction to the project
print ('This code is developed for Pipe Line course, Helwan university.\n')
print ('This code was developed under supervision of:\nDr.Eng. Osama Khorais\n\n')
print ('Developed by:\nMahmoud Mohamed Saad Soliman\nSection 10\n\n')
print ('The code is developed to solve the Question no.1 in Sheet no.1.')

#get variables from engineer
print ('Now we ask you to input input the values.\n\n')
Row=float(input('Density: '))
Meu=float(input('Absolute viscosity: '))
D=float(input('Inner diameter: '))
E=float(input('Absolute roughness: '))
L=float(input('Pipe length: '))
Hp=float(input('Pump head: '))
K=float(input('Friction coefficient: '))
P1=float(input('Pressure at point 1 : '))
P2=float(input('Pressure  at point 2 : '))
V1=float(input('Velocity at point 1 : '))
V2=float(input('Velocity at point 2 : '))

#constants used in calculations
g=9.81
Pie=(22/7)
gama=Row*g
e=2.718281828


#calculations expressions
In=int(input('\n\nNow we have 2 options:\nTo calculate Delta_Z please write 1 and press ENTER \nTo calculate Q  please write 2 and press ENTER\n\n') )

#the code for calculating Delta_Z
if In==1:
    B=float(input('\n\nPlease enter Volume flowrate in m^3/hr: '))
    m=3600
    Q=B/m
    V=4*Q/(Pie*math.pow(D,2))
    Re=(Row*V*D)/Meu
    in_Ln=0.27*(E/D)+5.74*( math.pow((1/Re),0.9) )
    F=1.325*( math.pow(math.log(in_Ln),-2) )
    print('Friction factor= '),(F)
    left=(F*L/D) + K
    right=math.pow(V,2) / (2*g)
    Hl=left*right
    delta_Z=( (P2-P1)/gama+( math.pow(V2,2)- math.pow(V1,2) )/(2*g) )-Hp+Hl
    print('\n\nDelta_Z =') ,(delta_Z)
    
else :
    in_Ln2=0.27*(E/D)
    F1=1.325*( math.pow(math.log(in_Ln2),-2) )
    delta_Z=float(input('\n\nDelta_Z: '))
    Hl=( (P1-P2)/gama+( math.pow(V1,2)- math.pow(V2,2) )/(2*g) )+Hp+delta_Z
    V_bast=(2*g*Hl)
    Q_c=Pie*D*D
    while(True):
        V=math.sqrt( V_bast / ( (F1*L/D)+K ) )
        Re=(Row*V*D)/Meu
        in_Ln=0.27*(E/D)+5.74*( math.pow((1/Re),0.9) )
        F2=1.325*( math.pow(math.log(in_Ln),-2) )
        V=math.sqrt( V_bast / ( (F2*L/D)+K ) )
        Q=Q_c*V/4
        diff=F2-F1
        if diff <=0:
            diff=(F2-F1)*-1
        if diff <= 0.001 :
            print('\n\nVolume flow rate     = '),(Q*3600)
            print('New Friction factor = '),(F2)
            print('Velocity             = '),(V)
            break
        else:
            print('\n\nVolume flow rate     = '),(Q*3600)
            print('New Fricition factor = '),(F2)
            print('Velocity             = '),(V)
            print('')
        F1=F2


try:
    input("\nPress enter to terminate")
except SyntaxError:
    pass
