import pandas as pd
import copy
try:
    from util import collum_dict, parse_line, get_data_as_dict
except ImportError:
    from bovespa2csv.util import collum_dict, parse_line, get_data_as_dict # noqa


class BovespaParser(object):
    """docstring for ClassName"""
    def __init__(self):
        self.info_dict = copy.deepcopy(collum_dict)
        self.df = None
        self.collums_list = ["tipo de registro",
                             "data do pregao", # noqa
                             "codigo bdi", # noqa
                             "codigo de negociação do papel", # noqa
                             "tipo de mercado", # noqa
                             "nome resumido da empresa emissora do papel", # noqa
                             "especificacao do papel", # noqa
                             "prazo em dias do mercado a termo", # noqa
                             "moeda de referencia", # noqa
                             "preco de abertura do papel-mercado no pregao", # noqa
                             "preco maximo do papel-mercado no pregao", # noqa
                             "preco minimo do papel-mercado no pregao", # noqa
                             "preco medio do papel-mercado no pregao", # noqa
                             "preco do ultimo negocio do papel-mercado no pregao", # noqa
                             "preco da melhor oferta de compra do papel-mercado no pregao", # noqa
                             "preco da melhor oferta de venda do papel-mercado no pregao", # noqa
                             "numero de negocios efetuados com o papel mercado no pregao", # noqa
                             "quantidade total de titulos negociados neste papel-mercado", # noqa
                             "volume total de titulos negociados neste papel-mercado", # noqa
                             "preco de exercicio para o mercado de opcoes ou valor do contrato para o mercado de  termo secundario", # noqa
                             'indicador de correção de preços de exercícios ou valores de contrato para os mercados de opções ou termo secundário', # noqa
                             'data do vencimento para os mercados de opções ou termo secundário', # noqa
                             'fator de cotação do papel', # noqa
                             'preço de exercício em pontos para opções referenciadas em dólar ou valor de contrato em pontos para termo secundário', # noqa
                             'código do papel no sistema isin ou código interno do papel', # noqa
                             'número de distribuição do papel']

    def read_txt(self, path):
        """
        fdfdf
        """
        self.info_dict = get_data_as_dict(path, self.info_dict)
        self.df = pd.DataFrame(self.info_dict)

    def to_csv(self, input_path, output_path):
        """
        fdfdf
        """
        if self.df is None:
            self.read_txt(input_path)
        self.df = self.df[self.collums_list]
        self.df.to_csv(output_path, index=False)

    def to_excel(self, input_path, output_path):
        """
        fdfdf
        """
        if self.df is None:
            self.read_txt(input_path)
        self.df = self.df[self.collums_list]
        writer = pd.ExcelWriter(output_path,
                                engine='xlsxwriter')
        self.df.to_excel(writer,
                         sheet_name='Sheet1')
        writer.save()
