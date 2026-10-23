# R058LFC

## Descrição

Local Físico por Central de Gerenciamento

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCen | Number(002,0) | Não | Central de Gerenciamento do Acesso |
| CodPlt | Number(005,0) | Não | Código do Site |
| NumAmb | Number(009,0) | Não | Ambiente da Planta |

---

## Chave Primária

- CodCen
- CodPlt
- NumAmb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058LFC_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

