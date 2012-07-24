# encoding: utf-8

import unittest
import datetime
import sys
from os.path import join, abspath, dirname
sys.path.insert(0, abspath(join(dirname(''))))

from data_humana import exibir


class TestDataHumana(unittest.TestCase):
    agora = datetime.datetime.now()

    def verifica_texto_tempo_decorrido(self, data_passada, tempo_decorrido):
        tempo = self.agora + data_passada
        data_transformada = exibir(tempo)
        self.assertEqual(data_transformada, tempo_decorrido)

    def test_deve_retornar_quantidade_anos_quando_estiver_em_anos(self):
        dez_anos = datetime.timedelta(days=-3650)
        self.verifica_texto_tempo_decorrido(dez_anos, '10 anos atrás')

    def test_deve_retornar_ano_no_singular_quanto_tiver_um_ano(self):
        um_ano = datetime.timedelta(days=-365)
        self.verifica_texto_tempo_decorrido(um_ano, '1 ano atrás')

    def test_deve_retornar_quantidade_meses_quando_estiver_em_meses(self):
        dez_meses = datetime.timedelta(days=-300)
        self.verifica_texto_tempo_decorrido(dez_meses, '10 meses atrás')

    def test_deve_retornar_mes_no_singular_quando_tiver_um_mes(self):
        um_mes = datetime.timedelta(days=-30)
        self.verifica_texto_tempo_decorrido(um_mes, '1 mês atrás')

    def test_deve_retornar_quantidade_semanas_quando_estiver_em_semanas(self):
        quatro_semanas = datetime.timedelta(days=-28)
        self.verifica_texto_tempo_decorrido(quatro_semanas, '4 semanas atrás')

    def test_deve_retornar_semana_no_singular_quando_tiver_uma_semana(self):
        uma_semana = datetime.timedelta(days=-7)
        self.verifica_texto_tempo_decorrido(uma_semana, '1 semana atrás')

    def test_deve_retornar_quantidade_dias_quando_estiver_em_dias(self):
        seis_dias = datetime.timedelta(days=-6)
        self.verifica_texto_tempo_decorrido(seis_dias, '6 dias atrás')

    def test_deve_retornar_dia_no_singular_quando_tiver_um_dia(self):
        um_dia = datetime.timedelta(days=-1)
        self.verifica_texto_tempo_decorrido(um_dia, '1 dia atrás')

    def test_deve_retornar_quantidade_horas_quando_estiver_em_horas(self):
        dez_horas = datetime.timedelta(hours=-10)
        self.verifica_texto_tempo_decorrido(dez_horas, '10 horas atrás')

    def test_deve_retornar_hora_no_singular_quando_tiver_uma_hora(self):
        uma_hora = datetime.timedelta(hours=-1)
        self.verifica_texto_tempo_decorrido(uma_hora, '1 hora atrás')

    def test_deve_retornar_quantidade_minutos_quando_estiver_em_minutos(self):
        dez_minutos = datetime.timedelta(minutes=-10)
        self.verifica_texto_tempo_decorrido(dez_minutos, '10 minutos atrás')

    def test_deve_retornar_minuto_no_singular_quando_tiver_um_minuto(self):
        um_minuto = datetime.timedelta(minutes=-1)
        self.verifica_texto_tempo_decorrido(um_minuto, '1 minuto atrás')

    def test_deve_retornar_menos_de_1_minuto_quando_estiver_em_segundos(self):
        segundos = datetime.timedelta(seconds=-10)
        self.verifica_texto_tempo_decorrido(segundos, 'menos de um minuto')

if __name__ == '__main__':
    unittest.main()
