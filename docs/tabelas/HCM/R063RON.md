# R063RON

## Descrição

Ronda de Vigilantes

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRon | Number(003,0) | Não | Código da Ronda |
| DesRon | String(050) | Sim | Descrição da Ronda |
| CodSin | Number(003,0) | Sim | Código do Sinal de Alarme |
| FncRon | Number(002,0) | Sim | Função da Ronda |
| FncCoa | Number(002,0) | Sim | Função de Coação |
| TolRon | Number(003,0) | Sim | Tolerância entre as etapas da ronda. |

---

## Chave Primária

- CodRon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R063RON_002

**Tabela:** R062SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

