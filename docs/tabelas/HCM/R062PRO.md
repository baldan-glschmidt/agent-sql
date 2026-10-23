# R062PRO

## Descrição

Procedimentos para Tratamento do Sinal de Alarme

---

## Resumo

- Campos: 2
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(003,0) | Não | Código do Sinal de Alarme |
| ProSin | String(500) | Sim | Descrição do Procedimento para Tratamento do Sinal de Alarme |

---

## Chave Primária

- CodSin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R062PRO_000

**Tabela:** R062SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

