import math
num = float(input('Qual seu angulo?'))
coss = math.cos(math.radians(num))
senn = math.sin(math.radians(num))
tan = math.tan(math.radians(num))
print('Seu angulo é {:.2f}\nO cosseno dele é {:.2f}\nseu seno é {:.2f}\nsua tangente é {:.2f}'.format(num,coss,senn,tan))
