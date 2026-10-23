# R051DEP

## Descrição

Rendimentos Informe/DIRF - Pensão Judicial

---

## Resumo

- Campos: 13
- Chave Primária: 11 campo(s)
- Índices: 0
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
| CmpRen | Date | Não | Competência dos Rendimentos |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CodDep | Number(002,0) | Não | Código do Dependente |
| TipPen | Number(001,0) | Não | Tipo da Pensão |
| ValPen | Number(011,2) | Sim | Valor da Pensão |
| OriRen | String(001) | Sim | Origem dos Rendimentos |

---

## Chave Primária

- NumEmp
- CodFil
- CodRet
- TipIrf
- CpfCgc
- OriAnu
- CmpRen
- TipCol
- NumCad
- CodDep
- TipPen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R051DEP_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R051DEP_009

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

