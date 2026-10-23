# R030PUB

## Descrição

Filial - Informações Órgão Publico

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatAlt | Date | Não | Data Alteração |
| IndSIA | String(006) | Sim | Número SIAFI |
| RegPro | String(001) | Sim | Regime Próprio de Previdência Social (S,N) |
| CodPai | Number(004,0) | Sim | Código do País da Federação |
| CodEst | String(004) | Sim | Estado da Federação |
| CodCid | Number(007,0) | Sim | Código da Cidade da Federação |
| TipOrg | Number(001,0) | Sim | Tipo de Órgão Público |
| InsEFR | Number(014,0) | Sim | CNPJ do Ente Federativo Responsável - EFR |
| CfjEfr | String(014) | Sim | CNPJ do Ente Federativo Responsável - EFR |
| NomEnt | String(100) | Sim | Nome do Ente Federativo ao qual o órgão está vinculado |
| TipPod | Number(001,0) | Sim | Poder a que se refere o subeto |
| ValSup | Number(014,2) | Sim | Valor do subteto do Ente Federativo |

---

## Chave Primária

- NumEmp
- CodFil
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030PUB_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

