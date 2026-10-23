# R047SIB

## Descrição

Cadastro de Sindicatos - Composição (Exceções)

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCif | Number(003,0) | Não | Código de Integração Financeira |
| CodSin | Number(004,0) | Não | Código do Sindicato |
| SinCif | String(001) | Sim | Sinal de Soma |
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |

---

## Chave Primária

- CodCif
- CodSin
- CodTab
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R047SIB_000

**Tabela:** R047CIF

| Origem | Destino |
|--------|---------|
| CodCif | CodCif |

### IR_R047SIB_001

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

### IR_R047SIB_003

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |

### IR_R047SIB_004

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

