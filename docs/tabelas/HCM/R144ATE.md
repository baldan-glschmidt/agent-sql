# R144ATE

## Descrição

BS - Atendimentos

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| DatSol | Date | Não | Data Solicitação |
| TipSol | Number(003,0) | Não | Tipo da Solicitação |
| DatSoc | Date | Sim | Data da Solução |
| TipSoc | Number(003,0) | Sim | Tipo da Solução |
| HisSol | String(3899) | Sim | Histórico da Solicitação |
| HisSoc | String(1899) | Sim | Histórico da Solução |
| NomArq | String(250) | Sim | Arquivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatSol
- TipSol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R144ATE_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R144ATE_004

**Tabela:** R144SOL

| Origem | Destino |
|--------|---------|
| TipSol | CodSol |

