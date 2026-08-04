# E120DEF

## Descrição

Vendas - Pedidos - Defensivo Agrícula

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqDef | Number(003,0) | Não | Sequência do defensivo agrícula |
| NumRec | String(030) | Sim | Número do Receituário |
| CpfTec | String(011) | Sim | Número do CPF do responsável técnico pela emissão do receituário |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqDef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120DEF_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

