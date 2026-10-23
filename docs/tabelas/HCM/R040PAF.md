# R040PAF

## Descrição

Publicação Aviso de Férias - Mestre

---

## Resumo

- Campos: 22
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| IniFer | Date | Não | Data Início das Férias |
| OriAvi | Number(001,0) | Não | 0=Cálculo Recibo de Férias, 1=Programação Individual, 2=Programação Coletiva |
| IniPer | Date | Não | Data Início do Período |
| NomEmp | String(080) | Sim | Razão Social da Empresa/Filial |
| CodFil | Number(006,0) | Sim | Código da Filial |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição da Filial |
| NumCgc | Number(015,0) | Sim | Número da Inscrição |
| CfjIns | String(014) | Sim | Número da Inscrição |
| NomFun | String(080) | Sim | Nome do Colaborador |
| NomFil | String(080) | Sim | Nome Filial |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| TitCar | String(100) | Sim | Título do Cargo |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| NomCid | String(030) | Sim | Nome da Cidade |
| DatExt | String(255) | Sim | Data extenso |
| TexAvi | String(1000) | Sim | Texto - Descrição Aviso de Férias |
| AssDig | String(001) | Sim | Gerado com assinatura digitalizada RH |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniFer
- OriAvi
- IniPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
