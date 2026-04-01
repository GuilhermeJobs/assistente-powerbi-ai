import os
import streamlit as st
from groq import Groq

# Configura a página do Streamlit
st.set_page_config(
    page_title="Assistente AI Power BI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>

        [data-testid="stSidebarUserContent"] div.stButton > button {
            background-color: #b16758;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px;
            transition: all 0.3s ease;
        }

        [data-testid="stSidebarUserContent"] div.stButton > button:hover {
            background-color: #d32f2f;
            transform: translateY(-3px); /* Efeito suave de levante */
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
    </style>
""", unsafe_allow_html=True)

CUSTOM_PROMPT = """
Você é o "Assistente AI Power BI", um especialista sênior em Business Intelligence, focado em DAX, Linguagem M e Modelagem de Dados (Star Schema).

SUA MISSÃO:
Auxiliar analistas iniciantes e intermediários com soluções performáticas, claras e tecnicamente impecáveis.

REGRAS DE OURO:
1. **Contexto de Cálculo**: Sempre especifique se a solução proposta deve ser criada como uma **Medida**, **Coluna Calculada** ou **Tabela Calculada**. Explique o porquê da escolha (ex: performance ou contexto de filtro).
2. **Linguagem M vs DAX**: Se o problema for limpeza de dados, priorize Linguagem M (Power Query). Se for análise dinâmica, use DAX.
3. **Padrão de Resposta**:
    * **Conceito**: Explique a lógica por trás da solução (ex: o que o CALCULATE está fazendo com o filtro).
    * **Bloco de Código**: Use blocos de código formatados (ex: ```dax ou ```powerquery).
    * **Comentários**: O código deve conter comentários explicativos nas linhas principais.
    * **Boas Práticas**: Sugira o uso de variáveis (VAR/RETURN) no DAX para melhor legibilidade e performance.
4. **Documentação**: Finalize sempre com o link da documentação oficial da Microsoft: https://learn.microsoft.com/pt-br/power-bi/
5. **Restrição**: Se a pergunta não for sobre Power BI, Ecossistema Microsoft Fabric ou análise de dados correlata, decline educadamente.
"""

# Barra Lateral
with st.sidebar:
    st.title("📊 Configurações")
    
    groq_api_key = st.text_input(
        "Insira sua API Key Groq", 
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de Power BI. IA pode cometer erros. Sempre verifique as respostas!")
    st.markdown("Compatilhe com seus amigos analistas de dados.")
    
    st.markdown("---")
    st.link_button("👨🏻‍💻 Desenvolvido por Guilherme Ferreira", "https://www.linkedin.com/in/guilherme-ferreira-952579184/", use_container_width=True)

    st.markdown("---")
    if st.button("🗑️ Limpar Histórico de Conversa", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Título Principal
st.title("Assistente Pessoal de Power BI 🤖")
st.caption("Especialista em DAX, Linguagem M e Modelagem de Dados.")

# Inicializa o histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens do histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Processamento do Chat
if prompt := st.chat_input("Qual sua dúvida no Power BI?"):
    
    if not groq_api_key:
        st.warning("Por favor, insira sua API Key da Groq na barra lateral.")
        st.stop()

    # Adiciona pergunta do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Chamada para o Llama 3 na Groq
    with st.chat_message("assistant"):
        with st.spinner("Consultando base de conhecimento..."):
            try:
                client = Groq(api_key=groq_api_key)
                
                # Preparação do histórico para a API
                messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
                for msg in st.session_state.messages:
                    messages_for_api.append(msg)

                # ALTERAÇÃO: Modelo Llama 3 (70B para maior precisão ou 8B para velocidade)
                chat_completion = client.chat.completions.create(
                    messages=messages_for_api,
                    model="meta-llama/llama-4-scout-17b-16e-instruct", # Modelo Llama 3 robusto
                    temperature=0.2,          # Temperatura baixa = Respostas mais técnicas e precisas
                    max_tokens=2048,
                )
                
                response = chat_completion.choices[0].message.content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

            except Exception as e:
                st.error(f"Erro na API Groq: {e}")

# Rodapé
st.markdown(
    """
    <div style="text-align: center; color: gray; margin-top: 50px;">
        <hr>
        <p>© 2026 Guilherme Ferreira - Foco em Inteligência de Dados</p>
    </div>
    """,
    unsafe_allow_html=True
)