# R450CNF

## Descrição

Configurações Gerais do Archiving

---

## Resumo

- Campos: 9
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NomLnk | String(020) | Sim | Nome do DBLink |
| DatUAr | Date | Sim | Última Data Transferida para Archiving |
| PerMan | Number(003,0) | Sim | Período Mantido (Meses) |
| TipBas | Number(001,0) | Sim | Tipo de Base |
| ProCad | String(001) | Sim | Atualizar Tabelas Cadastro |
| UsaLnk | String(001) | Sim | Utiliza DBLink |
| QtdCom | Number(005,0) | Sim | Quantidade de Registros Commit na Stored Procedure |
| OwnTab | String(254) | Sim | Schema das Tabelas no Banco de Dados |
| BasArc | String(100) | Sim | Base Histórico Para Conexão Archiving |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
