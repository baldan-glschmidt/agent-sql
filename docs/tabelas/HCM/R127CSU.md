# R127CSU

## Descrição

Custos por Cursos de Formação - Subsídios

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCuf | Number(004,0) | Não | Código do Curso de Formação |
| CodOem | Number(008,0) | Não | Código da Entidade |
| CmpCus | Date | Não | Competência do Item de Custo |
| AbrSub | String(030) | Não | Subsídios |
| TipSub | String(001) | Sim | Tipo de Subsídio |
| QtdSub | Number(011,2) | Sim | Subsídio do Item de Custo |
| TipTet | String(001) | Sim | Tipo do Teto |
| QtdTet | Number(011,2) | Sim | Teto p/comprometimento |
| IndSal | String(001) | Sim | Indicar Aplicação % do Salário |
| PerSal | Number(005,2) | Sim | Percentual Salário |

---

## Chave Primária

- CodCuf
- CodOem
- CmpCus
- AbrSub

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R127CSU_002

**Tabela:** R127CCU

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |
| CodOem | CodOem |
| CmpCus | CmpCus |

