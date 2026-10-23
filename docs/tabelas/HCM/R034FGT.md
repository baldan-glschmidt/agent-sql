# R034FGT

## Descrição

Alteração de Dados do Fgts

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CmpFgt | Date | Não | Competência |
| NomFun | String(040) | Sim | Nome Anterior do Colaborador |
| NumCtp | Number(009,0) | Sim | Número da Carteira de Trabalho e Previdênica Social |
| SerCtp | String(005) | Sim | Série da Carteira de Trabalho |
| EstCtp | String(002) | Sim | Estado da Carteira de Trabalho |
| NumPis | Number(011,0) | Sim | Número do PIS/PASEP |
| DatAdm | Date | Sim | Data de Admissão |
| DatOpc | Date | Sim | Data de Opção do FGTS |
| DatNas | Date | Sim | Data de Nascimento |
| AltEnd | String(001) | Sim | Alterou Endereço (S/N) |
| NumCpf | Number(011,0) | Sim | Número do CPF |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpFgt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034FGT_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

