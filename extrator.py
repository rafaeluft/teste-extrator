import re

class EmailNotFoundError(Exception):
    """Exceção customizada para indicar que nenhum email foi encontrado."""

def extrair_emails(texto):
    """
    Extrai endereços de e-mail de um texto usando expressões regulares.

    Args:
        texto (str): O texto no qual os endereços de e-mail serão procurados.

    Returns:
        list: Uma lista de strings contendo os endereços de e-mail encontrados no texto.

    Raises:
        EmailNotFoundError: Se nenhum endereço de e-mail for encontrado no texto.

    Exemplo:
        >>> texto = "Meu endereço de email é john.doe@example.com. Entre em contato."
        >>> extrair_emails(texto)
        ['john.doe@example.com']
    """
    # Usando uma expressão regular para encontrar endereços de e-mail
    padrao_email = r'([A-Za-z0-9_]+@[A-Za-z0-9_]+\.[a-z]{2,3}(\.[a-z]{2})?)'
    emails_encontrados = re.findall(padrao_email, texto)
    if len(emails_encontrados) == 0:
        raise EmailNotFoundError("Não encontrei emails.")
    return [email[0] for email in emails_encontrados]
