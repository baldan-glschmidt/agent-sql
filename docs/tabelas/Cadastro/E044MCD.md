# E044MCD

## Descrição

Cadastros - Matriz de Distribuição de Custos

---

## Resumo

- Campos: 15
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
| NumTab | Number(009,0) | Não | Número da Tabela |
| DatIni | Date | Não | Data Inicial da Validade |
| DatFim | Date | Não | Data Final da Validade |
| ObsCus | String(250) | Sim | Observação da Matriz de Distribuição de Custos |
| OriMat | String(001) | Sim | Origem da Matriz de Distribuição |
| UsuGer | Number(010,0) | Sim | Identificador do usuário |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Identificador do usuário |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| IdeExt | Number(009,0) | Sim | Identificador externo do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E044MCDIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumTab

---

## Relacionamentos

Nenhum relacionamento cadastrado.
