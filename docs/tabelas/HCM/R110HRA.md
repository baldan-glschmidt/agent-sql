# R110HRA

## Descrição

Ficha Médica - Remanejamento - Acompanhamento

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodFic | Number(009,0) | Não | Código da Ficha Médica |
| DatIni | Date | Não | Data início do remanejamento |
| DatAco | Date | Não | Data do acompanhamento |
| DatPer | Date | Sim | Data da Perícia Médica |
| CodPar | Number(003,0) | Sim | Código do Parecer |
| ObsAco | String(500) | Sim | Observação sobre o acompanhamento |

---

## Chave Primária

- NumEmp
- CodFic
- DatIni
- DatAco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110HRA_002

**Tabela:** R110HRE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |
| DatIni | DatIni |

