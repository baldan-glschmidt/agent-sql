# R051COL

## Descrição

Rendimentos Informe/DIRF - Cadastros

---

## Resumo

- Campos: 13
- Chave Primária: 8 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRet | Number(004,0) | Não | Código de Retenção do IR |
| TipIrf | String(001) | Não | IR Normal ou Estrangeiro |
| CpfCgc | Number(015,0) | Não | Número do CPF/CNPJ |
| OriAnu | Number(001,0) | Não | Origem |
| AnoRen | Date | Não | Ano Rendimentos |
| SeqCol | Number(002,0) | Não | Sequência |
| TipCol | Number(001,0) | Sim | Tipo do Colabolador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa |
| CodDep | Number(002,0) | Sim | Código do Dependente |
| TipBen | String(001) | Sim | Tipo do Beneficiário |

---

## Chave Primária

- NumEmp
- CodFil
- CodRet
- TipIrf
- CpfCgc
- OriAnu
- AnoRen
- SeqCol

---

## Índices

### R051COLIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CpfCgc
- AnoRen
- OriAnu

### R051COLIndice3

**Tipo:** Não unico

Campos:
- OriAnu
- CpfCgc

---

## Relacionamentos

### IR_R051COL_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R051COL_005

**Tabela:** R051BEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodRet | CodRet |
| TipIrf | TipIrf |
| CpfCgc | CpfCgc |
| OriAnu | OriAnu |

