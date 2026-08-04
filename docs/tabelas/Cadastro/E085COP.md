# E085COP

## Descrição

Cadastros - Clientes - Informações de Cooperado

---

## Resumo

- Campos: 21
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do cliente |
| SeqCoo | Number(009,0) | Não | Sequência do Cadastro de Cooperado |
| NumMat | String(030) | Sim | Número da matrícula do cooperado na cooperativa |
| DatAdm | Date | Sim | Data da admissão do cooperado |
| TipMob | Number(001,0) | Sim | Tipo da mão de obra empregada pelo cooperado |
| QtdEmp | Number(004,0) | Sim | Quantidade de empregados permanentes contratados pelo cooperado |
| QtdEmv | Number(004,0) | Sim | Quantidade de empregados eventuais contratados pelo cooperado |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| LvrAdm | Number(009,0) | Sim | Número do livro de registro de admissão do cooperado |
| PgnAdm | Number(009,0) | Sim | Número da página do livro de admissão de cooperado |
| AtaAdm | Number(009,0) | Sim | Número da linha da ata de admissão do cooperado em assembleia |
| LvrDes | Number(009,0) | Sim | Número do livro de registro de desligamento do cooperado |
| PgnDes | Number(009,0) | Sim | Número da página do livro de desligamento de cooperado |
| AtaDes | Number(009,0) | Sim | Número da linha da ata de desligamento do cooperado em assembleia |
| DatDes | Date | Sim | Data do desligamento na cooperativa |
| SitCop | Number(002,0) | Não | Situação atual do cooperado na cooperativa |

---

## Chave Primária

- CodCli
- SeqCoo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
