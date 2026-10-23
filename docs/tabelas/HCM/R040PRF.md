# R040PRF

## Descrição

Publicação Recibo de Férias - Mestre

---

## Resumo

- Campos: 36
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| IniPer | Date | Não | Data Início do Período |
| FimPer | Date | Sim | Data Fim do Período |
| IniFer | Date | Não | Data Início das Férias |
| DatPag | Date | Sim | Data Pagto do Recibo |
| RetTra | Date | Sim | Data de retorno ao trabalho |
| DiaFer | Number(004,2) | Sim | Dias de Férias |
| DiaAbo | Number(004,2) | Sim | Dias de Abono |
| DiaLic | Number(004,2) | Sim | Dias Lic.Rem.Fer.Col |
| FimFer | Date | Sim | Fim Férias |
| SalBas | Number(013,4) | Sim | Salário Base |
| LicRem | Number(004,2) | Sim | Dias Licença Remunerada |
| QtdDep | Number(002,0) | Sim | Qtd. Dependentes |
| NomEmp | String(040) | Sim | Razão Social da Empresa/Filial |
| CodFil | Number(006,0) | Sim | Código da Filial |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição da Filial |
| NumCgc | Number(015,0) | Sim | Número da Inscrição |
| CfjIns | String(014) | Sim | Número da Inscrição |
| NomFun | String(040) | Sim | Nome do Colaborador |
| NomCom | String(080) | Sim | Nome Completo |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| TitCar | String(100) | Sim | Título do Cargo |
| NumCtp | Number(009,0) | Sim | Número da Carteira de Trabalho |
| SerCtp | String(005) | Sim | Série da Carteira de Trabalho |
| EstCtp | String(002) | Sim | UF da Carteira de Trabalho |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| NomCid | String(030) | Sim | Nome da Cidade |
| ValLiq | Number(013,4) | Sim | Valor total líquido |
| ValExt | String(255) | Sim | Valor líquido extenso |
| ValPro | Number(013,4) | Sim | Valor total proventos |
| ValDes | Number(013,4) | Sim | Valor total descontos |
| AssDig | String(001) | Sim | Gerado com assinatura digitalizada RH |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniPer
- IniFer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
