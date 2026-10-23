# R042REC

## Descrição

Rescisão - Empréstimos Consignados

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| SeqEmp | Number(002,0) | Não | Sequência |
| MatCon | String(005) | Não | Matrícula da Instituição Consignatária |
| NroCon | String(040) | Não | Número do Contrato de Empréstimo Consignado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042REC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

