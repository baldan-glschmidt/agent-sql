# R086ACA

## Descrição

Acidentes de Trabalho - Causas de Acidente

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
| CauAct | Number(003,0) | Não | Causa Acidente |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAct
- HorAct
- CauAct

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086ACA_005

**Tabela:** R086CAC

| Origem | Destino |
|--------|---------|
| CauAct | CodCau |

