# 📊 Assistente AI Power BI (Llama 4 + Groq)
Este é um agente de Inteligência Artificial desenvolvido em Python e Streamlit, projetado especificamente para auxiliar analistas de dados (do iniciante ao intermediário) no ecossistema de Power BI.

O foco principal do assistente é fornecer suporte técnico preciso em DAX, Linguagem M e Modelagem de Dados (Star Schema), utilizando o poder de processamento do modelo Llama 4 via Groq API.

https://assistente-powerbi-ai.streamlit.app/

# 🎯 Objetivo do Projeto
Transformar a curva de aprendizado de novos analistas de BI. O assistente não apenas entrega o código, mas explica a lógica por trás da solução, diferenciando contextos de filtro e de linha, e promovendo as melhores práticas de desenvolvimento (como o uso de variáveis VAR/RETURN).

# 🚀 Tecnologias Utilizadas
Python: Linguagem base para a lógica do agente.
Streamlit: Framework para criação da interface web interativa e responsiva.
Llama 4: Modelo de linguagem de última geração para raciocínio lógico e geracional de código.
Groq Cloud: Infraestrutura de inferência ultra-rápida (LPU) para respostas quase instantâneas.
Custom Prompt Engineering: Instruções avançadas para garantir que o modelo se comporte como um Consultor Sênior de BI.

# ✨ Funcionalidades Principais
Explicação Didática: Conceituação de funções DAX e transformações no Power Query.
Geração de Código Inteligente: Exemplos práticos com sintaxe correta e comentários.
Contexto de Cálculo: Orientação clara se a solução deve ser aplicada como Medida ou Coluna Calculada.
Interface Customizada: Sidebar com botões de ação e design focado em UX.
Histórico Persistente: Mantém o contexto da conversa durante a sessão.
Botão de Limpeza Rápida: Reset imediato do chat para novas consultas.

# 🛠️ Como Executar o Projeto
Clone o repositório:
git clone https://github.com/GuilhermeJobs/assistente-powerbi-ai/
cd assistente-powerbi-ai/

Instale as dependências:
pip install -r requirements.txt
Obtenha uma API Key da Groq:
Acesse console.groq.com e gere sua chave gratuita.

Execute o App:
streamlit run app.py

# 🏗️ Estrutura de Arquivos
app.py: Código principal com a interface e lógica da IA.
requirements.txt: Lista de bibliotecas necessárias para o deploy.

# 👨‍💻 Desenvolvedor
Guilherme Ferreira

Aviso: Este assistente utiliza Inteligência Artificial. Sempre valide as fórmulas DAX e transformações de dados em um ambiente de homologação antes de aplicar em produção.
