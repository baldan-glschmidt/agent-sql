# R063RRV

## Descrição

Rota da Ronda de Vigilantes

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRon | Number(003,0) | Não | Código da Ronda |
| SeqRon | Number(002,0) | Não | Sequência da ronda |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| TemRon | Number(003,0) | Sim | Tempo entre as etapas de cada ronda |

---

## Chave Primária

- CodRon
- SeqRon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R063RRV_000

**Tabela:** R063RON

| Origem | Destino |
|--------|---------|
| CodRon | CodRon |

### IR_R063RRV_002

**Tabela:** R058DSP

| Origem | Destino |
|--------|---------|
| CodDsp | CodDsp |

