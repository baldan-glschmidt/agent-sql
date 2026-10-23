# R034APP

## Descrição

PPP Rubi -  Atividades do Colaborador

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatIni | Date | Não | Data do início da atividade do colaborador |
| CodAtv | Number(004,0) | Não | Código da atividade |
| CodAgt | Number(004,0) | Não | Código do Agente |
| CodGfi | Number(002,0) | Sim | Código de GFIP |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- CodAtv
- CodAgt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034APP_003

**Tabela:** R034PPP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatIni | DatIni |

