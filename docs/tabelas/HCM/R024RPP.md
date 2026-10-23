# R024RPP

## Descrição

PPP - Requisito de  Cargo - por Cargo e Cargo/Local

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| DatRqu | Date | Não | Data do Requisito do Cargo |
| DesReq | String(300) | Sim | Descrição do requisito |

---

## Chave Primária

- EstCar
- CodCar
- DatRqu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024RPP_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

