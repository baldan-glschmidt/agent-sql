# R110TPI

## Descrição

Prioridade Atendimento - Itens

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabPri | Number(003,0) | Não | Tabela de prioridade |
| CodPri | Number(003,0) | Não | Código |
| DesPri | String(050) | Sim | Descrição do item da tabela de prioridade |
| TmpEsp | Number(005,0) | Sim | Tempo espera |
| CorPri | String(010) | Sim | Cor |

---

## Chave Primária

- TabPri
- CodPri

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110TPI_000

**Tabela:** R110TPR

| Origem | Destino |
|--------|---------|
| TabPri | TabPri |

