# R064CNV

## Descrição

Convocações

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatCnv | Date | Não | Data da Convocação do Colaborador |
| TipCnv | Number(001,0) | Sim | Tipo da Convocação |
| HorCnv | Number(004,0) | Sim | Código do Horário da Convocação |
| IniFai | Number(005,0) | Sim | Início Faixa de Trabalho |
| FimFai | Number(005,0) | Sim | Fim Faixa de Trabalho |
| QtdHor | Number(005,0) | Sim | Qtde de Horas da Convocação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatCnv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R064CNV_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

