# R016TOT

## Descrição

Histórico Totalizadores por Local

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpTot | Date | Não | Competência do histórico de totalização |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodTot | Number(004,0) | Não | Código do Totalizador |
| QtdTot | Number(011,2) | Sim | Quantidade acumulada |
| OriInf | String(001) | Sim | Origem da informação(D-Digitado, G-Gerado) |

---

## Chave Primária

- NumEmp
- CmpTot
- TabOrg
- NumLoc
- TabEve
- CodTot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016TOT_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R016TOT_005

**Tabela:** R008TOT

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodTot | CodTot |

