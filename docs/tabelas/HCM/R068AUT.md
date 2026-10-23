# R068AUT

## Descrição

Autorizados na solicitação de acesso por local físico

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSol | Number(009,0) | Não | Código da Solicitação |
| DatIni | Date | Não | Data Inicial da Solicitação |
| SeqPes | Number(005,0) | Não | Sequência da Pessoa |
| TipPes | Number(001,0) | Sim | Tipo Pessoa |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro Colaborador |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |
| ObsAut | String(100) | Sim | Observação do autorizado |

---

## Chave Primária

- CodSol
- DatIni
- SeqPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
