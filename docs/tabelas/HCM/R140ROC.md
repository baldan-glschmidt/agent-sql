# R140ROC

## Descrição

Recursos Instrucionais - Ocupação Extraordinária

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRei | Number(004,0) | Não | Código do Recurso Instrucional |
| DatOcu | Date | Não | Data Ocupação da Sala |
| HorIni | Number(005,0) | Não | Hora Início da Ocupação |
| HorTer | Number(005,0) | Sim | Hora Término da Ocupação |
| QtdRei | Number(004,0) | Sim | Quantidade de Recursos Instrucionais |
| ComOcu | String(100) | Sim | Comentário da Ocupação Extraordinária |
| DesPro | String(500) | Sim | Providências |

---

## Chave Primária

- CodRei
- DatOcu
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R140ROC_000

**Tabela:** R140REI

| Origem | Destino |
|--------|---------|
| CodRei | CodRei |

