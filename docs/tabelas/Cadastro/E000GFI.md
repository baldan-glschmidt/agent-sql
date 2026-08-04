# E000GFI

## Descrição

Tabelas - Integrações - Pendências de Grupos Fiscais

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| IdeNgf | Number(009,0) | Não | Identificador do grupo fiscal |

---

## Chave Primária

- SeqInt

---

## Índices

### E000GFIIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- IdeNgf

### E000GFIIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

Nenhum relacionamento cadastrado.
