# R116ITR

## Descrição

Itens de Avaliação - Respostas

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodIta | Number(006,0) | Não | Código do Item de Avaliação |
| CodRsp | Number(003,0) | Não | Código da Resposta |
| DesRsp | String(100) | Sim | Descrição Resposta |
| ComRsp | String(255) | Sim | Descrição Completa da Resposta |

---

## Chave Primária

- CodIta
- CodRsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R116ITR_000

**Tabela:** R116ITA

| Origem | Destino |
|--------|---------|
| CodIta | CodIta |

