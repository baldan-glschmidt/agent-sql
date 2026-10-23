# R030GRC

## Descrição

Filiais da Empresa - Convênios Grps

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| TipGrp | Number(001,0) | Não | Tipo Grps |
| DatGrp | Date | Não | Data Grps |
| TerFpa | Number(004,0) | Não | Código do Terceiro do Convênio da GRPS |
| PerDco | Number(007,4) | Sim | % Devolução Convênio |
| PerRem | Number(007,4) | Sim | % Retido pela  Empresa |
| TemLim | String(001) | Sim | Liminar |
| CodPro | Number(009,0) | Sim | Número do processo judicial |
| CodSus | Number(014,0) | Sim | Código de Suspensão |

---

## Chave Primária

- NumEmp
- CodFil
- TipGrp
- DatGrp
- TerFpa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030GRC_003

**Tabela:** R030GRP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| TipGrp | TipGrp |
| DatGrp | DatGrp |

