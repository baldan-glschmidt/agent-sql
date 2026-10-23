# R110MRC

## Descrição

Receitas Médicas

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodAte | Number(006,0) | Não | Código do Atendente |
| NumRec | Number(006,0) | Não | Número da Receita |
| CodFic | Number(009,0) | Sim | Código da Ficha Médica |
| DatMrc | Date | Sim | Data Receita |
| DesPre | String(2000) | Sim | Prescrição médica |
| DesMrc | String(2000) | Sim | Observações do médico |
| TipRec | Number(001,0) | Sim | Tipo de receita |
| AutCom | String(001) | Sim | Autorização de compra de medicamentos |

---

## Chave Primária

- NumEmp
- CodAte
- NumRec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110MRC_001

**Tabela:** R108TAT

| Origem | Destino |
|--------|---------|
| CodAte | CodAte |

### IR_R110MRC_003

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

