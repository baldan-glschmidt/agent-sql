# R105PGU

## Descrição

Cadastro de Avaliadores - Período Grupo Cargos Pares

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
| GruCar | Number(004,0) | Não | Código do Grupo de Cargos Pares |
| DatIni | Date | Não | Data de início do período do grupo de cargos pares |
| DatFim | Date | Sim | Data de término do período do grupo de cargos pares |
| CodCic | Number(003,0) | Sim | Código do ciclo de avaliação |

---

## Chave Primária

- GruCar
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R105PGU_000

**Tabela:** R105GCP

| Origem | Destino |
|--------|---------|
| GruCar | GruCar |

