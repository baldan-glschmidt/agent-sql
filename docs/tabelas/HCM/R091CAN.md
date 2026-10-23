# R091CAN

## Descrição

Cadastro de Candidatos

---

## Resumo

- Campos: 19
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro do Candidato |
| NomCan | String(040) | Sim | Nome do Candidato |
| DatNas | Date | Sim | Data Nascimento |
| IdeCan | String(016) | Sim | Nº  da Carteira de Identidade - RG |
| CpfCan | Number(011,0) | Sim | CPF Candidato |
| EndCan | String(040) | Sim | Endereço Candidato |
| EndNum | String(006) | Sim | Número |
| EndCpl | String(025) | Sim | Complemento Endereço |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| CodBai | Number(004,0) | Sim | Código do Bairro |
| CodCep | Number(008,0) | Sim | Código CEP |
| TelCon | String(020) | Sim | Telefone de Contato |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma Desejado |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo Desejado |
| ObsCan | String(200) | Sim | Observações |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |

---

## Chave Primária

- NumCan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
