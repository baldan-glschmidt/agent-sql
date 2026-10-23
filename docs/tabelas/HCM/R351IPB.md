# R351IPB

## Descrição

S-2500 - eSocial - Identificação do período ao qual se referem as bases de cálculo

---

## Resumo

- Campos: 23
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CpfTra | Number(011,0) | Não | Número do CPF do trabalhador |
| IdeSeq | Number(005,0) | Não | Sequência parcial |
| SeqPtb | Number(009,0) | Não | Sequência |
| SeqIct | Number(009,0) | Não | Sequência |
| SeqIpb | Number(009,0) | Não | Sequência |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| PerRef | Date | Sim | Informar o mês/ano de referência das informações |
| BcCpMs | Number(015,2) | Sim | Valor da base de cálculo da contribuição previdenciária sobre a remuneração mensal do trabalhador |
| BcCp13 | Number(015,2) | Sim | Valor da base de cálculo da contribuição previdenciária sobre a remuneração do trabalhador referente ao 13º salário |
| BcFGTS | Number(015,2) | Sim | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador (sem 13° salário) |
| BcFG13 | Number(015,2) | Sim | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador sobre o 13º salário |
| GraExp | Number(001,0) | Sim | Código que representa o grau de exposição a agentes nocivos |
| VrBcFG | Number(015,2) | Sim | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador (sem 13° salário) |
| VrBc13 | Number(015,2) | Sim | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador sobre o 13º salário |
| PagDir | String(001) | Sim | O FGTS foi pago diretamente ao trabalhador mediante decisão/autorização judicial |
| CodCat | Number(004,0) | Sim | Código da categoria cujo contrato passou a integrar período de referência |
| VrBcCP | Number(015,2) | Sim | Valor da remuneração do trabalhador a ser considerada para fins previdenciários |
| BcFg12 | Number(015,2) | Sim | Valor da base de cálculo do FGTS sobre a remuneração do trabalhador (sem 13° salário) |
| BcFgSe | Number(015,2) | Sim | Valor da base de cálculo de FGTS declarada apenas em SEFIP (não informada no eSocial) e ainda não recolhida |
| BcFgEs | Number(015,2) | Sim | Valor da base de cálculo de FGTS declarada anteriormente no eSocial e ainda não recolhida |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- CpfTra
- IdeSeq
- SeqPtb
- SeqIct
- SeqIpb

---

## Índices

### R351IPBIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
