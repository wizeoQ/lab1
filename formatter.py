import numpy as np

def ex(exercize):
    print("\n==========")
    print("Задание ", exercize)
def eq(equal=5):
    print('\n'+"="*equal)
def d(dash=5):
    print('\n'+"-"*dash)
def n(nice=None):
    print("\n༺•༻")
def l(line=5):
    print('─'*line)
def ln(long_nice=None):
    print("\n───────✧───────")
    
def yes_or_not(def_a=lambda:None,def_b=lambda:None):
    while True:
        out_flag=input('>')
        if out_flag=="":continue
        elif out_flag in "yY1дД":
            def_a()
            break
        elif out_flag in "nN0нН":
            def_b()
            break

def simple_complex(x,round_digitals=3,is_print=True,is_i=True,is_return=True):
    rnd=int(round_digitals)
    if is_i==True:unit='i'
    if is_i==False:unit='j'
    if np.isnan(x)==True:x_ir,x_ii="nan",'' #случай nan
    elif np.isinf(x)==True:x_ir,x_ii="inf",'' #случай inf
    else:
        x_ir=round(float(np.real(x)),rnd)
        x_ii=round(float(np.imag(x)),rnd)
        if float(x_ir)==int(x_ir):x_ir=int(x_ir) #убираем лишний .0
        if float(x_ii)==int(x_ii):x_ii=int(x_ii) #убираем лишний .0
        if x_ii==0:x_ii='' #число не мнимое
        elif x_ii>0:x_ii='+'+str(x_ii)+unit
        elif x_ii<0:x_ii=str(x_ii)+unit #минус сам допишется
    result=str(x_ir)+str(x_ii)
    if is_print==True:print(result)
    if is_return==True:return result