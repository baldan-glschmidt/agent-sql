# R034BEN

## Descrição

Manutenção de benefícios - Órgão Público

---

## Resumo

- Campos: 48
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| NroBen | String(020) | Não | Número do Benefício |
| DatRef | Date | Não | Data Referência |
| TpReBn | Number(001,0) | Não | Tipo Registro do Benefício |
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
| IndSus | String(001) | Sim | Indicativo de suspensão do benefício |
| MtvSus | Number(002,0) | Não | Motivo da suspensão do benefício |
| DscSus | String(255) | Não | Descrição do motivo da suspensão do benefício |
| DatTer | Date | Não | Data de término do benefício |
| MtvTer | Number(002,0) | Não | Motivo da cessação do benefício |
| CNPJDs | Number(014,0) | Não | Informar o CNPJ do órgão público sucessor |
| CfjDes | String(014) | Sim | Informar o CNPJ do órgão público sucessor |
| SitTer | Number(003,0) | Não | Afastamento de Término Benefício |
| CauDem | Number(002,0) | Não | Causa Demissão do Colaborador |
| DatEfe | Date | Não | Data de início dos efeitos financeiros da reativação do benefício |
| SitRea | Number(003,0) | Não | Afastamento de Reativação de Benefício |
| EmpMat | Number(004,0) | Não | Empresa Matrícula |
| TipMat | Number(001,0) | Não | Tipo Colaborador Matrícula |
| CadMat | Number(009,0) | Não | Colaborador Matrícula |
| EmpIns | Number(004,0) | Não | Empresa Cnpj Origem |
| FilIns | Number(006,0) | Sim | Filial Cnpj Origem |
| MatIns | String(016) | Não | Matrícula do Instituidor TCE RS |
| CodPar | Number(002,0) | Sim | Código de Parentesco TCE RS |
| ObsPar | String(030) | Não | Observações Parentesco TCE RS - Definir o código de Parentesco 99-Outros |
| CmpAu1 | Number(009,0) | Sim | Campo Auxiliar 1 |
| CmpAu2 | String(100) | Sim | Campo Auxiliar 2 |
| SitHom | Number(002,0) | Sim | Situação da homologação |
| DatHom | Date | Sim | Data da homologação do benefício pelo Tribunal de Contas competente |
| TipDep | Number(002,0) | Sim | Tipo de dependente do instituidor da pensão por morte |
| DesDep | String(100) | Sim | Descrição da dependência do instituidor da pensão por morte |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- NroBen
- DatRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
