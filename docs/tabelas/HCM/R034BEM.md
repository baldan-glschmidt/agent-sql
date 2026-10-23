# R034BEM

## Descrição

Informações Benefício Extraordinário Mensal - B.E.M

---

## Resumo

- Campos: 36
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAco | Date | Não | Data em que foi firmado o acordo entre o empregador e o empregado |
| TipIns | Number(001,0) | Sim | Tipo de identificador do estabelecimento que fez o acordo |
| NumIns | Number(015,0) | Sim | Número identificador do estabelecimento responsável pelo acordo |
| CfjIns | String(014) | Sim | Número identificador do estabelecimento responsável pelo acordo |
| NumCNO | Number(012,0) | Sim | Nº identificador que contém informações cadastrais de obras de construção civil |
| DatAdm | Date | Sim | Data em que ocorreu a admissão do trabalhador no empregador |
| NumCpf | Number(011,0) | Sim | Número do CPF do trabalhador |
| NumPis | Number(011,0) | Sim | Número do PIS ou PASEP do trabalhador |
| NomTra | String(080) | Sim | Nome completo do trabalhador |
| NomMae | String(080) | Sim | Nome completo da mãe do trabalhador |
| DatNas | Date | Sim | Data de nascimento do trabalhador |
| TipAde | Number(001,0) | Sim | Tipo de adesão acordado entre o empregador e empregado |
| PerRed | Number(002,0) | Sim | Percentual de redução da carga horária |
| DurAco | Number(003,0) | Sim | Quantidade de dias de duração do acordo |
| CodBan | String(003) | Sim | Código bancário de 3 posições segundo a tabela FEBRABAN |
| AgeBan | Number(004,0) | Sim | Número da agência onde o trabalhador possui conta |
| DigAge | String(001) | Sim | Digíto verificador da agência bancária |
| ConBan | Number(012,0) | Sim | Número da conta bancária do trabalhador |
| DigBan | Number(001,0) | Sim | Dígito verificador da conta bancária do trabalhador |
| TipCon | Number(001,0) | Sim | Tipo da conta bancária do trabalhador |
| UltSal | Number(013,2) | Sim | Salário recebido pelo trabalhador no mês em questão |
| PenSal | Number(013,2) | Sim | Salário recebido pelo trabalhador no mês em questão |
| AntSal | Number(013,2) | Sim | Salário recebido pelo trabalhador no mês em questão |
| OriReg | Number(001,0) | Sim | Origem do registro |
| CmpAu1 | Number(011,2) | Sim | Campo Auxiliar 1 |
| CmpAu2 | Number(011,2) | Sim | Campo Auxiliar 2 |
| CmpAu3 | Number(009,0) | Sim | Campo Auxiliar 3 |
| CmpAu4 | Number(003,0) | Sim | Campo Auxiliar 4 |
| CmpAu5 | Date | Sim | Campo Auxiliar 5 |
| CmpAu6 | Date | Sim | Campo Auxiliar 6 |
| CmpAu7 | String(001) | Sim | Campo Auxiliar 7 |
| CmpAu8 | String(300) | Sim | Campo Auxiliar 8 |
| CmpAu9 | String(100) | Sim | Campo Auxiliar 9 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
