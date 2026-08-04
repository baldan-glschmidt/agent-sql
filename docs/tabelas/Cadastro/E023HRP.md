# E023HRP

## Descrição

Tabelas - Grupos de Contas a Receber ou Pagar - Contas por Empresa

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCrp | String(003) | Não | Código do grupo de contas a receber ou pagar |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRdv | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |

---

## Chave Primária

- CodCrp
- CodEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E023HRP_000

**Tabela:** E023CRP

| Origem | Destino |
|--------|---------|
| CodCrp | CodCrp |

