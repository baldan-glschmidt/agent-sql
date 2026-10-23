# R211PSQ

## Descrição

Pesquisa - Cadastro

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPsq | Number(006,0) | Não | Código da Pesquisa |
| DesPsq | String(060) | Sim | Descrição da Pesquisa |
| CodQue | Number(003,0) | Sim | Código do Questionário |
| TipPsq | String(001) | Sim | Define o tipo da pesquisa |
| ObjPsq | String(1999) | Sim | Objetivo da pesquisa |
| ForApr | Number(001,0) | Sim | Define a forma de identificação |
| OrdApr | Number(001,0) | Sim | Define a ordem dos valores |
| UsaPar | String(001) | Sim | Define se utiliza cadastro de participantes para geração dos identificadores |
| QtdPar | Number(005,0) | Sim | Quantidade de participantes da pesquisa |

---

## Chave Primária

- CodPsq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R211PSQ_002

**Tabela:** R210QUE

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |

