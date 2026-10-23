# R047LFT

## Descrição

Faturas Lançadas

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodFat | Number(004,0) | Não | Código da definição da Fatura |
| CmpFat | Date | Não | Competência da Fatura |
| SeqFat | Number(003,0) | Não | Sequência da Fatura |
| VncFat | Date | Sim | Vencimento da Fatura |
| VlrFat | Number(011,2) | Sim | Valor da Fatura |
| NumTit | String(030) | Sim | Número do Título |

---

## Chave Primária

- NumEmp
- CodFil
- CodFat
- CmpFat
- SeqFat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R047LFT_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R047LFT_002

**Tabela:** R047FAT

| Origem | Destino |
|--------|---------|
| CodFat | CodFat |

