# E906OPE

## Descrição

Produção - Operadores

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| NumCad | Number(009,0) | Não | Código do operador |
| NomOpe | String(080) | Não | Nome do operador |
| CodGrp | String(005) | Sim | Código do grupo a que o operador pertence |
| TurTrb | Number(001,0) | Sim | Turno de trabalho do operador |
| SupIme | Number(009,0) | Sim | Código do superior imediato |
| CodCel | String(004) | Sim | Célula de produção onde o operador está alocado |
| PrdOpd | String(001) | Não | Indica se o operador está trabalhando em alguma O.P./O.S. |
| OpdOrp | String(001) | Não | Permite movimentação de várias O.Ps./O.Ss. ao mesmo tempo |
| CodCcu | String(009) | Sim | Código do Centro de Custo do operador |
| SitOpe | String(001) | Não | Situação do operador |
| CodLot | String(050) | Sim | Lote do componente base sendo utilizado atualmente pelo operador |

---

## Chave Primária

- CodEmp
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
