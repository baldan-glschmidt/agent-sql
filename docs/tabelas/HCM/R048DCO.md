# R048DCO

## Descrição

CLC's Por Outra Empresa

---

## Resumo

- Campos: 18
- Chave Primária: 13 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodOem | Number(008,0) | Não | Código Outra Empresa |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| DatLct | Date | Não | Data do Lançamento |
| TipCtb | String(001) | Não | Origem Contabilização |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código Lançamento Contábil |
| CodFil | Number(006,0) | Sim | Código da Filial |
| FilCtb | Number(006,0) | Sim | Filial Contábil |
| CodRat | Number(009,0) | Não | Código do Rateio |
| ConFin | Number(007,0) | Não | Conta Financeira |
| RatPad | Number(009,0) | Sim | Código do Rateio |
| CodCcu | String(018) | Não | Centro de Custo |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| HisPad | Number(004,0) | Sim | Código Histórico Padrão |
| DebCre | String(001) | Não | Tipo Lançamento |
| ValClc | Number(011,2) | Sim | Valor do CLC |

---

## Chave Primária

- NumEmp
- CodOem
- CodCal
- DatLct
- TipCtb
- TabEve
- CodClc
- CodCcu
- TabOrg
- NumLoc
- DebCre
- CodRat
- ConFin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R048DCO_002

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

### IR_R048DCO_006

**Tabela:** R048CLC

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodClc | CodClc |

