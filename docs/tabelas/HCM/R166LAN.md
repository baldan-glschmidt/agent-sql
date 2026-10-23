# R166LAN

## Descrição

Auxílio Educação - Lançamentos Integração Folha

---

## Resumo

- Campos: 17
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Sim | Número da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| CmpAux | Date | Sim | Competência do Auxílio |
| CmpRee | Date | Sim | Competência do Reembolso |
| CodCua | Number(009,0) | Sim | Código do Curso de Aperfeiçoamento |
| CodCuf | Number(004,0) | Sim | Código do Curso de Formação |
| CodTcu | Number(004,0) | Sim | Código do Item de Custo |
| VlrLan | Number(011,2) | Sim | Valor Lançado |
| VlrRee | Number(011,2) | Sim | Valor Calculado do Reembolso |
| TabEve | Number(003,0) | Sim | lookup para tabela de eventos |
| CodEve | Number(004,0) | Sim | Código do Evento |
| OriReg | String(001) | Sim | Origem Registro: (D)igitado ou (G)erado |
| ObsLan | String(100) | Sim | Observação do Lançamento |
| CodCal | Number(005,0) | Sim | Código do Cálculo em que foi Efetuado a Integração |
| DatECo | Date | Sim | Data de Entrega do Comprovante |
| IntAut | String(001) | Sim | Integração Autorizada |

---

## Chave Primária

Não possui.

---

## Índices

### R166LANindice1

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CmpAux

---

## Relacionamentos

### IR_R166LAN_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R166LAN_007

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

### IR_R166LAN_011

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

