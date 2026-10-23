# R711FOR

## Descrição

Permissões de Formulários Específicos - Itens (Para Consultas)

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
| CodPer | Number(002,0) | Não | Código da Permissões para o Formulário |
| ValPer | String(1000) | Sim | Valor da Permissão para o Formulário |

---

## Chave Primária

- CodSeq
- CodPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R711FOR_000

**Tabela:** R710FOR

| Origem | Destino |
|--------|---------|
| CodSeq | CodSeq |

