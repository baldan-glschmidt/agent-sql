# R014DDF

## Descrição

Direito de Férias p/ Data

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| DatAlt | Date | Não | Data Alteração |
| DiaSem | Number(001,0) | Não | Dias trabalhados durante a semana |
| DiaAno | Number(003,0) | Sim | Dias trabalhados durante o ano |
| DiaFal | Number(003,0) | Não | Dias de Faltas |
| DiaDir | Number(002,0) | Sim | Dias de Direito |

---

## Chave Primária

- CodSin
- DatAlt
- DiaSem
- DiaFal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014DDF_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

