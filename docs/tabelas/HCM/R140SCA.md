# R140SCA

## Descrição

Capacidade da Sala - Disposição de Lugares

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSla | Number(004,0) | Não | Código da Sala de Treinamento |
| CodDis | Number(003,0) | Não | Código Disposição |
| QtdVga | Number(006,0) | Sim | Capacidade Máxima de Vagas |

---

## Chave Primária

- CodSla
- CodDis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R140SCA_000

**Tabela:** R140SLA

| Origem | Destino |
|--------|---------|
| CodSla | CodSla |

### IR_R140SCA_001

**Tabela:** R140DIS

| Origem | Destino |
|--------|---------|
| CodDis | CodDis |

