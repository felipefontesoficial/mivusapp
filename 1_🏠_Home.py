import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="App Mivus"
)


logo = "caminho_para_sua_logo.png" 
st.sidebar.image(logo, use_column_width=True)
st.sidebar.write("Feito por: [Mivus Academy](https://www.mivus.com.br)")

st.title("Olá, Querido Lendário 😀")
st.write("Agora, tudo o que você precisa estará organizado em um só lugar.")

st.markdown("---") # Separador

#Título da Coluna

col1, col2 = st.columns([0.7, 0.3])
col1.subheader(":balloon: Desafio 70 Leads em 1 Semana ")
col2.write("**Data:** 02/12 à 06/12/2024")

st.write("\n") #Espaço em branco


# Apresentação do desafio

st.markdown("""**Regras do Desafio:**

Você deverá prospectar 70 Clientes em 1 Semana.

Todos os dias, ao final do dia ( 17:30h ) você deverá mostrar sua comprovação de abordagens diárias. ( *Tire print do relatório do seu CRM e mande no grupo* )

**Recomendação:** Faça 15 abordagens por dia, e na sexta faça apenas 10. 

*Conta como abordagem:* Ligação, E-mail, Mensagem do WhatsApp. Seja primeiro contato ou Follow Up. 

**Premiação:**

- **Aula** Ao Vivo Exclusiva Sobre Copy
- **Gravação** de Ligações de Prospecção da Mivus
- **Bastidores** de Uma Venda ( Analisando Copy )
- **Acesso** ao Novo Roteiro de Prospecção Mivus""")
