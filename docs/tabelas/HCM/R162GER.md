# R162GER

## Descrição

BS- Vales Diários Gerados

---

## Resumo

- Campos: 10
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
| DatVal | Date | Não | Data do Vale |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodVal | Number(004,0) | Não | Código do Vale |
| QtdVal | Number(006,2) | Sim | Quantidade de Vales de 1 dia |
| VlrVal | Number(011,2) | Sim | Valor de cada vale |
| StaVal | String(001) | Sim | Status do Vale |
| OriVal | String(001) | Sim | Origem do Vale |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TabEve
- CodVal
- DatVal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R162GER_004

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

