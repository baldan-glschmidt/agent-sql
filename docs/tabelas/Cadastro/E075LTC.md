# E075LTC

## Descrição

Tabelas - Produto - Ligação Transação para Preço de Custo por Produto

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeMes | Number(009,0) | Não | Sequencial registro Custo do Produto por Data |
| IdePcd | Number(009,0) | Não | Sequencial registro Preço Custo por produto e derivação |
| CodEmp | Number(004,0) | Não | Código da empresa |
| DatIni | Date | Não | Data Inicial do período |
| DatFim | Date | Não | Data final do período |
| CodTns | String(005) | Não | Código da transação |
| EstEos | String(001) | Sim | Indicativo se a transação é de entrada ou saída |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E075LTCIndice1

**Tipo:** Unico

Campos:
- DatIni
- DatFim
- CodEmp
- CodTns

---

## Relacionamentos

Nenhum relacionamento cadastrado.
