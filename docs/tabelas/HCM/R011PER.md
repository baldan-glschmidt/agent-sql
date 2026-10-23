# R011PER

## Descrição

Periodicidade do Banco de Horas

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBHr | Number(005,0) | Não | Código do Banco de Horas |
| DatIni | Date | Não | Data Inicial do Período |
| DatFim | Date | Sim | Data Final do Período |
| FecCre | String(001) | Sim | Periodicidade do Fechamento dos Créditos do Banco |
| LimCre | Number(003,0) | Sim | Limite de Compensação dos Créditos |
| TmLCre | String(001) | Sim | Tempo Limite dos Créditos do Banco de Horas |
| FecDeb | String(001) | Sim | Periodicidade do Fechamento dos Débitos do Banco |
| LimDeb | Number(003,0) | Sim | Limite de Compensação dos Débitos |
| TmLDeb | String(001) | Sim | Tempo Limite dos Débitos do Banco de Horas |

---

## Chave Primária

- CodBHr
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R011PER_000

**Tabela:** R011BHR

| Origem | Destino |
|--------|---------|
| CodBHr | CodBHr |

