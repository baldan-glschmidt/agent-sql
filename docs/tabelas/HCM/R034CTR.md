# R034CTR

## Descrição

Contrato Temporário

---

## Resumo

- Campos: 26
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colabolador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data Início |
| MotCtr | Number(001,0) | Sim | Hipótese legal para contratação de trabalhador temporário |
| TipCtr | Number(001,0) | Sim | Tipo de contrato |
| IncCtr | Number(001,0) | Sim | Tipo de inclusão de contrato |
| JusCtr | String(5999) | Sim | Justificativa |
| CPFSbs | Number(011,0) | Sim | CPF do trabalhador substituído |
| MatSbs | String(030) | Sim | Matrícula do trabalhador que está sendo substituído - Obsoleto |
| SitGer | Number(001,0) | Sim | Situação da Geração |
| DatFim | Date | Sim | Data Fim |
| EndDif | String(001) | Sim | Endereço Diferente da Tomadora |
| CodPai | Number(004,0) | Sim | Código do País |
| CodEst | String(004) | Sim | Estado |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| CodBai | Number(004,0) | Sim | Código do Bairro |
| EndCep | Number(008,0) | Sim | Código Postal do Endereço |
| EndRua | String(100) | Sim | Endereço |
| EndNum | String(005) | Sim | Número |
| EndCpl | String(025) | Sim | Complemento |
| CodOem | Number(008,0) | Sim | Estabelecimento em que o trabalhador temporário está prestando serviço |
| TipIns | Number(001,0) | Sim | Tipo de inscrição do estabelecimento |
| NumIns | Number(015,0) | Sim | Número de inscrição do estabelecimento |
| CfjIns | String(014) | Sim | Número de inscrição do estabelecimento |
| TipLgr | String(005) | Sim | Tipo de Logradouro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034CTR_002

**Tabela:** R034CPL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

