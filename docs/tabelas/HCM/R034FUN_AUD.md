# R034FUN_AUD

## Descrição

Auditoria Ficha Básica Colaborador

---

## Resumo

- Campos: 34
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(015,0) | Não | Sequencia do Registro |
| VerSeq | Number(010,0) | Não | Versão da Sequencia |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colabolador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| NomFun | String(040) | Sim | Nome do Colaborador |
| ApeFun | String(050) | Sim | Apelido do Colaborador |
| DatAdm | Date | Sim | Data de Admissão |
| SitAfa | Number(003,0) | Sim | Situação de Afastamento |
| TipCon | Number(002,0) | Sim | Tipo de Contrato |
| TipSex | String(001) | Sim | Sexo do Colaborador |
| EstCiv | Number(001,0) | Sim | Estado Civil |
| DatNas | Date | Sim | Data de Nascimento |
| CodNac | Number(003,0) | Sim | Código da Nacionalidade |
| AnoChe | Number(004,0) | Sim | Ano de Chegada |
| VisEst | Number(002,0) | Sim | Classificação da condição do estrangeiro no Brasil |
| RegEst | String(014) | Sim | Carteira de Estrangeiro |
| DvlEst | Date | Sim | Data de Validade da Carteira de Estrangeiro |
| DvlCtp | Date | Sim | Data de Validade da Carteira de Trabalho (Estrangeiro) |
| NumCtp | Number(009,0) | Sim | Número da Carteira de Trabalho |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| NumPis | Number(011,0) | Sim | Número do PIS/PASEP |
| DcdPis | Date | Sim | Data de Cadastramento no PIS/PASEP |
| DatAfa | Date | Sim | Data do Último Afastamento |
| HorAfa | Number(005,0) | Sim | Hora do Último Afastamento |
| EmpRes | Number(004,0) | Sim | Código da Empresa Responsável |
| TipRes | Number(001,0) | Sim | Tipo de Colaborador Responsável |
| CadRes | Number(009,0) | Sim | Cadastro do Responsável |
| TipTer | Number(003,0) | Sim | Tipo de Terceiro |
| ApuPfs | String(001) | Sim | Apuração do Professor |
| NumPsp | String(020) | Sim | Número Passaporte para controle Alfandegado. |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| StaAlf | Number(001,0) | Sim | Status da permissão para o local alfandegado |

---

## Chave Primária

- SeqReg
- VerSeq
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
