# R999PSQ

## Descrição

Configuração da Tela de Pesquisa de Registros

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NomPsq | String(035) | Não | Nome da consulta, normalmente será o nome da tabela |
| CodUsu | Number(010,0) | Não | Código do usuário |
| SrcFrm | String(030) | Não | Nome do form origem |
| AutSho | String(001) | Sim | Mostrar automaticamente os registros |
| OrdCol | String(1999) | Sim | Campos de ordenação |
| AplOpt | Number(002,0) | Sim | Set de opções aplicadas ao mostrar (Localização, Filtro, ...) |
| FndFld | String(050) | Sim | Campo para localizar |
| FndTyp | Number(002,0) | Sim | Tipo de localização |
| FndVal | String(254) | Sim | Valor para localização |
| FltFld | String(050) | Sim | Campo para filtrar |
| FltCon | Number(002,0) | Sim | Condição do filtro |
| FltVal | String(254) | Sim | Valor para filtrar |
| AdvFlt | String(3999) | Sim | Filtro Avançado |
| ActPag | Number(001,0) | Sim | Ficha ativa quando o usuário fecha a tela de pesquisa |

---

## Chave Primária

- NomPsq
- CodUsu
- SrcFrm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
