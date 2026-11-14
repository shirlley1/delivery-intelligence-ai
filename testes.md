# Testes do Delivery Intelligence AI

## Objetivo
Avaliar como o assistente de IA identifica, classifica e recomenda encaminhamentos para ocorrências fictícias de delivery.

## Teste 01 — Pedido incompleto

**Relato:** O cliente informa que recebeu o pedido com dois itens faltando.

**Classificação:** Pedido incompleto.

**Prioridade:** Média.

**Resultado esperado:** Identificar os itens ausentes, solicitar informações necessárias e recomendar a consulta aos detalhes do pedido.

## Teste 02 — Atraso na entrega

**Relato:** O cliente informa que a entrega está muito atrasada e demonstra irritação.

**Classificação:** Atraso na entrega.

**Prioridade:** Média, sujeita à confirmação do tempo de atraso e do status do pedido.

**Resultado esperado:** Consultar o status atualizado, identificar a causa do atraso quando disponível e orientar o encaminhamento adequado.

## Aprendizado dos testes

Os testes demonstraram que a IA pode organizar relatos em categorias, identificar informações faltantes e sugerir próximos passos.

Uma melhoria necessária é estabelecer critérios mais objetivos para a classificação de prioridade.

## Limitações

- Os cenários são fictícios.
- Não há conexão com pedidos reais.
- As recomendações não foram validadas em uma operação real.
- Os resultados representam experimentações iniciais com IA generativa.
