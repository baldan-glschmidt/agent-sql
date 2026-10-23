# R073ALU

## Descrição

Alunos

---

## Resumo

- Campos: 31
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumMat | String(015) | Não | Matrícula do Aluno |
| NomAlu | String(050) | Sim | Nome do Aluno |
| ApeAlu | String(020) | Sim | Apelido do Aluno |
| TipSex | String(001) | Sim | Sexo do Aluno |
| DatNas | Date | Sim | Data de Nascimento do Aluno |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| NumDoc | String(020) | Sim | Número do Documento do Aluno |
| GraIns | Number(002,0) | Sim | Grau de Instrução do Aluno |
| EndRua | String(040) | Sim | Endereço Residencial |
| EndNum | String(006) | Sim | Número |
| EndCpl | String(025) | Sim | Complemento Endereço |
| CodCid | Number(007,0) | Sim | Cidade |
| CodBai | Number(004,0) | Sim | Bairro |
| EndCep | Number(008,0) | Sim | CEP |
| NumTel | String(020) | Sim | Número do Telefone |
| EmaAlu | String(050) | Sim | E-mail do Aluno |
| CodPrm | Number(005,0) | Sim | Permissão de Acesso para Dias Normais |
| PrmSab | Number(005,0) | Sim | Permissão de Acesso para os Sábados |
| PrmDom | Number(005,0) | Sim | Permissão de Acesso para os Domingos |
| PrmFer | Number(005,0) | Sim | Permissão de Acesso para os Feriados |
| ValAut | String(001) | Sim | Necessita de Validação do Responsável |
| ConTpm | String(001) | Sim | Controla tempo de permanência |
| ConRee | String(001) | Sim | Controla Tempo Mínimo de Reentrada |
| UsaBio | Number(001,0) | Sim | Utiliza Controle Biométrico |
| GraCon | Number(003,0) | Sim | Grau de Conferência na Biometria |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |
| NumEnd | String(006) | Sim | Número do endereço |
| UtiChv | String(001) | Sim | Pode usar chave |
| ConAdp | String(001) | Sim | Controla Nível e Anti-Dupla |
| UsaRFa | String(001) | Sim | Utiliza Reconhecimento Facial |

---

## Chave Primária

- NumMat

---

## Índices

### R073ALUIndice2

**Tipo:** Não unico

Campos:
- NomAlu

---

## Relacionamentos

Nenhum relacionamento cadastrado.
