# E046PLA

## Descrição

Tabelas - Visões Contábeis - Plano de Contas

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodVis | String(020) | Não | Código da visão |
| CtaVis | Number(009,0) | Não | Conta da visão |
| DesCta | String(100) | Sim | Descrição da conta |
| ClaCta | String(025) | Sim | Classificação da conta |
| NivCta | Number(002,0) | Sim | Nível da conta |
| IndTot | String(001) | Sim | Indicativo se a conta é uma totalizadora |
| NumOrd | Number(009,0) | Sim | Contém o valor que será gerado no Registro J150 - NU_ORDEM do SPED ECD |

---

## Chave Primária

- CodEmp
- CodVis
- CtaVis

---

## Índices

### E046PLAIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodVis
- ClaCta

---

## Relacionamentos

### IR_E046PLA_001

**Tabela:** E046VIS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodVis | CodVis |

