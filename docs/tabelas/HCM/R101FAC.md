# R101FAC

## Descrição

Ciclos - Focos da Avaliação

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
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| FocAva | Number(001,0) | Não | Foco da Avaliação |
| InfAva | String(001) | Sim | Permite informar avaliador individual para este tipo de avaliação |
| PesFoc | Number(007,4) | Sim | Peso do foco de avaliação em relação aos demais do ciclo |

---

## Chave Primária

- CodCic
- FocAva

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R101FAC_000

**Tabela:** R101CIC

| Origem | Destino |
|--------|---------|
| CodCic | CodCic |

