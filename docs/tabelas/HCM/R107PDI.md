# R107PDI

## Descrição

PDI - Plano de desenvolvimento individual

---

## Resumo

- Campos: 21
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo de colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| CodPln | Number(004,0) | Não | Código do plano de desenvolvimento |
| DesPln | String(100) | Sim | Descrição do plano de desenvolvimento |
| OriPln | Number(001,0) | Sim | Origem do plano de desenvolvimento individual |
| DatPln | Date | Sim | Data de início do plano de desenvolvimento |
| PraPln | Date | Sim | Data de término do plano de desenvolvimento |
| CodCic | Number(003,0) | Sim | Código do ciclo de avaliação |
| EstCar | Number(004,0) | Sim | Estrutura de Cargos |
| CodCar | String(024) | Sim | Cargo |
| CodCrr | Number(003,0) | Sim | Código da Carreira |
| CodDia | Number(009,0) | Sim | Código Diagnóstico |
| AvrCon | String(001) | Sim | Indica se o Responsável tomou conhecimento do plano de desenvolvimento de seu liderado |
| AvaCon | String(001) | Sim | Indica se o Colaborador tomou conhecimento do seu plano de desenvolvimento |
| EmpRsp | Number(004,0) | Sim | Empresa do Responsável pelo plano de desenvolvimento |
| TipRsp | Number(001,0) | Sim | Tipo do Colaborador Responsável pelo plano de desenvolvimento |
| CadRsp | Number(009,0) | Sim | Cadastro do Responsável pelo plano de desenvolvimento |
| CodUsu | Number(010,0) | Sim | Código do usuário que criou o plano de desenvolvimento |
| NumLot | Number(009,0) | Sim | Núm. do lote em que foi gerado o Plano de Desenvolvimento |
| CodPer | Number(004,0) | Sim | Perfil de PDI Web |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPln

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
