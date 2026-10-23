# R065MGV

## Descrição

Movimentação do Guarda Volumes

---

## Resumo

- Campos: 16
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodGvl | String(010) | Não | Código da Guarda Volume |
| DatUso | Date | Não | Data de Uso do Guarda Volume |
| HorUso | Number(005,0) | Não | Hora do Uso do Guarda Volume |
| SeqUso | Number(009,0) | Não | Sequencia de uso |
| TipUgv | Number(001,0) | Sim | Tipo de Usuário do Guarda Volume |
| NumEmp | Number(004,0) | Sim | Empresa do Colaborador |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| CadOcr | Number(009,0) | Sim | Cadastro do Colaborador de Outra Unidade |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |
| NumMat | String(015) | Sim | Matrícula do Aluno |
| DesObj | String(254) | Sim | Descrição Objeto |
| DatRet | Date | Sim | Data de Retirada do Guarda Volume |
| HorRet | Number(005,0) | Sim | Hora da Retirada do Guarda Volume |
| NumCan | Number(007,0) | Sim | Cadastro do Candidato |

---

## Chave Primária

- CodGvl
- DatUso
- HorUso
- SeqUso

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R065MGV_000

**Tabela:** R065GVL

| Origem | Destino |
|--------|---------|
| CodGvl | CodGvl |

