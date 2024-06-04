# Automação de Testes do Blog do Agi

Este projeto automatiza a pesquisa de artigos no blog do Agi utilizando Selenium e Pytest. Os testes são executados automaticamente via GitHub Actions.

## Configuração do Ambiente

### Pré-requisitos

- Python 3.8+
- pip (Python package installer)

### Instalando as Dependências

1. Clone o repositório:

    ```bash
    git clone https://github.com/ab2m/automacao-testes-blogdoagi.git
    cd automacao-testes-blogdoagi
    ```

2. Crie um ambiente virtual e ative-o (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

## Executando os Testes

### Localmente

Para executar os testes localmente:

1. Verifique o estilo do código:

    ```bash
    flake8 tests/
    black --check tests/
    ```

2. Execute os testes:

    ```bash
    pytest --cov=tests --cov-report=html --maxfail=1 --disable-warnings
    ```

### Em Paralelo

Para executar os testes em paralelo, use o plugin `pytest-xdist`:

```bash
pytest -n auto --dist=loadscope