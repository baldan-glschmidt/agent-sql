# E085RXC

## Descrição

Cadastros - Clientes - Relação Cliente X Cliente

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| CliRel | Number(009,0) | Não | Cliente Relacionado |
| PerFat | Number(005,2) | Sim | Percentual do pedido que deve ser faturado para o cliente principal |

---

## Chave Primária

- CodCli
- CliRel

---

## Índices

### E085RXCIndice1

**Tipo:** Não unico

Campos:
- CliRel

---

## Relacionamentos

### IR_E085RXC_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E085RXC_001

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CliRel | CodCli |

