# R051EVE

## Descrição

Rendimentos Informe/DIRF - Eventos

---

## Resumo

- Campos: 12
- Chave Primária: 10 campo(s)
- Índices: 1
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
| RenEve | String(001) | Não | Tipo de Rendimento do Evento |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |
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
- RenEve
- TabEve
- CodEve

---

## Índices

### R051EVEIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CpfCgc
- CmpRen
- OriAnu
- OriRen

---

## Relacionamentos

### IR_R051EVE_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R051EVE_009

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

