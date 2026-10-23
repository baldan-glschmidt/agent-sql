# R101CLA

## Descrição

Ciclos - Classificação de Objetivos

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| TipAva | Number(002,0) | Não | Sequência do tipo da avaliação |
| CodCla | Number(004,0) | Não | Código da classe de objetivos |
| DesCla | String(040) | Sim | Descrição da classe de objetivos |
| QtdMin | Number(003,0) | Sim | Define a quantidade mínima de classes |
| QtdMax | Number(003,0) | Sim | Define a quantidade máxima de classes |
| LimPes | Number(003,0) | Sim | Define um limite de peso para a classe |
| CorCla | String(010) | Sim | Define a cor da classe de objetivos |

---

## Chave Primária

- CodCic
- TipAva
- CodCla

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R101CLA_001

**Tabela:** R101CTA

| Origem | Destino |
|--------|---------|
| CodCic | CodCic |
| TipAva | TipAva |

