# R140SLR

## Descrição

Salas de Treinamento - Recursos Instrucionais

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
| CodRei | Number(004,0) | Não | Código do Recurso Instrucional |
| QtdRei | Number(004,0) | Sim | Quantidade de Recursos Utilizados |

---

## Chave Primária

- CodSla
- CodRei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R140SLR_000

**Tabela:** R140SLA

| Origem | Destino |
|--------|---------|
| CodSla | CodSla |

### IR_R140SLR_001

**Tabela:** R140REI

| Origem | Destino |
|--------|---------|
| CodRei | CodRei |

