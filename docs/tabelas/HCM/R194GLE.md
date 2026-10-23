# R194GLE

## Descrição

BS - Glebas

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFaz | Number(008,0) | Não | Código da Fazenda |
| CodGle | Number(005,0) | Não | Código da Gleba |
| DesGle | String(030) | Sim | Descrição da Gleba |

---

## Chave Primária

- CodFaz
- CodGle

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R194GLE_000

**Tabela:** R194FAZ

| Origem | Destino |
|--------|---------|
| CodFaz | CodFaz |

