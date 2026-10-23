# R118ITR

## Descrição

Itens de Questionário - Respostas

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
| CodItq | Number(003,0) | Não | Código do Item do Questionário |
| CodRsp | Number(003,0) | Não | Código da Resposta |
| DesRsp | String(100) | Sim | Descrição Resposta |
| ComRsp | String(255) | Sim | Descrição Completa da Resposta |

---

## Chave Primária

- CodItq
- CodRsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R118ITR_000

**Tabela:** R118ITQ

| Origem | Destino |
|--------|---------|
| CodItq | CodItq |

