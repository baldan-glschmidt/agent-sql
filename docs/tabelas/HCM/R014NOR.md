# R014NOR

## Descrição

Salários Normativos

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| CmpNor | Date | Não | Competência Sal.Normativo |
| SelCar | String(001) | Sim | Seleção por Cargo |
| SelIda | String(001) | Sim | Seleção por Idade |
| SelSer | String(001) | Sim | Seleção por Tempo Serviço |
| SelTsa | String(001) | Sim | Seleção por Tipo Salário |
| SalNor | Number(011,2) | Sim | Salário Normativo Básico |
| MinTer | Number(011,2) | Sim | Mínimo 1/3 Férias |

---

## Chave Primária

- CodSin
- CmpNor

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014NOR_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

