# R096REC

## Descrição

Resumo de EPIs por Colaborador

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodEpi | Number(008,0) | Não | Código do Epi |
| DatEnt | Date | Não | Data da Entrega |
| DatVal | Date | Não | Data de Validade |
| DatRev | Date | Não | Data de Revisão |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodEpi
- DatEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R096REC_003

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

