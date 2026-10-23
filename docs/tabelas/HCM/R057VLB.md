# R057VLB

## Descrição

Valores Benefício

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBnf | Number(002,0) | Não | Código do Benefício |
| DatAlt | Date | Não | Data de Alteração do Valor do Benefício |
| CodVin | Number(002,0) | Não | Código do Vínculo |
| VlrBnf | Number(008,2) | Sim | Valor do Benefício |

---

## Chave Primária

- CodBnf
- CodVin
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R057VLB_000

**Tabela:** R057BNF

| Origem | Destino |
|--------|---------|
| CodBnf | CodBnf |

