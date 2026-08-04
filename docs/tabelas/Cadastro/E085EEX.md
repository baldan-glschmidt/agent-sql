# E085EEX

## Descrição

Cadastros - Integrações - Exceção de Exportação

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInt | Number(002,0) | Não | Código do sistema integrado |
| CodCli | Number(009,0) | Não | Código do Cliente |

---

## Chave Primária

- CodInt
- CodCli

---

## Índices

### E085EEXIndice1

**Tipo:** Não unico

Campos:
- CodCli

---

## Relacionamentos

### IR_E085EEX_000

**Tabela:** E000SIS

| Origem | Destino |
|--------|---------|
| CodInt | CodInt |

### IR_E085EEX_001

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

