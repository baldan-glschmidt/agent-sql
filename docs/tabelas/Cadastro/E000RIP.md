# E000RIP

## Descrição

Tabelas - Integrações - Retornos de Integração

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqRip | Number(009,0) | Não | Número sequencial dos registros de retorno da integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| IdeInt | Number(009,0) | Não | Código Identificador do tipo de informação |
| CodInt | Number(002,0) | Não | Código do sistema integrado |
| IdeExt | Number(009,0) | Não | Código Identificador externo do registro |
| InfRet | String(7999) | Sim | Informação das chaves que devem retornar |

---

## Chave Primária

- SeqRip

---

## Índices

### E000RIPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

Nenhum relacionamento cadastrado.
