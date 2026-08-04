# E140EIP

## Descrição

Vendas - Exclusões de Notas Fiscais de Saída

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| PedPal | Number(008,0) | Sim | Número do pedido no Palmtop |
| NumPed | Number(008,0) | Sim | Número do pedido que gerou a  nota fiscal de saída |
| SeqIpd | Number(004,0) | Sim | Sequência do item no pedido da nota fiscal de saída |
| CodRep | Number(009,0) | Sim | Código do representante da nota fiscal de saída |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
