import streamlit as st
import requests
import json

st.set_page_config(
    layout="wide",
    page_title="App Mivus"
)

def mostrar_consulta_cnpj_dominio():
    st.title("Consultor de CNPJ e Domínio")

    col1, col2 = st.columns(2)
    
    # Inserir CNPJ
    col1.subheader("Consultar CNPJ")
    cnpj_input = col1.text_input("Digite o CNPJ:", "").replace(".", "").replace("-", "").replace("/", "").replace(" ", "")
    if col1.button("Consultar CNPJ"):
        if cnpj_input:
            consulta_cnpj(cnpj_input)
        else:
            col1.warning("Por favor, digite um CNPJ válido.")

    # Inserir Domínio
    col2.subheader("Consultar Domínio")
    dominio_input = col2.text_input("Digite o domínio:")
    if col2.button("Consultar Domínio"):
        if dominio_input:
            consultar_rdap(dominio_input)
        else:
            col2.warning("Por favor, digite um domínio válido.")

    st.markdown("---") 




#Função de Consultar CNPJ
def consulta_cnpj(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX", "cnpj": "06990590000123", "plugin": "RF"} # coloque sua token válida aqui!
    response = requests.request("GET", url, params=querystring)

    if response.status_code == 200:
        resp = json.loads(response.text)

        data_abertura = resp.get('abertura', 'Não disponível')
        situacao = resp.get('situacao', 'Não disponível')
        nome_fantasia = resp.get('fantasia', 'Não disponível')
        porte = resp.get('porte', 'Não disponível')
        complemento = resp.get('complemento', '')
        data_situacao = resp.get('data_situacao', 'Não disponível')
        numero_socios = len(resp.get('qsa', []))  

        st.markdown("---") 

        st.header(f"Informações da Empresa - CNPJ: {resp.get('cnpj', 'Não encontrado')}")

        st.subheader("Dados principais:")
        st.write(f"Nome: {resp.get('nome', 'Não disponível')}")
        st.write(f"Nome Fantasia: {nome_fantasia}")
        st.write(f"Data de Abertura: {data_abertura}")
        st.write(f"Situação: {situacao}")
        st.write(f"Porte: {porte}")
        
        st.subheader("Endereço:")
        st.write(f"{resp.get('logradouro', '')}, {resp.get('numero', '')} {complemento} - {resp.get('bairro', '')} - {resp.get('municipio', '')} ({resp.get('uf', '')}) - CEP: {resp.get('cep', '')}")

        st.subheader("Outras Informações:")
        st.write(f"Atividade Principal: {resp.get('atividade_principal', [{}])[0].get('text', 'Não disponível')}")
        st.write(f"E-mail: {resp.get('email', 'Não disponível')}")
        st.write(f"Telefone: {resp.get('telefone', 'Não disponível')}")
        st.write(f"Data da Situação: {data_situacao}")
        st.write(f"Número de Sócios: {numero_socios}")

        # Encontrar e exibir o administrador
        st.subheader("Administrador:")
        administrador = None
        for socio in resp.get('qsa', []):
            if "administrador" in socio['qual'].lower():
                administrador = socio['nome']
                break

        if administrador:
            st.write(administrador)
        else:
            st.write("Nenhum administrador encontrado.")

        st.subheader("Sócios:")
        if numero_socios > 0:
            for socio in resp['qsa']:
                st.write(f"- {socio['nome']} ({socio['qual']})")
        else:
            st.write("Nenhum sócio encontrado.")

    elif response.status_code == 404:
        st.error("CNPJ não encontrado.")
    else:
        st.error("Ocorreu um erro ao consultar o CNPJ. Verifique o CNPJ e tente novamente.")

#Função de Consultar Domínio
def consultar_rdap(dominio):
    url = f"https://rdap.registro.br/domain/{dominio}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()

        # Extraindo os dados desejados
        nome_dominio = dados['handle']
        status = dados['status'][0]

        # Percorrendo as entidades para encontrar o registrante
        for entidade in dados['entities']:
            if 'roles' in entidade and 'registrant' in entidade['roles']:
                razao_social = entidade['vcardArray'][1][2][2]
                handle_registrante = entidade['handle']
                representante_legal = entidade.get('legalRepresentative', 'Não informado')
                
                # Verificando se o CNPJ/CPF está presente
                cnpj_cpf = 'Não informado'
                if 'publicIds' in entidade:
                    for public_id in entidade['publicIds']:
                        if public_id['type'] in ('cnpj', 'cpf'):
                            cnpj_cpf = public_id['identifier']
                break
        
        # Exibindo os dados utilizando elementos do Streamlit
        st.markdown("---") 
        st.header(f"Informações do domínio {dominio}:")
        st.markdown(f"**Nome do Domínio:** {nome_dominio}")
        st.markdown(f"**Status:** {status}")
        st.markdown(f"**Razão Social:** {razao_social}")
        st.markdown(f"**CNPJ/CPF:** {cnpj_cpf}")
        st.markdown(f"**Handle do Registrante** {handle_registrante}")
        st.markdown(f"**Representante Legal:** {representante_legal}")

    else:
        st.error(f"Erro ao consultar o domínio: {resposta.status_code}")



mostrar_consulta_cnpj_dominio()




