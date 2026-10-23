# R048CLC

## Descrição

Códigos Lançto Contábil (CLC)

---

## Resumo

- Campos: 14
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código Lançamento Contábil |
| NomCon | String(100) | Sim | Descrição do Código de Lançamento Contábil |
| TipLan | String(001) | Sim | Tipo Lançamento |
| NivLan | String(001) | Sim | Nível Lançamento |
| PerCal | Number(007,4) | Sim | Percentual de Cálculo |
| HisPad | Number(004,0) | Sim | Código Histórico Padrão |
| CplHis | String(100) | Sim | Complemento do Histórico Padrão |
| RegCal | Number(003,0) | Sim | Regra de Cáculo |
| ExeReg | String(001) | Sim | Define Quando a Regra Deve Ser Executada |
| BasClc | String(001) | Sim | Tipo de Base |
| CodTcl | Number(004,0) | Sim | Tipo CLC |
| ConAux | String(001) | Sim | CLC Possui Contas Auxiliares (S,N) |
| CodFor | Number(009,0) | Sim | Código Fornecedor |

---

## Chave Primária

- TabEve
- CodClc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R048CLC_000

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

