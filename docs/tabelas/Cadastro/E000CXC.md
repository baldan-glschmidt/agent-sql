# E000CXC

## Descrição

Tabelas - Integrações - Controle de Cupons X Convênios

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodEqu | Number(003,0) | Não | Código do equipamento fiscal |
| CroEcf | Number(006,0) | Não | Cont. de Reinício de Operação do ECF |
| NumCfi | Number(009,0) | Não | Número do cupom fiscal de referência da redução Z |
| CodCnv | Number(004,0) | Não | Código do convênio |
| CodCli | Number(009,0) | Não | Código do cliente |
| VlrCnv | Number(011,2) | Sim | Valor utilizado do convênio |
| DatEmi | Date | Sim | Data de Emissão do Cupom Fiscal |

---

## Chave Primária

- CodEmp
- CodFil
- CodEqu
- CroEcf
- NumCfi
- CodCnv

---

## Índices

### E000CXCIndice1

**Tipo:** Não unico

Campos:
- CodCnv

---

## Relacionamentos

### IR_E000CXC_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E000CXC_005

**Tabela:** E069CNV

| Origem | Destino |
|--------|---------|
| CodCnv | CodCnv |

