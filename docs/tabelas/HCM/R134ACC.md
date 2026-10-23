# R134ACC

## Descrição

Turmas - Registro de Acesso

---

## Resumo

- Campos: 15
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCra | Number(012,0) | Não | Número do Crachá |
| DatAcc | Date | Não | Data do Acesso |
| HorAcc | Number(005,0) | Não | Hora do Acesso |
| SeqAcc | Number(002,0) | Não | Sequência do Registro |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor no Acesso |
| CodFnc | Number(002,0) | Sim | Código da Função no Acesso |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo de Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| CodCua | Number(009,0) | Sim | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Sim | Código da Turma |
| CodHcu | Number(006,0) | Sim | Código do Horário |
| StaFre | Number(001,0) | Sim | Status do registro |
| MsgLog | String(300) | Sim | Mensagem do log do processamento |

---

## Chave Primária

- NumCra
- DatAcc
- HorAcc
- SeqAcc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
