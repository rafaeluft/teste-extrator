import glob
from extrator import extrair_emails, EmailNotFoundError

def print_emails(lista_emails):
    """
    Imprime os endereços de e-mail da lista.

    Args:
        lista_emails (list): Uma lista de strings contendo endereços de e-mail.

    Exemplo:
        >>> lista = ["john@example.com", "jane@example.com"]
        >>> print_emails(lista)
        john@example.com
        jane@example.com
    """
    for email in lista_emails:
        print(email)

def extrai_emails_from_path(path="./"):
    """
    Extrai e imprime os endereços de e-mail de arquivos de texto em um diretório e subdiretórios.

    Args:
        path (str, optional): O diretório raiz a ser pesquisado em busca de arquivos de texto.
            O padrão é o diretório atual.

    Exemplo:
        >>> extrai_emails_from_path("/caminho/para/diretorio")
        # (saída depende dos arquivos de texto encontrados)
    """
    for file_path in glob.glob(f"{path}/**/*.txt", recursive=True):
        try:
            with open(file_path) as txt_file:
                msg = txt_file.read()
                print_emails(extrair_emails(msg))
        except EmailNotFoundError:
            print(f"Nenhum email encontrado em: {file_path}")
