# R136REC

## Descrição

Testes Turma - Recursos Instrucionais

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
| CodTst | String(005) | Não | Código do Teste |
| CodRei | Number(004,0) | Não | Código do Recurso Instrucional |
| QtdRei | Number(004,0) | Sim | Quantidade de Recursos Utilizados |

---

## Chave Primária

- CodTst
- CodRei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R136REC_000

**Tabela:** R136TES

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |

### IR_R136REC_001

**Tabela:** R140REI

| Origem | Destino |
|--------|---------|
| CodRei | CodRei |

