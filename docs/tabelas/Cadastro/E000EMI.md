# E000EMI

## Descrição

Tabelas - Integração - Requisição de Estoques - Controle de integração

---

## Resumo

- Campos: 9
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
| CodInt | Number(002,0) | Não | Código da integração |
| IdeExt | Number(009,0) | Sim | Identificador externo do registro |
| NumEme | Number(009,0) | Sim | Número da Requisição |
| IdcExt | Number(009,0) | Sim | Identificador Externo Contrato do Registro |
| CtrExt | String(020) | Sim | Número do Contrato Externo |
| EmbExt | String(050) | Sim | Número do Embarque Externo |

---

## Chave Primária

- IdeUni

---

## Índices

### E000EMIIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodInt
- IdeExt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
