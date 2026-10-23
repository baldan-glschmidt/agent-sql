# R017IDP

## Descrição

Estrutura de Postos de Trabalho - Itens de descrição do Posto

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
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| SeqIdp | Number(005,0) | Não | Sequência do item de descrição do posto |
| DesIdp | String(050) | Sim | Descrição do item |
| AtiRis | String(001) | Sim | Indica se o item de descrição será utilizado para informar as atividades de risco |

---

## Chave Primária

- EstPos
- SeqIdp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017IDP_000

**Tabela:** R017EST

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |

