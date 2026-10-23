# R128ASU

## Descrição

Custos por Assuntos - Subsídios

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
| CodAss | Number(004,0) | Não | Código do Assunto |
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

- CodAss
- CodOem
- CmpCus
- AbrSub

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128ASU_002

**Tabela:** R128ACU

| Origem | Destino |
|--------|---------|
| CodAss | CodAss |
| CodOem | CodOem |
| CmpCus | CmpCus |

