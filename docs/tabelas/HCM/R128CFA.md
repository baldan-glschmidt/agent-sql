# R128CFA

## Descrição

Custos por Cursos de Aperfeiçoamento - Faixa Salarial

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
| CodCua | Number(009,0) | Sim | Código do Curso de Aperfeiçoamento |
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

### R128CFAIndice1

**Tipo:** Não unico

Campos:
- CodCua
- CodOem
- CmpCus
- AbrSub

---

## Relacionamentos

### IR_R128CFA_003

**Tabela:** R128CSU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| CodOem | CodOem |
| CmpCus | CmpCus |
| AbrSub | AbrSub |

