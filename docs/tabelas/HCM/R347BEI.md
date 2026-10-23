# R347BEI

## Descrição

Auxiliar de S-2410 - Cadastro de Benefício - Entes Públicos - Início

---

## Resumo

- Campos: 29
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
| SeqBei | Number(009,0) | Não | Sequência |
| NroBen | String(020) | Não | Número do Benefício |
| DatIni | Date | Não | Data Início do Benefício |
| SitBen | Number(001,0) | Não | Indicar a situação do benefício no órgão declarante |
| DatPub | Date | Não | Data de publicação da concessão do benefício |
| TipBen | Number(004,0) | Não | Tipo Benefício |
| MatEso | String(030) | Não | Matrícula do servidor/militar no Sistema de RH do órgão cujo vínculo deu ensejo ao benefício |
| CNPJOr | Number(014,0) | Não | CNPJ do órgão público responsável pela matrícula |
| CfjOri | String(014) | Sim | CNPJ do órgão público responsável pela matrícula |
| PanSeg | Number(001,0) | Não | Tipo de plano de segregação da massa |
| DscBen | String(255) | Não | Descrição do instrumento ou situação que originou o pagamento do benefício |
| DetJud | String(001) | Sim | Benefício foi concedido por determinação judicial |
| PenMor | Number(001,0) | Não | Tipo de pensão por morte |
| CpfIns | Number(011,0) | Não | CPF do instituidor da pensão por morte |
| DatIns | Date | Não | Data de óbito do instituidor da pensão por morte |
| CNPJAn | Number(014,0) | Não | CNPJ do órgão público anterior |
| CfjAnt | String(014) | Sim | CNPJ do órgão público anterior |
| BenAnt | String(020) | Não | Número do Benefício Anterior |
| DatSuc | Date | Não | Data da transferência do benefício para o órgão público declarante |
| DscSuc | String(255) | Não | Observação Sucessão |
| DatTer | Date | Não | Data de término do benefício. |
| MtvTer | Number(002,0) | Não | Motivo da cessação do benefício |
| SitHom | Number(002,0) | Sim | Situação da homologação |
| DatHom | Date | Sim | Data da homologação do benefício pelo Tribunal de Contas competente |
| TipDep | Number(002,0) | Sim | Tipo de dependente do instituidor da pensão por morte |
| DesDep | String(100) | Sim | Descrição da dependência do instituidor da pensão por morte |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqBei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
