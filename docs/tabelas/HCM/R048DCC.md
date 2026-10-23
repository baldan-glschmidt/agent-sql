# R048DCC

## Descrição

CLC's Por Colaborador

---

## Resumo

- Campos: 20
- Chave Primária: 14 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
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
| ValClc | Number(014,2) | Sim | Valor do CLC |
| CodFor | Number(009,0) | Sim | Código Fornecedor |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
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

### R048DCCIndice2

**Tipo:** Não unico

Campos:
- TabEve
- CodClc

---

## Relacionamentos

### IR_R048DCC_003

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

### IR_R048DCC_007

**Tabela:** R048CLC

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodClc | CodClc |

