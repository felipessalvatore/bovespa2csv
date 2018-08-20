
# dictionary with the main columns following the pdf file on
# http://www.b3.com.br/data/files/C8/F3/08/B4/297BE410F816C9E492D828A8/SeriesHistoricas_Layout.pdf

collum_dict = {"tipo de registro": [],
               "data do pregao": [], # noqa
               "codigo bdi": [], # noqa
               "codigo de negociação do papel": [], # noqa
               "tipo de mercado": [], # noqa
               "nome resumido da empresa emissora do papel": [], # noqa
               "especificacao do papel": [], # noqa
               "prazo em dias do mercado a termo": [], # noqa
               "moeda de referencia": [], # noqa
               "preco de abertura do papel-mercado no pregao": [], # noqa
               "preco maximo do papel-mercado no pregao": [], # noqa
               "preco minimo do papel-mercado no pregao": [], # noqa
               "preco medio do papel-mercado no pregao": [], # noqa
               "preco do ultimo negocio do papel-mercado no pregao": [], # noqa
               "preco da melhor oferta de compra do papel-mercado no pregao": [], # noqa
               "preco da melhor oferta de venda do papel-mercado no pregao": [], # noqa
               "numero de negocios efetuados com o papel mercado no pregao": [], # noqa
               "quantidade total de titulos negociados neste papel-mercado": [], # noqa
               "volume total de titulos negociados neste papel-mercado": [], # noqa
               "preco de exercicio para o mercado de opcoes ou valor do contrato para o mercado de  termo secundario": [], # noqa
               'indicador de correção de preços de exercícios ou valores de contrato para os mercados de opções ou termo secundário': [], # noqa
               'data do vencimento para os mercados de opções ou termo secundário': [], # noqa
               'fator de cotação do papel': [], # noqa
               'preço de exercício em pontos para opções referenciadas em dólar ou valor de contrato em pontos para termo secundário': [], # noqa
               'código do papel no sistema isin ou código interno do papel': [], # noqa
               'número de distribuição do papel': []} # noqa


def parse_line(line, info_dict):
    """
    Function that parse a line of the txt file breaking the string
    as describe in the B3 pdf

    http://www.b3.com.br/data/files/C8/F3/08/B4/297BE410F816C9E492D828A8/SeriesHistoricas_Layout.pdf

    :param line: text line
    :type line: str
    :param info_dict: dict with the columns as defined in collum_dict
    :type info_dict: dict
    :return: updated dict
    :rtype: dict
    """
    part = line[:2]
    info_dict["tipo de registro"].append(part)
    part = line[2:10]
    info_dict["data do pregao"].append(part)
    part = line[10:12]
    info_dict["codigo bdi"].append(part)
    part = line[12:24]
    info_dict["codigo de negociação do papel"].append(part)
    part = line[24: 27]
    info_dict["tipo de mercado"].append(part)
    part = line[27:39]
    info_dict["nome resumido da empresa emissora do papel"].append(part)
    part = line[39:49]
    info_dict["especificacao do papel"].append(part)
    part = line[49:52]
    info_dict["prazo em dias do mercado a termo"].append(part)
    part = line[52:56]
    info_dict["moeda de referencia"].append(part)
    part = line[56:69]
    part = float(part) / 100
    info_dict["preco de abertura do papel-mercado no pregao"].append(part)
    part = line[69:82]
    part = float(part) / 100
    info_dict["preco maximo do papel-mercado no pregao"].append(part)
    part = line[82:95]
    part = float(part) / 100
    info_dict["preco minimo do papel-mercado no pregao"].append(part)
    part = line[95:108]
    part = float(part) / 100
    info_dict["preco medio do papel-mercado no pregao"].append(part)
    part = line[108:121]
    part = float(part) / 100
    info_dict["preco do ultimo negocio do papel-mercado no pregao"].append(part) # noqa
    part = line[121:134]
    part = float(part) / 100
    info_dict["preco da melhor oferta de compra do papel-mercado no pregao"].append(part) # noqa
    part = line[134:147]
    part = float(part) / 100
    info_dict["preco da melhor oferta de venda do papel-mercado no pregao"].append(part) # noqa
    part = line[147:152]
    part = float(part) / 100
    info_dict["numero de negocios efetuados com o papel mercado no pregao"].append(part) # noqa
    part = line[152:170]
    info_dict["quantidade total de titulos negociados neste papel-mercado"].append(part) # noqa
    part = line[170:188]
    part = float(part) / 100
    info_dict["volume total de titulos negociados neste papel-mercado"].append(part) # noqa
    part = line[188:201]
    part = float(part) / 100
    info_dict["preco de exercicio para o mercado de opcoes ou valor do contrato para o mercado de  termo secundario"].append(part) # noqa
    part = line[201:202]
    info_dict['indicador de correção de preços de exercícios ou valores de contrato para os mercados de opções ou termo secundário'].append(part) # noqa
    part = line[202:210]
    info_dict['data do vencimento para os mercados de opções ou termo secundário'].append(part) # noqa
    part = line[210:217]
    part = int(part)
    info_dict['fator de cotação do papel'].append(part)
    part = line[217:230]
    part = float(part) / 100
    info_dict['preço de exercício em pontos para opções referenciadas em dólar ou valor de contrato em pontos para termo secundário'].append(part) # noqa
    part = line[230:242]
    info_dict['código do papel no sistema isin ou código interno do papel'].append(part) # noqa
    part = line[242: 245]
    info_dict['número de distribuição do papel'].append(part)

    return info_dict


def get_data_as_dict(path, info_dict):
    """
    Function that parse each line of the txt file and returns
    a dict with all the information

    :param path: text path
    :type path: str
    :param info_dict: dict with the columns as defined in collum_dict
    :type info_dict: dict
    :return: updated dict
    :rtype: dict
    """
    # with open(path, "r", encoding='latin-1') as file:
    with open(path, "r", encoding='latin-1') as file:
        for i, line in enumerate(file):
            if line[2:10] != "COTAHIST":
                try:
                    _ = line[1] # noqa
                    info_dict = parse_line(line, info_dict)
                except IndexError:
                    pass
    return info_dict
