# R051EXT

## Descrição

Rendimentos Informe/DIRF - Exterior

---

## Resumo

- Campos: 21
- Chave Primária: 7 campo(s)
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
| DatPag | Date | Não | Data de Pagamento |
| TipRen | Number(003,0) | Sim | Tipo de Rendimento |
| ForTri | Number(002,0) | Sim | Forma de Tributação |
| BasIrf | Number(011,2) | Sim | Valor Base do IR |
| ValIrf | Number(011,2) | Sim | Valor do IR |
| BasFer | Number(011,2) | Sim | Base IR de Férias |
| IrfFer | Number(011,2) | Sim | Valor IR de Férias |
| Bas13s | Number(011,2) | Sim | Base IR de 13° Salário |
| Irf13s | Number(011,2) | Sim | Valor do IR 13° Salário |
| BasPlr | Number(011,2) | Sim | Base IR de Participação nos Lucros |
| IrfPlr | Number(011,2) | Sim | Valor de IR Sobre Participação nos Lucros |
| OriRen | String(001) | Sim | Origem dos Rendimentos |
| BasAu1 | Number(011,2) | Sim | Uso Exclusivo da Senior |
| ValAu1 | Number(011,2) | Sim | Uso Exclusivo da Senior |
| TipAux | Number(005,0) | Sim | Uso Exclusivo da Senior |

---

## Chave Primária

- NumEmp
- CodFil
- CodRet
- TipIrf
- CpfCgc
- OriAnu
- DatPag

---

## Índices

### R051EXTIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CpfCgc
- DatPag
- OriAnu
- OriRen

### R051EXTIndice3

**Tipo:** Não unico

Campos:
- OriAnu
- CpfCgc

---

## Relacionamentos

### IR_R051EXT_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R051EXT_005

**Tabela:** R051BEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodRet | CodRet |
| TipIrf | TipIrf |
| CpfCgc | CpfCgc |
| OriAnu | OriAnu |

