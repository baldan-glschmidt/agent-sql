# R086ALO

## Descrição

Acidentes de Trabalho - Locais de Lesão

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAct | Date | Não | Data Acidente de Trabalho |
| HorAct | Number(005,0) | Não | Hora Acidente de Trabalho |
| LocLes | Number(003,0) | Não | Código Local das Lesões |
| LatLes | Number(001,0) | Sim | Lateralidade da Lesão |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAct
- HorAct
- LocLes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086ALO_005

**Tabela:** R086LLE

| Origem | Destino |
|--------|---------|
| LocLes | CodLle |

