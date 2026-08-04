# E085INE

## Descrição

Cadastros - Clientes - Inscrição Estadual

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
| SigUfs | String(002) | Não | Sigla do estado do cliente |
| InsEst | String(025) | Não | Inscrição estadual do cliente |

---

## Chave Primária

- CodCli
- SigUfs

---

## Índices

### E085INEIndice1

**Tipo:** Não unico

Campos:
- SigUfs

---

## Relacionamentos

### IR_E085INE_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E085INE_001

**Tabela:** E007UFS

| Origem | Destino |
|--------|---------|
| SigUfs | SigUfs |

