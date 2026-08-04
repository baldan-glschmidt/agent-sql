# E037FRJ

## Descrição

Tabelas - Fórmulas de Reajustes

---

## Resumo

- Campos: 19
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFrj | String(003) | Não | Código da fórmula de reajuste |
| DesFrj | String(030) | Não | Descrição da fórmula de reajuste |
| CodMoe | String(003) | Sim | Código da moeda/índice de reajuste |
| DatFrj | Number(001,0) | Sim | Data base para cálculo do reajuste |
| CodCpg | String(006) | Sim | Código da condição de pagamento da fórmula de reajuste |
| IndEnt | String(001) | Sim | Indicativo se é necessário entrada na fórmula de reajuste |
| IndTax | String(001) | Sim | Indicativo se será cobrada taxa na fórmula de reajuste |
| TaxFrj | Number(013,10) | Sim | Percentual de taxa da fórmula de reajuste |
| TxtFrj | String(250) | Sim | Texto do cálculo da fórmula de reajuste |
| SitFrj | String(001) | Sim | Situação da fórmula de reajuste |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| TipEnt | Number(001,0) | Sim | Indica como a entrada será tratada na fórmula de reajuste |
| TptEnt | String(003) | Sim | Código do tipo de título da entrada na fórmula de reajuste |
| TnsEnt | String(005) | Sim | Código de transação da entrada na fórmula de reajuste |
| CalTxp | String(001) | Sim | Indica se o cálculo da taxa será pela tabela price |
| PerDtn | Number(013,10) | Sim | Percentual de desconto para títulos não vencidos |

---

## Chave Primária

- CodEmp
- CodFrj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E037FRJ_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

