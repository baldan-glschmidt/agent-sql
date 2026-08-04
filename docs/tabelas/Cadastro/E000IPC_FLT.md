# E000IPC_FLT

## Descrição

Tabelas - Integração - Notas Fiscais de Entrada - Itens da folha do leite

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumInt | String(020) | Não | Número do Documento Externo (Integrado) |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| CodPro | String(014) | Não | Código do produto da nota fiscal de entrada |
| CodDer | String(007) | Sim | Código da derivação do produto da nota fiscal de entrada |
| QtdRec | Number(014,5) | Sim | Quantidade recebida do item da nota fiscal de entrada |
| PesBru | Number(021,10) | Sim | Peso bruto do item da nota fiscal de entrada |
| PesLiq | Number(021,10) | Sim | Peso líquido do item da nota fiscal de entrada |
| PreUni | Number(021,10) | Sim | Preço unitário do item da nota fiscal de entrada |
| VlrLiq | Number(015,2) | Sim | Valor líquido do item da nota fiscal de entrada |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumInt
- SeqIpc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
