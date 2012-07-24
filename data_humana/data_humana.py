# encoding: utf-8

from datetime import datetime


def exibir(data):
    """
    O parametro data é a data em qua aconteceu o fato,
    baseado nessa data será calculada a diferença para a data atual,
    e será retornada uma mensagem humana do tempo decorrido:

    data: datetime
    retorno: string

    Exemplos de retorno: 10 horas atrás, 10 meses atrás, 3 semanas atrás
    """

    agora = datetime.now()
    diferenca_datas = agora - data
    anos = meses = semanas = dias = horas = minutos = 0

    anos = diferenca_datas.days / 365
    meses = diferenca_datas.days / 30
    semanas = diferenca_datas.days / 7
    dias = diferenca_datas.days
    horas = diferenca_datas.seconds / 3600
    minutos = diferenca_datas.seconds / 60

    if anos:
        formato = (anos, pluralizar('ano', 'anos', anos))

    elif meses:
        formato = (meses, pluralizar('mês', 'meses', meses))

    elif semanas:
        formato = (semanas, pluralizar('semana', 'semanas', semanas))

    elif dias:
        formato = (dias, pluralizar('dia', 'dias', dias))

    elif horas:
        formato = (horas, pluralizar('hora', 'horas', horas))

    elif minutos:
        formato = (minutos, pluralizar('minuto', 'minutos', minutos))

    else:
        return 'menos de um minuto'

    return '%d %s atrás' % formato


def pluralizar(palavra_singular, palavra_plural, quantidade):
    """
    pluralizar serve para decidir qual das palavras deve ser retornada,
    de acordo com a quantidade, caso seja maior que um, é retornado no
    plural, senao é retornada a palavra no singular.

    palavra_singular: string
    palavra_plural: string
    quantidade: integer, float (número em geral)
    retorno: string
    """

    if quantidade > 1:
        return palavra_plural
    else:
        return palavra_singular
