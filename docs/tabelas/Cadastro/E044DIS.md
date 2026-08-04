# E044DIS

## Descrição

Cadastros - Tabela de Distribuição de Custo

---

## Resumo

- Campos: 19
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| ClaCta | String(030) | Sim | Classificação da conta contábil |
| SeqDis | Number(009,0) | Não | Sequência da Distribuição da Matriz |
| NumTab | Number(009,0) | Não | Numero da Tabela da Matriz de Distribuição de Custos |
| TipCcu | Number(001,0) | Não | Tipo do centro de custos |
| NumMat | Number(009,0) | Não | Numero da Tabela de Competência Matriz de Distribuição de Gastos |
| LgnTip | String(001) | Não | Considera Tipo de Centro de Custo |
| NumTrf | Number(009,0) | Não | Numero da Tabela da Matriz de Zeramento Contábil |
| UsuExe | Number(010,0) | Sim | Usuário responsável pela execução. |
| DatExe | Date | Sim | Data da última Execução |
| HorExe | Number(005,0) | Sim | Hora da última Execução |
| UsuGer | Number(010,0) | Sim | Identificador do usuário |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Identificador do usuário |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E044DISIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- SeqDis

---

## Relacionamentos

Nenhum relacionamento cadastrado.
