# R347BEA

## Descrição

Auxiliar de S-2416 - Cadastro de Benefício - Entes Públicos - Alteração

---

## Resumo

- Campos: 23
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqBea | Number(009,0) | Não | Sequência |
| NroBen | String(020) | Não | Número do Benefício |
| DatAlt | Date | Não | Data Alteração do Benefício |
| TipBen | Number(004,0) | Não | Tipo Benefício |
| PanSeg | Number(001,0) | Não | Tipo de plano de segregação da massa |
| DscBen | String(255) | Não | Descrição do instrumento ou situação que originou o pagamento do benefício |
| PenMor | Number(001,0) | Não | Tipo de pensão por morte |
| IndSus | String(001) | Sim | Indicativo de suspensão do benefício |
| MtvSus | Number(002,0) | Não | Motivo da suspensão do benefício |
| DscSus | String(255) | Não | Descrição do motivo da suspensão do benefício |
| CPLI01 | Number(009,0) | Sim | Campo inteiro para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPLI02 | Number(009,0) | Sim | Campo inteiro para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPLI03 | Number(009,0) | Sim | Campo inteiro para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPLS01 | String(255) | Sim | Campo alfanumérico para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPLS02 | String(255) | Sim | Campo alfanumérico para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPDT01 | Date | Sim | Campo data para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPLT01 | Number(005,0) | Sim | Campo hora para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPLL01 | String(4096) | Sim | Campo lob para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| TipDep | Number(002,0) | Sim | Tipo de dependente do instituidor da pensão por morte |
| DesDep | String(100) | Sim | Descrição da dependência do instituidor da pensão por morte |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqBea

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
