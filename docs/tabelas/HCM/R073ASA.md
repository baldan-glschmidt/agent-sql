# R073ASA

## Descrição

Autorização de Saída Alunos

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumMat | String(015) | Não | Matrícula do Aluno |
| DatAsa | Date | Não | Data da Autorização de Saída |
| HorAsa | Number(005,0) | Não | Hora da Autorização de Saída |
| HorTer | Number(005,0) | Sim | Hora do Término da Autorização de Saída |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador da Saída |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador da Saída |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador da Saída |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Autorização |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |

---

## Chave Primária

- NumMat
- DatAsa
- HorAsa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
