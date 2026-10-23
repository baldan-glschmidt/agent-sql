# R127CFA

## Descrição

Custos por Cursos de Formação - Faixa Salarial

---

## Resumo

- Campos: 6
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCuf | Number(004,0) | Sim | Código do Curso de Formação |
| CodOem | Number(008,0) | Sim | Código da Entidade |
| CmpCus | Date | Sim | Competência do Item de Custo |
| AbrSub | String(030) | Sim | Subsídios |
| VlrAte | Number(011,2) | Sim | Faixa de Valor Até |
| PerCus | Number(005,2) | Sim | Percentual Custo |

---

## Chave Primária

Não possui.

---

## Índices

### R127CFAIndice1

**Tipo:** Não unico

Campos:
- CodCuf
- CodOem
- CmpCus
- AbrSub

---

## Relacionamentos

### IR_R127CFA_003

**Tabela:** R127CSU

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |
| CodOem | CodOem |
| CmpCus | CmpCus |
| AbrSub | AbrSub |

