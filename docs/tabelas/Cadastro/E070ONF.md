# E070ONF

## Descrição

Integrações - Varejo - Operações de nota fiscal

---

## Resumo

- Campos: 20
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodOpe | Number(004,0) | Não | Código da operação de nota fiscal |
| DesOpe | String(100) | Sim | Descrição da operação de nota fiscal |
| AplOpe | String(001) | Sim | Aplicação da operação de nota fiscal |
| SitOpe | String(001) | Sim | Situação do registro de operação de nota fiscal |
| FinNfs | Number(001,0) | Sim | Finalidade da operação de nota fiscal |
| CodSnf | String(003) | Sim | Código da série da nota fiscal |
| TnsEst | String(005) | Sim | Transação para natureza de operação estadual |
| TnsIes | String(005) | Sim | Transação para natureza de operação interestadual |
| TnsEpn | String(005) | Sim | Transação estadual para produtos com tributação de ICMS normal |
| TnsEps | String(005) | Sim | Trans. estadual p/ produtos com tributação de ICMS por substituição tributária |
| TnsIpn | String(005) | Sim | Transação interestadual para produtos com tributação de ICMS normal |
| TnsIps | String(005) | Sim | Trans. interestadual p/ prod. com tributação de ICMS por substituição tributária |
| TnsEsi | String(005) | Sim | Transação estadual para serviços sujeitos a tributação de ISS |
| TnsIsi | String(005) | Sim | Transação interestadual para serviços sujeitos a tributação de ISS |
| TnsEsn | String(005) | Sim | Transação estadual para serviços com tributação de ICMS normal |
| TnsEss | String(005) | Sim | Transação estadual p/ serviços com tribut. de ICMS por substituição tributária |
| TnsIsn | String(005) | Sim | Transação interestadual para serviços com tributação de ICMS normal |
| TnsIss | String(005) | Sim | Transação interestadual p/ serv. c/ tribut. de ICMS por substituição tributária |

---

## Chave Primária

- CodEmp
- CodFil
- CodOpe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E070ONF_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

