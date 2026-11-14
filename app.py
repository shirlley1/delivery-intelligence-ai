
import streamlit as st

st.set_page_config(
    page_title="Delivery Intelligence AI",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 Delivery Intelligence AI")
st.subheader("Assistente inteligente para ocorrências de delivery")

st.write(
    "Descreva o problema relatado pelo cliente. "
    "O sistema identificará a ocorrência e recomendará um encaminhamento."
)

relato = st.text_area(
    "Qual foi o problema relatado pelo cliente?",
    placeholder="Ex.: Meu pedido está atrasado e ainda não chegou..."
)

def analisar_ocorrencia(texto):
    texto = texto.lower()

    if "não recebi" in texto or "nao recebi" in texto or "não chegou" in texto or "nao chegou" in texto:
        return (
            "Pedido não recebido",
            "Alta",
            "Consultar os registros da entrega e encaminhar para análise humana."
        )

    elif "faltando" in texto or "incompleto" in texto:
        return (
            "Pedido incompleto",
            "Média",
            "Verificar os itens do pedido e orientar o cliente pelo canal oficial."
        )

    elif "errado" in texto or "diferente" in texto:
        return (
            "Item incorreto",
            "Média",
            "Conferir os itens solicitados e os itens entregues."
        )

    elif "atrasado" in texto or "demorando" in texto or "atraso" in texto:
        return (
            "Atraso na entrega",
            "Média",
            "Consultar o status do pedido e verificar a previsão atualizada."
        )

    elif "danificado" in texto or "quebrado" in texto:
        return (
            "Produto danificado",
            "Alta",
            "Solicitar análise do caso e encaminhar ao suporte responsável."
        )

    else:
        return (
            "Ocorrência não identificada",
            "Indeterminada",
            "Coletar mais informações e encaminhar para análise humana."
        )

if st.button("Analisar ocorrência"):
    if relato.strip():
        categoria, prioridade, acao = analisar_ocorrencia(relato)

        st.divider()
        st.subheader("Resultado da análise")

        st.write("**Categoria:**", categoria)
        st.write("**Prioridade:**", prioridade)
        st.write("**Ação recomendada:**", acao)
        st.info("Esta é uma classificação inicial baseada em regras. Casos reais precisam de validação humana.")
    else:
        st.warning("Digite uma ocorrência antes de analisar.")
