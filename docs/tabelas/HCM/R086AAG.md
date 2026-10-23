# R086AAG

## Descrição

Acidentes de Trabalho - Agentes de Lesão

---

## Resumo

- Campos: 6
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAct | Date | Não | Data Acidente de Trabalho |
| HorAct | Number(005,0) | Não | Hora Acidente de Trabalho |
| AgeLes | Number(003,0) | Não | Código do Agente Causador |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAct
- HorAct
- AgeLes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086AAG_005

**Tabela:** R086AGT

| Origem | Destino |
|--------|---------|
| AgeLes | CodAgt |

