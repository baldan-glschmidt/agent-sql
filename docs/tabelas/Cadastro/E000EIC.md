# E000EIC

## Descrição

Tabelas - Integrações - Exceções de Integração de Cupom Fiscal

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInt | Number(002,0) | Não | Código da Integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SeqEis | Number(009,0) | Não | Sequencia da exceção de integração |
| DatEmi | Date | Não | Data de emissão do cupom fiscal |
| CodEqu | Number(003,0) | Sim | Código do equipamento fiscal da redução Z |
| CroEcf | Number(006,0) | Sim | Cont. de Reinício de Operação do ECF |
| NumCfi | Number(009,0) | Não | Número do cupom fiscal de referência da redução Z |

---

## Chave Primária

- CodInt
- CodEmp
- CodFil
- SeqEis

---

## Índices

### E000EICIndice1

**Tipo:** Unico

Campos:
- CodInt
- CodEmp
- CodFil
- CodEqu
- CroEcf
- NumCfi

### E000EICIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

### IR_E000EIC_000

**Tabela:** E000SIS

| Origem | Destino |
|--------|---------|
| CodInt | CodInt |

### IR_E000EIC_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E000EIC_002

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

