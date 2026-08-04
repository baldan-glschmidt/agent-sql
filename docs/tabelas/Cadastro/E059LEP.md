# E059LEP

## Descrição

Tabelas - Tipos de Embalagens - Ligação Embalagens como Produto

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmb | Number(004,0) | Não | Código da embalagem |
| CodEmp | Number(004,0) | Não | Código da empresa do produto |
| CodPro | String(014) | Não | Código do produto como embalagem para movimentação dos estoques |
| CodDer | String(007) | Não | Código da derivação do produto como embalagem |

---

## Chave Primária

- CodEmb
- CodEmp
- CodPro
- CodDer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E059LEP_000

**Tabela:** E059EMB

| Origem | Destino |
|--------|---------|
| CodEmb | CodEmb |

