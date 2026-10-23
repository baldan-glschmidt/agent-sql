# R038AFA_AUD

## Descrição

Auditoria Afastamentos

---

## Resumo

- Campos: 33
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(015,0) | Não | Sequencia do Registro |
| VerSeq | Number(010,0) | Não | Versão da Sequencia |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatAfa | Date | Não | Data do Afastamento |
| HorAfa | Number(005,0) | Não | Hora do Afastamento |
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
| ObsAfa | String(255) | Sim | Observação do Afastamento |
| StaAtu | Number(001,0) | Sim | Status do Histórico |
| MotRai | Number(002,0) | Sim | Motivo do Afastamento para a Rais |
| NroAut | String(015) | Sim | Número de Autorização |
| CodOem | Number(008,0) | Sim | Adm. Seguridade |
| CodSub | String(003) | Sim | Identificação do subgrupo da CID |
| DatPer | Date | Sim | Data da Decisão da Perícia do Nexo Epidemiológico |
| SitIni | Number(003,0) | Sim | Situação Inicial do Afastamento |
| RisNex | String(001) | Sim | Indica se há risco do afastamento ser convertido em acidente de trabalho (Nexo Epidemiológico) |
| DatNex | Date | Sim | Data de Início do Nexo Epidemiológico |
| DiaPrv | Number(004,0) | Sim | Dias Previsto Término |
| CodCua | Number(009,0) | Sim | Código do Curso que Originou o Afastamento |
| TmaCua | Number(006,0) | Sim | Código da Turma que Originou o Afastamento |
| DatPar | Date | Sim | Data do Parto |
| DiaBlq | Number(001,0) | Sim | Número de dias que o crachá será bloqueado |

---

## Chave Primária

- SeqReg
- VerSeq
- NumEmp
- TipCol
- NumCad
- DatAfa
- HorAfa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
