# R162SOC

## Descrição

BS - Solicitação Avulsa de Vales

---

## Resumo

- Campos: 16
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Número do Colaborador |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodVal | Number(004,0) | Não | Código do Tipo do Vale |
| DatSoc | Date | Não | Data Solicitação do Vale |
| DatVal | Date | Sim | Data Validade da Solicitação |
| PerVal | Number(005,2) | Sim | Percentual Sobre Salário |
| VlrVal | Number(011,2) | Sim | Valor do Vale |
| PerSub | Number(007,4) | Sim | Percentual de Subsídio do Vale |
| QtdVal | Number(006,2) | Sim | Quantidade de Vales |
| QtdUti | Number(005,2) | Sim | Quantidade de Vales Dia Util |
| QtdSab | Number(005,2) | Sim | Quantidade de Vales Sábado |
| QtdDom | Number(005,2) | Sim | Quantidade de Vales Domingo |
| QtdFer | Number(005,2) | Sim | Quantidade de Vales Feriado |
| TipInc | String(001) | Sim | Tipo Inclusão |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TabEve
- CodVal
- DatSoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R162SOC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R162SOC_004

**Tabela:** R044TVL

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodVal | CodVal |

