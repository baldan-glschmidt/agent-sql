# E000EIZ

## Descrição

Tabelas - Integrações - Exceções de Integração de Redução Z

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInt | Number(002,0) | Não | Código da Integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SeqEis | Number(009,0) | Não | Sequencia da exceção de integração |
| CroEcf | Number(006,0) | Não | Cont. de Reinício de Operação do ECF |
| CodEqu | Number(003,0) | Não | Código do equipamento fiscal da redução Z |
| DatRef | Date | Não | Data de referência da redução Z |

---

## Chave Primária

- CodInt
- CodEmp
- CodFil
- SeqEis

---

## Índices

### E000EIZIndice1

**Tipo:** Unico

Campos:
- CodInt
- CodEmp
- CodFil
- CroEcf
- CodEqu
- DatRef

### E000EIZIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodEqu

---

## Relacionamentos

### IR_E000EIZ_000

**Tabela:** E000SIS

| Origem | Destino |
|--------|---------|
| CodInt | CodInt |

### IR_E000EIZ_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E000EIZ_002

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E000EIZ_005

**Tabela:** E050EQF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodEqu | CodEqu |

