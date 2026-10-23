# R127FFA

## Descrição

Custos por Fases Curso de Formação - Faixa Salarial

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NivCuf | Number(002,0) | Não | Nível de Formação do Curso |
| SeqNiv | Number(002,0) | Não | Sequência do Nível |
| FasCuf | String(003) | Não | Fase do Curso de Formação |
| CodOem | Number(008,0) | Não | Código da Entidade |
| CmpCus | Date | Não | Competência do Item de Custo |
| AbrSub | String(030) | Não | Subsídios |
| VlrAte | Number(011,2) | Não | Faixa de Valor Até |
| PerCus | Number(005,2) | Sim | Percentual Custo |

---

## Chave Primária

- NivCuf
- SeqNiv
- FasCuf
- CodOem
- CmpCus
- AbrSub
- VlrAte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R127FFA_005

**Tabela:** R127FSU

| Origem | Destino |
|--------|---------|
| NivCuf | NivCuf |
| SeqNiv | SeqNiv |
| FasCuf | FasCuf |
| CodOem | CodOem |
| CmpCus | CmpCus |
| AbrSub | AbrSub |

