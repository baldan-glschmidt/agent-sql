# R024NIV

## Descrição

Estrutura do Cargo - Níveis

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
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| NivCar | Number(002,0) | Não | Nível do Cargo |
| DesNiv | String(010) | Sim | Descrição do Nível do Cargo |
| NumPos | Number(002,0) | Sim | Qtde de Posições do Nível na Máscara |

---

## Chave Primária

- EstCar
- NivCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024NIV_000

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

