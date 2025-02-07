from televisor import *

televisao = Televisor('SONY','SONY-123')

controle = ControleRemoto(televisao)

controle.sintonizarCanal('SBT')
controle.trocarCanal('SBT')

print(televisao.canal_atual)