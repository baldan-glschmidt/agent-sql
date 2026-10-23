# R074MIC

## Descrição

Micro-Regiões

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
| CodReg | Number(003,0) | Não | Código da Região |
| CodMic | Number(003,0) | Não | Código da Micro-Região |
| DesMic | String(020) | Sim | Descrição da Micro-Região |
| EstReg | String(002) | Sim | Estado da Micro-Região |

---

## Chave Primária

- CodReg
- CodMic

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R074MIC_000

**Tabela:** R074REG

| Origem | Destino |
|--------|---------|
| CodReg | CodReg |

