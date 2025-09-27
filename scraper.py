import requests
import pandas as pd


# Ela já deve conter todos os filtros (jobName, city, etc.).
full_api_url = 'https://employability-portal.gupy.io/api/v1/jobs?jobName=python'


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://portal.gupy.io',
    'Referer': 'https://portal.gupy.io/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v-="140"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"'
}

print("Buscando vagas com a URL completa e final...")


response = requests.get(full_api_url, headers=headers)

if response.status_code == 200:
    dados = response.json()
    print("Dados recebidos com sucesso!")

    lista_de_vagas = []
    if 'data' in dados and dados['data']:
        for vaga in dados['data']:
            titulo = vaga.get('name', 'N/A')
            empresa = vaga.get('companyName', 'N/A')
            local = f"{vaga.get('city', '')}, {vaga.get('state', '')}"
            link = vaga.get('jobUrl', 'N/A')
            tipo_vaga = vaga.get('type', 'N/A')

            lista_de_vagas.append({
                'Titulo': titulo,
                'Empresa': empresa,
                'Local': local,
                'Tipo': tipo_vaga,
                'Link': link
            })
        
        print(f"{len(lista_de_vagas)} vagas encontradas! Salvando em CSV...")
        df = pd.DataFrame(lista_de_vagas)
        df.to_csv('vagas_gupy_api.csv', index=False, encoding='utf-8-sig')
        print("Tudo pronto! Seu arquivo 'vagas_gupy_api.csv' foi criado com sucesso.")
    else:
        print("A API respondeu com sucesso, mas não retornou vagas para essa busca.")
else:
    print(f"ERRO ao acessar a API. Status Code: {response.status_code}")
    print("Resposta da API:")
    print(response.text)