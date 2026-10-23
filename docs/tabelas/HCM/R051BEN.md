# R051BEN

## Descrição

Rendimentos Informe/DIRF - Beneficiários

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 2
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
| OriRen | String(001) | Sim | Origem dos Rendimentos |

---

## Chave Primária

- NumEmp
- CodFil
- CodRet
- TipIrf
- CpfCgc
- OriAnu

---

## Índices

### R051BENIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CpfCgc
- OriAnu
- OriRen

### R051BENIndice3

**Tipo:** Não unico

Campos:
- OriAnu
- CpfCgc

---

## Relacionamentos

### IR_R051BEN_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

