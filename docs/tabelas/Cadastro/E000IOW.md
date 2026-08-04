# E000IOW

## Descrição

Tabelas - Integrações - Itens de ordens de separação/recebimento

---

## Resumo

- Campos: 31
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumOrd | String(020) | Não | Número da ordem de separação/recebimento |
| SeqIto | Number(004,0) | Não | Sequência do item da ordem de separação/recebimento |
| CodPro | String(014) | Não | Código do produto do pedido |
| CodDer | String(007) | Não | Código da derivação do produto do pedido |
| CodDep | String(010) | Não | Código do depósito a ser baixado o estoque do produto do pedido |
| FilAne | Number(005,0) | Sim | Código da filial da análise de embarque |
| NumAne | Number(012,0) | Sim | Número da análise de embarque |
| NumPfa | Number(009,0) | Sim | Número da pré-fatura |
| SeqPes | Number(003,0) | Sim | Sequência do item na pré-fatura |
| FilNfc | Number(005,0) | Sim | Código da filial da nota fiscal de entrada |
| CodFor | Number(009,0) | Sim | Fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Sim | Número da nota fiscal de entrada |
| SnfNfc | String(003) | Sim | Código da série da nota fiscal de entrada |
| SeqIpc | Number(003,0) | Sim | Sequência do item da nota fiscal de entrada |
| FilNfv | Number(005,0) | Sim | Código da filial da nota fiscal de saída |
| SnfNfv | String(003) | Sim | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Sim | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Sim | Sequência do item de produto na nota fiscal de saída |
| FilPed | Number(005,0) | Sim | Código da filial do pedido |
| NumPed | Number(008,0) | Sim | Número do pedido |
| SeqIpd | Number(004,0) | Sim | Sequência do item do pedido |
| DatMov | Date | Sim | Data da movimentação do estoque |
| SeqMov | Number(006,0) | Sim | Sequência de movimento na data de movimentação |
| QtdOrd | Number(014,5) | Sim | Quantidade do item na ordem de separação/recebimento |
| QtdFis | Number(014,5) | Sim | Quantidade física do item no depósito |
| SitIto | Number(001,0) | Não | Situação do item da ordem de separação/recebimento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- NumOrd
- SeqIto

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
