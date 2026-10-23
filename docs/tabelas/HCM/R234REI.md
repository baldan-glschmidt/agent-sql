# R234REI

## Descrição

Evento - Recursos Instrucionais

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| DatIni | Date | Não | Data Inicial do Horário |
| HorIni | Number(005,0) | Não | Hora Inicial do horário |
| CodRei | Number(004,0) | Não | Código do Recurso Instrucional |
| QtdRei | Number(004,0) | Sim | Quantidade de Recursos Instrucionais |

---

## Chave Primária

- CodEvn
- DatIni
- HorIni
- CodRei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234REI_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234REI_003

**Tabela:** R140REI

| Origem | Destino |
|--------|---------|
| CodRei | CodRei |

