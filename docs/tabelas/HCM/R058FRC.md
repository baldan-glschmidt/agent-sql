# R058FRC

## Descrição

Funções Restritas do Cargo

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| CodFra | Number(002,0) | Não | Código da Função Restrita do Acesso |

---

## Chave Primária

- EstCar
- CodCar
- CodFra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058FRC_000

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R058FRC_002

**Tabela:** R058FRA

| Origem | Destino |
|--------|---------|
| CodFra | CodFra |

