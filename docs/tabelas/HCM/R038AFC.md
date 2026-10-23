# R038AFC

## Descrição

Afastamentos - Cálculo

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatAfa | Date | Não | Data do Afastamento |
| HorAfa | Number(005,0) | Não | Hora do Afastamento |
| CodCal | Number(005,0) | Não | Código do Cálculo |
| DatIni | Date | Sim | Data do Início |
| DatFim | Date | Sim | Data do Término |
| CmpAu1 | Number(009,0) | Sim | Campo Auxiliar 1 |
| CmpAu2 | String(040) | Sim | Campo Auxiliar 2 |
| CmpAu3 | Number(011,2) | Sim | Campo Auxiliar 3 |
| CmpAu4 | Date | Sim | Campo Auxiliar 4 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAfa
- HorAfa
- CodCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038AFC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

