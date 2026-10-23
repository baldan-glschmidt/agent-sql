# R051ISE

## Descrição

Rendimentos Informe/DIRF - Terceiros Isentos

---

## Resumo

- Campos: 11
- Chave Primária: 8 campo(s)
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
| CodIse | Number(002,0) | Não | Código do Motivo Isento |
| ValIse | Number(011,2) | Sim | Valor Isento |
| ConIns | Number(011,2) | Sim | Contribuição INSS |
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
- CodIse

---

## Índices

### R051ISEIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CpfCgc
- CmpRen
- OriAnu
- OriRen

---

## Relacionamentos

### IR_R051ISE_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R051ISE_007

**Tabela:** R050ISE

| Origem | Destino |
|--------|---------|
| CodIse | CodIse |

