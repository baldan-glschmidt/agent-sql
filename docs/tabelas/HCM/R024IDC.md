# R024IDC

## Descrição

Estrutura do Cargo - Itens de descrição do Cargo

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| SeqIdc | Number(005,0) | Não | Sequência do item de descrição do cargo |
| DesIdc | String(050) | Sim | Descrição do item |
| DesCar | String(001) | Sim | Indica se o item de descrição será considerado na descrição de cargos |
| AtiRis | String(001) | Sim | Indica se o item de descrição será utilizado para informar as atividades de risco |

---

## Chave Primária

- EstCar
- SeqIdc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024IDC_000

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

