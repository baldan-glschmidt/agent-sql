# R036EDU

## Descrição

Controle de Frequência Escolar

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodDep | Number(002,0) | Não | Código do dependente |
| AnoEsc | Number(004,0) | Não | Ano Escolar |
| DepBol | String(001) | Sim | Dependente Bolsista (S,N) |
| CodOem | Number(008,0) | Sim | Código da Escola |
| SerIns | Number(002,0) | Sim | Código da Série |
| EntMai | Date | Sim | Data Entrega da Freq. Maio |
| EntNov | Date | Sim | Data Entrega da Freq. Novembro |
| PerMai | Number(005,2) | Sim | Percentual de Frequencia em Maio |
| PerNov | Number(005,2) | Sim | Percentual de Frequencia em Novembro |
| DatVac | Date | Sim | Data Comprovante Vacinação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep
- AnoEsc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R036EDU_003

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

