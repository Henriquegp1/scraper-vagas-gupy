# scraper-vagas-gupy
"Script em Python que coleta vagas de tecnologia da API da Gupy.
# 🚀 Web Scraper de Vagas da Gupy (via API)

Este projeto é um web scraper em Python que coleta vagas de tecnologia diretamente da API da Gupy, contornando a necessidade de raspar o HTML de um site dinâmico.

## A Jornada do Projeto

O desenvolvimento deste scraper foi um grande aprendizado em depuração de aplicações web. O desafio inicial de raspar um site carregado com JavaScript me levou a investigar a comunicação de rede da plataforma. Utilizando as Ferramentas de Desenvolvedor do Chrome, fui capaz de identificar, analisar e replicar a chamada de API exata que o site usa para buscar e exibir as vagas, resultando em um scraper muito mais rápido, eficiente e robusto.

## Tecnologias Utilizadas
* Python
* Requests (para fazer chamadas à API)
* Pandas (para estruturar e salvar os dados em .csv)

## Como Usar
1. Clone este repositório: `git clone https://github.com/SEU_USUARIO/scraper-vagas-gupy.git`
2. Crie e ative um ambiente virtual: `python -m venv venv` e `.\venv\Scripts\activate`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute o script: `python scraper.py`
5. O resultado será salvo no arquivo `vagas_gupy_api.csv`.
