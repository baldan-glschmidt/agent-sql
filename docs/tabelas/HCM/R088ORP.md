# R088ORP

## Descrição

Solicitações de Oficina - Itens de Orçamento

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSol | Number(006,0) | Não | Código da Solicitação de Oficina |
| CodOem | Number(008,0) | Não | Código da Empresa que Gerou o Orçamento |
| CodPec | Number(006,0) | Não | Código da Peça/Serviço Orçado na Solicitação |
| QtdPec | Number(008,2) | Sim | Quantidade de Peça / Serviço |
| ValPec | Number(011,2) | Sim | Valor da Peça ou Serviço Orçado |
| ApvOrp | String(001) | Sim | Item do Orçamento Aprovado |

---

## Chave Primária

- CodSol
- CodOem
- CodPec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088ORP_000

**Tabela:** R088SOF

| Origem | Destino |
|--------|---------|
| CodSol | CodSol |

### IR_R088ORP_001

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

### IR_R088ORP_002

**Tabela:** R088PEC

| Origem | Destino |
|--------|---------|
| CodPec | CodPec |

