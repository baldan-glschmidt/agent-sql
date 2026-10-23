# R127NFA

## Descrição

Custos por Nível Curso de Formação - Faixa Salarial

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NivCuf | Number(002,0) | Não | Nível de Formação do Curso |
| CodOem | Number(008,0) | Não | Código da Entidade |
| CmpCus | Date | Não | Competência do Item de Custo |
| AbrSub | String(030) | Não | Subsídios |
| VlrAte | Number(011,2) | Não | Faixa de Valor Até |
| PerCus | Number(005,2) | Sim | Percentual Custo |

---

## Chave Primária

- NivCuf
- CodOem
- CmpCus
- AbrSub
- VlrAte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R127NFA_003

**Tabela:** R127NSU

| Origem | Destino |
|--------|---------|
| NivCuf | NivCuf |
| CodOem | CodOem |
| CmpCus | CmpCus |
| AbrSub | AbrSub |

