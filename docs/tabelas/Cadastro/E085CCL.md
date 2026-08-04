# E085CCL

## Descrição

Cadastros - Clientes - Características

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodCcl | String(003) | Não | Código da característica de cliente |
| SeqOrd | Number(002,0) | Não | Ordem preferencial da característica |
| CodCcc | Number(003,0) | Não | Código do componente da característica de cliente |
| UsuCad | Number(010,0) | Sim | Usuário responsável pelo cadastramento |
| DatCad | Date | Sim | Data do cadastramento do fornecedor |
| HorCad | Number(005,0) | Sim | Hora/minuto do cadastramento do fornecedor |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela alteração do registro |
| DatAlt | Date | Sim | Data da alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do registro |

---

## Chave Primária

- CodCli
- CodCcl
- SeqOrd

---

## Índices

### E085CCLIndice1

**Tipo:** Não unico

Campos:
- CodCcl
- CodCcc

---

## Relacionamentos

### IR_E085CCL_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E085CCL_003

**Tabela:** E014CCC

| Origem | Destino |
|--------|---------|
| CodCcl | CodCcl |
| CodCcc | CodCcc |

