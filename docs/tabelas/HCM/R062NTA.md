# R062NTA

## Descrição

Notificação do Alarme

---

## Resumo

- Campos: 4
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| CodSin | Number(003,0) | Sim | Código do Sinal de Alarme |
| DatUlt | Date | Sim | Data do último alarme notificado |
| HorUlt | Number(005,0) | Sim | Hora do último alarme notificado |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R062NTA_001

**Tabela:** R062SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

