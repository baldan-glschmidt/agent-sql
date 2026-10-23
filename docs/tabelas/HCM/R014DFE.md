# R014DFE

## Descrição

Direito de Férias

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| DiaSem | Number(001,0) | Não | Dias trabalhados durante a semana |
| DiaFal | Number(003,0) | Não | Dias de Faltas |
| DiaDir | Number(002,0) | Sim | Dias de Direito |
| DiaAno | Number(003,0) | Sim | Dias trabalhados durante o ano |

---

## Chave Primária

- CodSin
- DiaSem
- DiaFal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014DFE_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

