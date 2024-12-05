import streamlit as st
import base64
import pandas as pd

# Função para carregar imagem de fundo
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background("irisrosa.png")

# Estilo personalizado
st.markdown(
    """
    <style>
    .custom-bg {
        background-color: #DEB887;  /* Tan */
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="custom-bg">ʕ •ᴥ•ʔ</div>', unsafe_allow_html=True)

# Armazenar dados dos usuários
users_db = {}

# Função para registrar um novo usuário
def register_user(username, password):
    if username in users_db:
        st.error("Usuário já existe.")
        return False
    users_db[username] = password
    st.success("Usuário cadastrado com sucesso!")
    return True

# Abas do app
abas = st.tabs(["Tela inicial", "Dados pessoais", "Calendário de Festas", "Lista", "Local e Pessoas", "Tema", "Comida e Bebida", "Especiais", "Entretenimento", "Tabela"])

# Aba inicial
with abas[0]:  #Tela Inicial
    st.title(" Seja bem-Vindo")
  
 
    st.image("niver.png", width=900) 
    #st.image("niver.png", height=700)  

    st.write(" Este aplicativo foi desenvolvido com o objetivo de auxiliar pequenas empresas na organização de festas infantis. Após o preenchimento de todas as abas do sistema, a tabela com os dados deve ser gerada e enviada para o e-mail presente na lista de afazeres. Em seguida, a equipe da empresa entrará em contato, por telefone, para confirmar os detalhes e oferecer o suporte necessário.")
#Aba dados pessoais
with abas[1]:
    st.title("Dados pessoais")
    nome= st.text_input("Digite seu nome aqui:")
    numero= st.text_input("Digite seu numero aqui:")


# Aba do Calendário
with abas[2]:  # Aba de Calendário de Festas
    st.title("Calendário de Festas")
    
    if 'festas' not in st.session_state:
        st.session_state.festas = []

    data = st.date_input("Selecione a data da festa", format="DD/MM/YYYY", key="data_input")
    hora = st.time_input("Selecione a hora da festa", key="hora_input")

    data_existente = any(festa['data'] == data for festa in st.session_state.festas)

    if st.button("Adicionar Festa", key="adicionar_festa"):
        if data_existente:
            st.error("Não é possível agendar uma festa nesse dia. Já existe uma festa marcada.")
        else:
            st.session_state.festas.append({'data': data, 'hora': hora})
            st.success("Festa adicionada com sucesso!")
            print("Cadastro feito com sucesso: Festa agendada para", data, "às", hora)

    if st.session_state.festas:
        festas_df = pd.DataFrame(st.session_state.festas)
        st.subheader("Festas Agendadas")
        st.table(festas_df)

# Aba de Lista
with abas[3]:
    st.title("Lista de Tarefas")

    if 'tarefas' not in st.session_state:
        st.session_state.tarefas = [
            "Fazer os convites",
            "Pedir confirmação da festa aos convidados",
            "Lembrancinhas",
            "Fotógrafo",
            "Escolher o tema",
            "Escolher as comidas e bebidas",
            "Escolher entretenimento", 
            "Escolher o dia e o horário (certificar que não há outra festa no mesmo dia)",
            "Enviar Tabela final para a Empresa",
            "Atender ligação da agência para confirmação de valores"
        ]

    tarefas_concluidas = 0

    for tarefa in st.session_state.tarefas:
        if st.checkbox(tarefa, key=tarefa):  # Checkbox com texto da tarefa
            st.markdown(f"~{tarefa}~")  # Riscando a tarefa
            tarefas_concluidas += 1
            print(f"Tarefa riscada: {tarefa}")  # Mensagem no console

    total_tarefas = len(st.session_state.tarefas)
    tarefas_pendentes = total_tarefas - tarefas_concluidas
    print(f"Tarefas pendentes: {tarefas_pendentes}")  

    st.text("Convites: (32) 99812-3455")
    st.text("Lembrancinhas: (32) 99809-8765")
    st.text("Agência - número: 34567")
    st.text("Mandar tabela final: e-mail @partykids.vertentes.gmail.com.br")

# Aba de Local e Pessoas

with abas[4]:
    st.title("Local e Pessoas")
     
    convidados = st.number_input("Quantas pessoas vão vir?", min_value=1)
    local = st.selectbox("Escolha o local da festa:", [
        "Espaço Gold",
        "Paradise", 
        "Acampamento", 
        "Jardim Encantado",
        "Sítio Pássaro Azul"
    ])
    st.image("locais.png")

#Aba de Tema
with abas[5]:
    st.title("Tema")

    paleta_cores = st.selectbox("Escolha a paleta de cores da festa:", [
        "Rosa Claro/Pink", "Tons quentes", "Lilas/Azul", 
        "Azul Claro/Azul Escuro", "Tons de verde", "Nenhum Acima"
    ])
    paleta_cores_personalizado = st.text_input("Qual paleta de cores você deseja caso nenhuma acima atenda seu desejo?")
    tema = st.text_input("Qual o tema da festa?")

# Aba de Comida e Bebida
with abas[6]:
    st.title("Comida e Bebida")

    sabor_bolo = st.selectbox("Escolha o sabor do bolo:", [
        "Brigadeiro", "Ninho", "Doce de leite", 
        "Nutella", "Frutas vermelhas", "Limão", 
        "Mousse de Maracujá", "Doce de leite com pêssego", "Personalizado"
    ])
    bolo_personalizado = st.text_input("Como você deseja o bolo personalizado caso nenhum acima atenda seu desejo?")
    
    tipos_salgado = st.multiselect("Escolha os Salgados:", [
        "Coxinha", "Bolinha de queijo", "Bolinha de pizza", 
        "Risole de queijo e calabresa", "Risole de Frango", 
        "Cigarrete", "Pastel de carne", "Pastel de queijo", 
        "Pastel de pizza", "Kibe"
    ])
    
    tipos_drinks = st.multiselect("Escolha de bebida:", [
        "Suco de uva", "Suco de laranja", "Suco de maçã", 
        "Suco de limão", "Suco de pêssego", "Refrigerante de laranja", 
        "Refrigerante de uva", "Coca-cola", "Guaraná", "Sprite"
    ])

with abas[7]: 
    st.title("Especiais")

    especiais_personalizado = st.text_input("Em caso de restrições alimentares, diga aqui:")

# Aba de Entretenimento
with abas[8]:
    st.title("Entretenimento")

    tipos_entretenimento = st.multiselect("Escolha as formas de entretenimento:", [
        "Pintura facial", "Mágico", "Brincadeiras Tradicionais", 
        "Oficina de Artesanato", "Palhaço", "Animador", 
        "Show de fantoches", "Contação de histórias", 
        "Caça Tesouro", "Shows Musicais", "Karaokê", 
        "Brinquedos infláveis"
    ])

# Aba de Tabela 
with abas[9]:
    st.title("Tabela ")

    if st.button("Salvar Informações"):
        informacoes = {        
            "convidados": convidados,
            "local": local,
            "paleta_cores": paleta_cores,
            "paleta_cores_personalizado": paleta_cores_personalizado,
            "tema": tema,
            "sabor_bolo": sabor_bolo,
            "bolo_personalizado": bolo_personalizado,
            "tipos_salgado": tipos_salgado,
            "tipos_drinks": tipos_drinks,	  
	     "especiais_personalizado": especiais_personalizado,
            "tipos_entretenimento": tipos_entretenimento,
        }

        dados_festa = {
            "Campo": [
                "Nome", "Numero", "Data", "Hora", "Convidados", "Local", "Paleta de Cores",
                "Paleta de Cores (Personalizado)", "Tema da Festa", 
                "Sabor do Bolo", "Bolo (Personalizado)", 
                "Tipos de Salgados", "Tipos de Bebidas", "Comidas Especiais(personalizado)",
		 "Entretenimento"
            ],
            "Informação": [
                nome, numero, data, hora, convidados, local, paleta_cores,
                paleta_cores_personalizado, tema, sabor_bolo,
                bolo_personalizado, ', '.join(tipos_salgado), 
                ', '.join(tipos_drinks), especiais_personalizado, ', '.join(tipos_entretenimento)
            ]
        }

        st.success("Informações salvas com sucesso!")
        st.write("Informações da festa:")
        st.table(pd.DataFrame(dados_festa))

     # Calculando Gastos da Festa 


#valor_estipulado = st.number_input("Valor estipulado:", min_value=0.0)
#valor_inicial = st.number_input("Valor inicial:", min_value=0.0)
#gastos = st.number_input("Total de gastos:", min_value=0.0)

#if st.button("Calcular"):
 #   troco = valor_inicial - gastos
  #  st.write("Troco:", troco)
#if st.button("Desistir da Festa"):
 #   st.session_state.gastos = {
  #      'valor_estipulado': 0.0,
   #     'valor_inicial': 0.0,
    #    'total_gastos': 0.0,
     #   'desistiu': True
    #}
    #st.success("Você desistiu da festa")