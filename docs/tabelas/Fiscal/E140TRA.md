# E140TRA

## Descrição

Tabelas - Notas Fiscais de Saída - Transmitentes

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqTra | Number(003,0) | Não | Sequência do Transmitente |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| IndDec | String(001) | Não | Indicador de declarante |
| PerTra | Number(007,4) | Sim | Proporção transmitida individual |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqTra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140TRA_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140TRA_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

### IR_E140TRA_005

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

