# R711CAL

## Descrição

Permissões de Cálculos - Items (Para Consultas)

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
| CodSeq | Number(005,0) | Não | Código da Sequência das Permissões |
| CodPer | Number(002,0) | Não | Código da Permissões para o Cálculo |
| ValPer | String(001) | Sim | Valor da Permissão para o Cálculo |

---

## Chave Primária

- CodSeq
- CodPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R711CAL_000

**Tabela:** R710CAL

| Origem | Destino |
|--------|---------|
| CodSeq | CodSeq |

