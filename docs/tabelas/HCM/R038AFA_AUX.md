# R038AFA_AUX

## Descrição

Afastamentos  -  TRIGGERS

---

## Resumo

- Campos: 30
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro Colaborador |
| DatAfa | Date | Sim | Data do Afastamento |
| HorAfa | Number(005,0) | Sim | Hora do Afastamento |
| DatTer | Date | Sim | Data do Término do Afastamento |
| HorTer | Number(005,0) | Sim | Hora do Término do Afastamento |
| PrvTer | Date | Sim | Data Término Previsto |
| SitAfa | Number(003,0) | Sim | Situação de Afastamento |
| CauDem | Number(002,0) | Sim | Causa Demissão do Colaborador |
| DiaJus | Number(002,0) | Sim | Dias Justificados |
| FimQua | Date | Sim | Data fim remuneração após o desligamento/término |
| QhrAfa | Number(005,0) | Sim | Qtde de Horas Faltas no Afastamento |
| OriAfa | Number(001,0) | Sim | 0=Afast, 1=Perda Férias, 2=Medicina, 3=Aut. Saída, 4=Treinamento, 5=Troca Filial |
| ExmRet | String(001) | Sim | Exame de Retorno |
| ConTov | String(001) | Sim | Considerar Demissão p/ Cálculo do Turn-Over |
| ObsAfa | String(080) | Sim | Observação do Afastamento |
| StaAtu | Number(001,0) | Sim | Status do Histórico |
| SitAnt | Number(003,0) | Sim | Situação Anterior a Alteração |
| EmpOld | Number(004,0) | Sim | Código da Empresa |
| TipOld | Number(001,0) | Sim | Tipo Colaborador |
| CadOld | Number(009,0) | Sim | Cadastro Colaborador |
| DtAOld | Date | Sim | Data do Afastamento |
| HAfOld | Number(005,0) | Sim | Hora do Afastamento |
| DtTOld | Date | Sim | Data do Término do Afastamento |
| NroAut | String(015) | Sim | Número de Autorização |
| CodOem | Number(008,0) | Sim | Adm. Seguridade |
| DiaBlq | Number(001,0) | Sim | Número de dias que o crachá será bloqueado |
| SitOri | Number(003,0) | Sim | Situação original do afastamento |
| MotAlt | String(001) | Sim | Indica se o afastamento atual é uma alteração de situação não retroativa. |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
