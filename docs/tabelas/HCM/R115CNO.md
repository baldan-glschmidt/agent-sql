# R115CNO

## Descrição

Campos de Pendência de Notificação

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
| CodNot | Number(009,0) | Não | Código da pendência de notificação |
| CodSeq | Number(009,0) | Não | Código da sequência do item de notificação |
| NomCam | String(030) | Sim | Nome do campo presente no template da notificação |
| ValStr | String(199) | Sim | Valor do campo presente no template da notificação |

---

## Chave Primária

- CodNot
- CodSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R115CNO_000

**Tabela:** R115NOT

| Origem | Destino |
|--------|---------|
| CodNot | CodNot |

