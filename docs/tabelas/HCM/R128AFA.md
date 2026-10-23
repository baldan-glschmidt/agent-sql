# R128AFA

## Descrição

Custos por Assunto - Faixa Salarial

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
| CodAss | Number(004,0) | Sim | Código do Assunto |
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

### R128AFAIndice1

**Tipo:** Não unico

Campos:
- CodAss
- CodOem
- CmpCus
- AbrSub

---

## Relacionamentos

### IR_R128AFA_003

**Tabela:** R128ASU

| Origem | Destino |
|--------|---------|
| CodAss | CodAss |
| CodOem | CodOem |
| CmpCus | CmpCus |
| AbrSub | AbrSub |

