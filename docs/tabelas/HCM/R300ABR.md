# R300ABR

## Descrição

Abrangências dos Processos Automáticos

---

## Resumo

- Campos: 40
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPat | Number(002,0) | Não | Tipo do Processo Automático |
| CodPro | Number(003,0) | Não | Código do Processo Automático |
| CodGru | Number(003,0) | Sim | Código do Grupo de Empresas |
| CodLot | Number(004,0) | Sim | Código de Lote de Colaboradores |
| AbrEmp | String(100) | Sim | Abrangência de Empresa |
| AbrTcl | String(100) | Sim | Abrangência de Tipo de Colaborador |
| AbrCad | String(100) | Sim | Abrangência de Colaborador |
| AbrFil | String(100) | Sim | Abrangência de Filial |
| AbrLoc | String(1500) | Sim | Abrangência de Local |
| AbrSin | String(100) | Sim | Abrangência de Sindicato |
| AbrTco | String(100) | Sim | Abrangência de Tipo de Contrato |
| AbrTsa | String(100) | Sim | Abrangência de Tipo de Salário |
| AbrVin | String(100) | Sim | Abrangência de Vínculo |
| AbrCar | String(100) | Sim | Abrangência de Cargo |
| AbrTrb | String(100) | Sim | Abrangência de Turno |
| AbrEsc | String(100) | Sim | Abrangência de Escala |
| AbrTma | String(100) | Sim | Abrangência de Turma de Escala |
| AbrCcu | String(200) | Sim | Abrangência de Centro de Custo |
| AbrEve | String(100) | Sim | Abrangência de Evento |
| CodPlt | Number(005,0) | Sim | Código do Site |
| AbrRlg | String(100) | Sim | Abrangência de Coletor |
| AbrUcr | String(100) | Sim | Abrangência de Uso de Crachá |
| CodGrr | Number(003,0) | Sim | Código do Grupo de Coletores |
| AbrOcr | String(100) | Sim | Abrangência de Outra Unidade |
| AbrTcr | String(100) | Sim | Abrangência de Tipo de Crachá |
| AbrMat | String(100) | Sim | Abrangência de Matrícula de Aluno |
| AbrCur | String(100) | Sim | Abrangência de Curso do Aluno |
| AbrFas | String(100) | Sim | Abrangência de Fase do Aluno |
| AbrDpf | String(100) | Sim | Abrangência de Disciplina do Aluno |
| AbrTrm | String(100) | Sim | Abrangência de Turma do Aluno |
| AbrTip | String(100) | Sim | Abrangência de Tipo de Documento |
| AbrDoc | String(100) | Sim | Abrangência de Documento |
| AbrPro | String(100) | Sim | Abrangência de Prontuário do Paciente |
| ISubNv | Number(001,0) | Sim | Inicializa Nível |
| CreAcc | Number(001,0) | Sim | Inicializa Créditos de Acesso |
| TipPav | String(050) | Sim | Tipo de Pessoa |
| AbrOem | String(100) | Sim | Abrangência de Outras Empresas |
| AbrSit | String(100) | Sim | Abrangência de Situação |
| GerLog | Number(001,0) | Sim | Gera LOG para listas |
| AbrCEs | String(100) | Sim | Abrângencia de Classe da Escala |

---

## Chave Primária

- TipPat
- CodPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R300ABR_001

**Tabela:** R300PRO

| Origem | Destino |
|--------|---------|
| TipPat | TipPat |
| CodPro | CodPro |

