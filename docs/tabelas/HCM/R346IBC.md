# R346IBC

## Descrição

eSocial JR - Processo Trabalhista - Bases de cálculo

---

## Resumo

- Campos: 19
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
| CodPro | Number(009,0) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| PerRef | Date | Não | Mês/ano de referência das informações |
| BcCpMs | Number(015,2) | Sim | Valor da base de cálculo da contribuição previdenciária sobre a remuneração mensal |
| BcCp13 | Number(015,2) | Sim | Valor da base de cálculo da contribuição previdenciária sobre a remuneração do trabalhador referente ao 13º salário |
| BcFgts | Number(015,2) | Sim | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador (sem 13° salário) |
| BcFg13 | Number(015,2) | Sim | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador sobre o 13° salário |
| GraExp | Number(001,0) | Sim | Código que representa o grau de exposição a agentes nocivos |
| BcFgtG | Number(015,2) | Sim | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador (sem 13° salário) |
| BcF13G | Number(015,2) | Sim | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador sobre o 13° salário |
| ParDir | String(001) | Sim | O FGTS transacionado foi pago diretamente ao trabalhador mediante decisão/autorização judicial? |
| MudCat | String(001) | Sim | Houve mudança no código de categoria |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador declarado no período de referência |
| VrBcCP | Number(015,2) | Sim | Valor da remuneração do trabalhador a ser considerada para fins previdenciários |
| BcFg12 | Number(015,2) | Sim | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador (sem 13° salário) |
| BcFgSe | Number(015,2) | Sim | Valor da base de cálculo de FGTS declarada apenas em SEFIP (não informada no eSocial) e ainda não recolhida |
| BcFgEs | Number(015,2) | Sim | Valor da base de cálculo de FGTS declarada anteriormente no eSocial e ainda não recolhida |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro
- PerRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
