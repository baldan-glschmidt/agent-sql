# R128GFA

## Descrição

Custos Geral - Faixa Salarial

---

## Resumo

- Campos: 5
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
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

### R128GFAIndice1

**Tipo:** Não unico

Campos:
- CodOem
- CmpCus
- AbrSub

---

## Relacionamentos

### IR_R128GFA_002

**Tabela:** R128GSU

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |
| CmpCus | CmpCus |
| AbrSub | AbrSub |

