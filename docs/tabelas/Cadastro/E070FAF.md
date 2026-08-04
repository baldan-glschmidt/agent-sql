# E070FAF

## Descrição

Cadastros - Filiais - Filiais atendidas pela filial de assistência técnica

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SeqFaf | Number(003,0) | Não | Sequência do item |
| FilAtd | Number(005,0) | Não | Filial atendida pela filial assistência técnica |
| DepAtv | String(010) | Sim | Depósito de assistência técnica para armazenar os produtos com defeito. |
| OnfEpc | Number(004,0) | Sim | Operação de nota fiscal para notas fiscais de entrada para conserto. |
| OnfRpc | Number(004,0) | Sim | Operação de nota fiscal para notas fiscais de remessa para conserto. |
| OnfRce | Number(004,0) | Sim | Operação de nota fiscal para notas fiscais de retorno de conserto externo. |
| OnfRcc | Number(004,0) | Sim | Operação de nota fiscal para notas fiscais de retorno de conserto para cliente. |
| OnfTef | Number(004,0) | Sim | Operação de nota fiscal para transferência entre filiais. |
| OnfEpt | Number(004,0) | Sim | Operação de nota fiscal para entrada por troca de mercadoria. |
| OnfSpt | Number(004,0) | Sim | Operação de nota fiscal para saída por troca de mercadoria. |

---

## Chave Primária

- CodEmp
- CodFil
- SeqFaf

---

## Índices

### E070FAFIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- FilAtd

---

## Relacionamentos

### IR_E070FAF_003

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| FilAtd | CodFil |

