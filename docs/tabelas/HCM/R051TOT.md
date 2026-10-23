# R051TOT

## Descrição

Rendimentos Informe/DIRF - Totalizadores

---

## Resumo

- Campos: 15
- Chave Primária: 10 campo(s)
- Índices: 1
- Relacionamentos: 1

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
| RenTot | String(001) | Não | Tipo de Rendimento do Totalizador |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodTot | Number(004,0) | Não | Código do Totalizador |
| ValTot | Number(011,2) | Sim | Valor do Totalizador |
| OriRen | String(001) | Sim | Origem dos Rendimentos |
| FilCmp | Number(006,0) | Sim | Filial na Competência |
| CodOem | Number(008,0) | Não | Entidade |
| TipPag | Number(001,0) | Sim | Pagamento |

---

## Chave Primária

- NumEmp
- CodFil
- CodRet
- TipIrf
- CpfCgc
- OriAnu
- CmpRen
- RenTot
- TabEve
- CodTot

---

## Índices

### R051TOTIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CpfCgc
- CmpRen
- OriAnu
- OriRen

---

## Relacionamentos

### IR_R051TOT_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

