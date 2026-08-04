# E001TNC

## Descrição

Tabelas - Transações Complementar

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação origem |
| CodLan | String(006) | Sim | Código do Lançamento |
| BasCre | Number(002,0) | Sim | Código da base de cálculo do crédito (tabela 4.3.7 SPED Pis/Cofins) |
| OpeAnp | Number(007,0) | Sim | Código da operação conforme cadastro da ANP |
| CodPri | String(004) | Sim | Código da tabela de presunção IRPJ |
| CodPrc | String(004) | Sim | Código da tabela de presunção CSLL |
| TipMov | String(001) | Sim | Tipo da movimentação para o SPED fiscal |
| CodAn2 | Number(007,0) | Sim | Código de operação de agente não cadastrado |
| USU_CodLan | String(006) | Sim | Codigo do Lancamento Secundario |
| USU_CodLa2 | String(006) | Sim | Codigo do Lancamento Terciario |

---

## Chave Primária

- CodEmp
- CodTns

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E001TNC_001

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

