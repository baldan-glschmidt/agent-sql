# R111CAM

## Descrição

Vacinação - Campanha

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodCam | Number(004,0) | Não | Código de identificação da campanha |
| DesCam | String(040) | Sim | Descrição da campanha de vacinação |
| ObsCam | String(2000) | Sim | Observações da campanha |
| SexMas | String(001) | Sim | Sexo para filtrar na geração de solicitação de vacina. |
| IdMinM | Number(003,0) | Sim | Idade mínima para colaboradores do sexo masculino |
| IdMaxM | Number(003,0) | Sim | Idade máxima para colaboradores do sexo masculino |
| SexFem | String(001) | Sim | Sexo para filtrar na geração de solicitação de vacina. |
| IdMinF | Number(003,0) | Sim | Idade mínima para colaboradores do sexo feminino |
| IdMaxF | Number(003,0) | Sim | Idade máxima para colaboradores do sexo feminino |
| AbrSub | String(100) | Sim | Abrangência de subnormalidade para ser considerada da geração de solicitação |
| AbrFil | String(100) | Sim | Abrangência de Filial para ser considerada da geração de solicitação |

---

## Chave Primária

- NumEmp
- CodCam

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
