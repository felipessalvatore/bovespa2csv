import pandas as pd
import copy
try:
    from util import collum_dict, parse_line, get_data_as_dict
except ImportError:
    from bovespa2csv.util import collum_dict, parse_line, get_data_as_dict # noqa


class BovespaParser(object):
    """
    Class to parse a txt document that can be obtained in the site

    http://www.bmfbovespa.com.br/pt_br/servicos/market-data/historico/mercado-a-vista/series-historicas/

    The document can be transformed into a csv or an excel file.

    Example:
    suppose bovespa text is the file 'COTAHIST_DXXXXXX.TXT'

        from bovespa2csv.BovespaParser import BovespaParser

        parser = BovespaParser()
        parser.to_csv("COTAHIST_DXXXXXX.TXT","example.csv")
        parser.to_excel("COTAHIST_DXXXXXX.TXT","example.xlsx")
    """
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
        Method to parse each line of the txt
        and store the information into a DataFrame

        :param path: text path
        :type path: str
        """
        self.info_dict = get_data_as_dict(path, self.info_dict)
        self.df = pd.DataFrame(self.info_dict)

    def to_csv(self, input_path, output_path):
        """
        Method to transform a Bovespa txt file into a csv file

        :param input_path: path to Bovespa txt
        :type input_path: str
        :param output_path: path to csv file
        :type output_path: str
        """
        if self.df is None:
            self.read_txt(input_path)
        self.df = self.df[self.collums_list]
        self.df.to_csv(output_path, index=False)

    def to_excel(self, input_path, output_path):
        """
        Method to transform a Bovespa txt file into a xlsx file

        :param input_path: path to Bovespa txt
        :type input_path: str
        :param output_path: path to xlsx file
        :type output_path: str
        """
        if self.df is None:
            self.read_txt(input_path)
        self.df = self.df[self.collums_list]
        writer = pd.ExcelWriter(output_path,
                                engine='xlsxwriter')
        self.df.to_excel(writer,
                         sheet_name='Sheet1')
        writer.save()
