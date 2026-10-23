# R184PCO

## Descrição

PLR - Pontuação do Colaborador

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Número do Colaborador |
| CodObj | Number(004,0) | Não | Código do Objetivo |
| DatPon | Date | Não | Data Pontuação |
| DatIni | Date | Sim | Data Início |
| DatFim | Date | Sim | Data Fim |
| ResObj | Number(011,2) | Sim | Resultado do Objetivo |
| PonObj | Number(011,2) | Sim | Pontos do Objetivo |
| TotObj | Number(011,2) | Sim | Total do Objetivo (Pontos * Peso) |
| ExpCal | String(030) | Sim | Expressão Utilizada no Cálculo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodObj
- DatPon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R184PCO_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R184PCO_003

**Tabela:** R182OBJ

| Origem | Destino |
|--------|---------|
| CodObj | CodObj |

