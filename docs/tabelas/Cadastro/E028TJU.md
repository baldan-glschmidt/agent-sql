# E028TJU

## Descrição

Tabelas - Integrações - Tabela de Juros

---

## Resumo

- Campos: 15
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumSeq | Number(009,0) | Não | Número sequencial do registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| DatIni | Date | Não | Data início de validade da tabela de juros |
| DatFim | Date | Não | Data final de validade da tabela de juros |
| CodFil | Number(005,0) | Sim | Código da filial |
| CodCpg | String(006) | Não | Código da condição de pagamento |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| CodFam | String(006) | Sim | Código da Família do Produto |
| CodOri | String(003) | Sim | Código de origem do produto |
| CodTpr | String(004) | Sim | Código da tabela de preço |
| CodPro | String(014) | Sim | Código do produto na tabela de juros |
| CodDer | String(007) | Sim | Código da derivação na tabela de juros |
| CodAgc | String(005) | Sim | Código de agrupamento comercial de produtos |
| AplTju | Number(002,0) | Sim | Aplicação da tabela de Juros |
| PerJur | Number(005,2) | Sim | Percentual de Juros |

---

## Chave Primária

- NumSeq

---

## Índices

### E028TJUIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodCpg

---

## Relacionamentos

### IR_E028TJU_005

**Tabela:** E028CPG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCpg | CodCpg |

