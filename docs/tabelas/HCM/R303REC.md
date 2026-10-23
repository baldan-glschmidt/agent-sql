# R303REC

## Descrição

e-Sfinge - Concursos/Resultado do Concurso

---

## Resumo

- Campos: 18
- Chave Primária: 11 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano |
| BimAno | Number(001,0) | Não | Código Bimestre Ano |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| Edital | String(016) | Não | Número do edital de concurso |
| Especi | Number(006,0) | Não | Número da especialidade |
| NumIns | Number(016,0) | Não | Número de inscrição do candidato no concurso |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CodCar | String(016) | Não | Código do Cargo |
| VigCar | Date | Não | Data de Início da Vigência do Cargo |
| NumCpf | Number(011,0) | Não | Número do CPF do aprovado |
| NomApr | String(100) | Não | Nome do aprovado no concurso |
| NumCla | Number(007,0) | Não | Número de classificação do aprovado na especialidade |
| DatDes | Date | Sim | Data que participante do concurso foi desabil. por não preencher req. do edital |
| IndDef | String(001) | Não | Indica se o candidato possui deficiência |
| NotApr | Number(007,4) | Sim | Nota final do aprovado |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- TipCol
- NumCad
- Edital
- Especi
- NumIns
- TipQua
- CodCar
- VigCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R303REC_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

