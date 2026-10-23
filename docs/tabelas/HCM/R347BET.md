# R347BET

## Descrição

Auxiliar de S-2420 - Cadastro de Benefício - Entes Públicos - Término

---

## Resumo

- Campos: 17
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
| SeqBet | Number(009,0) | Não | Sequência |
| NroBen | String(020) | Não | Número do Benefício |
| DatTer | Date | Não | Data de término do benefício. |
| MtvTer | Number(002,0) | Não | Motivo da cessação do benefício |
| CNPJDs | Number(014,0) | Não | Informar o CNPJ do órgão público sucessor |
| CfjIns | String(014) | Sim | Informar o CNPJ do órgão público sucessor |
| CPLI01 | Number(009,0) | Sim | Campo inteiro para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPLI02 | Number(009,0) | Sim | Campo inteiro para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPLI03 | Number(009,0) | Sim | Campo inteiro para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPLS01 | String(255) | Sim | Campo alfanumérico para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPLS02 | String(255) | Sim | Campo alfanumérico para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPDT01 | Date | Sim | Campo data para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPLT01 | Number(005,0) | Sim | Campo hora para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |
| CPLL01 | String(4096) | Sim | Campo lob para uso diverso. NÃO UTILIZAR EM CUSTOMIZAÇÔES |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqBet

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
