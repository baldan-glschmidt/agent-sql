# R022PRF

## Descrição

Conselhos Profissionais

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPrf | Number(004,0) | Não | Código Conselho Profissional |
| DesPrf | String(050) | Sim | Descrição Cons.Profissional |
| SigPrf | String(007) | Sim | Sigla Conselho Profissional |
| CodCid | Number(007,0) | Sim | Sede Conselho Profissional |
| RegPrf | String(006) | Sim | Região Conselho Profissional |

---

## Chave Primária

- CodPrf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R022PRF_003

**Tabela:** R074CID

| Origem | Destino |
|--------|---------|
| CodCid | CodCid |

