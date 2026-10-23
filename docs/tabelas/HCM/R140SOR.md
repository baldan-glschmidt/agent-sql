# R140SOR

## Descrição

Salas de Treinamento - Recursos Instrucionais da Ocupação Extraordinária

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
| CodSla | Number(004,0) | Não | Código da Sala de Treinamento |
| DatOcu | Date | Não | Data Ocupação da Sala |
| HorIni | Number(005,0) | Não | Hora Início da Ocupação |
| CodRei | Number(004,0) | Não | Código do Recurso Instrucional |
| QtdRei | Number(004,0) | Sim | Quantidade de Recursos Utilizados |

---

## Chave Primária

- CodSla
- DatOcu
- HorIni
- CodRei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R140SOR_002

**Tabela:** R140SOC

| Origem | Destino |
|--------|---------|
| CodSla | CodSla |
| DatOcu | DatOcu |
| HorIni | HorIni |

### IR_R140SOR_003

**Tabela:** R140REI

| Origem | Destino |
|--------|---------|
| CodRei | CodRei |

