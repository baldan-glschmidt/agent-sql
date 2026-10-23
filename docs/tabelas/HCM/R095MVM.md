# R095MVM

## Descrição

Movimentação de Materiais

---

## Resumo

- Campos: 25
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatMov | Date | Não | Data da Movimentação de Materiais |
| HorMov | Number(005,0) | Não | Hora da Movimentação de Materiais |
| SeqMov | Number(002,0) | Não | Sequência do Registro |
| CodMat | String(008) | Sim | Código do Material |
| DesMat | String(040) | Sim | Descrição do Material |
| QtdMat | Number(006,0) | Sim | Quantidade |
| TipMov | String(001) | Sim | Tipo de Movimentação |
| TipPes | Number(001,0) | Sim | Tipo de pessoa usuária de controle de materiais |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |
| EmpOcr | Number(004,0) | Sim | Código da Empresa |
| CadOcr | Number(009,0) | Sim | Cadastro do Colaborador de Outra Unidade |
| NumMat | String(015) | Sim | Matrícula do Aluno |
| NfsEnt | Number(007,0) | Sim | Número da Nota Fiscal de Entrada |
| NfsSai | Number(007,0) | Sim | Número da Nota Fiscal de Saída |
| ObsMat | String(080) | Sim | Observação do Visitante |
| ObsAtu | String(080) | Sim | Observação da Autorização |
| CodUsu | Number(010,0) | Sim | Código do Usuário que registrou a Movimentação |
| RetMat | String(001) | Sim | Material Precisa de Retorno |
| StaMat | Number(001,0) | Sim | Status do Material na Saída |
| CodPor | Number(003,0) | Sim | Código da Portaria |
| SeqReg | Number(015,0) | Sim | Sequencia do Registro |

---

## Chave Primária

- DatMov
- HorMov
- SeqMov

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
